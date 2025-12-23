# decode_mqtt_stream.py
import sys
import os
import binascii
import struct # For parsing binary data

# --- Setup for Protobuf Imports ---
# Add the current directory to sys.path to import generated protobuf modules
# This assumes the script is run from the directory where data_app_pb2.py is located,
# or that this directory is added to PYTHONPATH.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    import data_app_pb2
    from google.protobuf.timestamp_pb2 import Timestamp # Required for timestamp handling
except ImportError:
    print("Error: Could not import protobuf generated files (e.g., data_app_pb2.py).", file=sys.stderr)
    print("Please ensure you have compiled data_app.proto using 'protoc --proto_path=. --python_out=. data_app.proto' in the same directory.", file=sys.stderr)
    sys.exit(1)

# --- BLE Advertisement Parsing Logic ---
# This function parses the raw BLE Advertisement Data (AD structures).
# It includes basic parsing for common AD types like Flags, Service UUIDs, Local Name,
# and Manufacturer Specific Data (0xFF), with specific handlers for iBeacon and Eddystone.
# For Kontakt.io's proprietary data formats, you would need to extend this function
# based on their specific documentation for Manufacturer Specific Data.
def parse_ble_advertisement_data(raw_adv_data_bytes):
    parsed_data = {}
    i = 0
    while i < len(raw_adv_data_bytes):
        # Each AD structure starts with a length byte
        length = raw_adv_data_bytes[i]
        if length == 0:
            break # Length 0 indicates the end of AD structures

        # Ensure we don't read past the end of the total raw_adv_data_bytes
        if i + 1 >= len(raw_adv_data_bytes):
            break # Malformed or truncated AD structure

        # AD Type byte
        ad_type = raw_adv_data_bytes[i+1]
        # The actual data for this AD structure (length-1 bytes)
        ad_data = raw_adv_data_bytes[i+2 : i+1+length]

        # --- Common Bluetooth SIG AD Types ---
        if ad_type == 0x01:
            parsed_data['flags'] = f"0x{ad_data[0]:02x}"
        elif ad_type in [0x02, 0x03]:
            parsed_data.setdefault('service_uuids_16bit', []).extend([f"0x{struct.unpack('<H', ad_data[j:j+2])[0]:04x}" for j in range(0, len(ad_data), 2)])
        elif ad_type in [0x06, 0x07]:
            parsed_data.setdefault('service_uuids_128bit', []).extend([ad_data[j:j+16].hex() for j in range(0, len(ad_data), 16)])
        elif ad_type == 0x09:
            parsed_data['local_name'] = ad_data.decode('utf-8', errors='ignore')
        elif ad_type == 0xFF:
            if len(ad_data) >= 2:
                company_id = struct.unpack('<H', ad_data[0:2])[0] 
                parsed_data['manufacturer_id'] = f"0x{company_id:04x}"
                parsed_data['manufacturer_data_raw'] = ad_data[2:].hex()

                # --- Specific Manufacturer Data Formats ---
                # iBeacon (Apple Company ID 0x004C)
                if company_id == 0x004C and len(ad_data) >= 23 and ad_data[2] == 0x02 and ad_data[3] == 0x15:
                    parsed_data['iBeacon'] = {
                        'uuid': ad_data[4:20].hex(),
                        'major': struct.unpack('>H', ad_data[20:22])[0],
                        'minor': struct.unpack('>H', ad_data[22:24])[0],
                        'tx_power': struct.unpack('>b', ad_data[24:25])[0]
                    }
                # Eddystone UID (Google Company ID 0x00FE, Frame Type 0x00)
                elif company_id == 0x00FE and len(ad_data) >= 20 and ad_data[2] == 0x00:
                     parsed_data['eddystone_uid'] = {
                         'tx_power': struct.unpack('>b', ad_data[3:4])[0],
                         'namespace_id': ad_data[4:14].hex(),
                         'instance_id': ad_data[14:20].hex()
                     }
                # Eddystone URL (Google Company ID 0x00FE, Frame Type 0x10)
                elif company_id == 0x00FE and len(ad_data) >= 4 and ad_data[2] == 0x10:
                     parsed_data['eddystone_url_tx_power'] = struct.unpack('>b', ad_data[3:4])[0]
                     # URL encoding/decoding is more complex, storing raw hex for now
                     parsed_data['eddystone_url_raw'] = ad_data[4:].hex()
                
                # --- Kontakt.io Specific Data ---
                # To parse Kontakt.io's proprietary data (e.g., Secure Shuffling, Asset Tag data),
                # you would need to add specific logic here. Kontakt.io uses its own Company ID
                # (e.g., 0x0078 for Kontakt.io, check their documentation for exact ID and formats).
                # Example (hypothetical, based on Kontakt.io docs):
                # elif company_id == 0x0078: # Replace with actual Kontakt.io Company ID
                #     # Parse ad_data[2:] according to Kontakt.io's specific format
                #     # This might involve checking frame types within their data
                #     parsed_data['kontakt_io_specific'] = "..."

        # Move to the next AD structure
        i += length + 1
    return parsed_data

# --- Main Protobuf Decoding and Printing Logic ---
def decode_and_print_message(hex_data_string, topic=None):
    """
    Decodes a single hexadecimal Protobuf string (DataBatch)
    and prints its content, including parsed BLE advertisement data.
    """
    try:
        # Convert hex string to binary bytes
        binary_data = binascii.unhexlify(hex_data_string.strip())
    except binascii.Error as e:
        print(f"Error: Invalid hex string '{hex_data_string.strip()}': {e}", file=sys.stderr)
        return

    # Create an instance of the top-level message (DataBatch)
    data_batch = data_app_pb2.DataBatch()

    try:
        # Parse the binary data into the protobuf message
        data_batch.ParseFromString(binary_data)
        
        if topic:
            print(f"--- Topic: {topic} ---")
        
        # Iterate through each DataSubscription message in the batch
        for subscription in data_batch.messages:
            print("  DataSubscription:")
            
            if subscription.HasField('device_id'):
                print(f"    Device ID: {subscription.device_id}")
            
            # Convert Protobuf timestamp to human-readable ISO format
            if subscription.HasField('timestamp'):
                dt_object = subscription.timestamp.ToDatetime()
                print(f"    Timestamp: {dt_object.isoformat()}")
            
            if subscription.HasField('ap_mac_address'):
                print(f"    AP MAC Address: {subscription.ap_mac_address}")
            
            # Check if it's a BLE Advertisement type
            if subscription.HasField('ble_advertisement'):
                print("    BLE Advertisement (from Protobuf metadata):")
                print(f"      MAC Address: {subscription.ble_advertisement.mac_address}")
                if subscription.ble_advertisement.HasField('rssi'):
                    print(f"      RSSI: {subscription.ble_advertisement.rssi}")
            
            # Now, parse the raw 'data' field which contains the actual BLE advertisement packet
            if subscription.data:
                print(f"    Raw Advertisement Data (Hex from 'data' field): {subscription.data.hex()}")
                parsed_adv = parse_ble_advertisement_data(subscription.data)
                if parsed_adv:
                    print("    Parsed Advertisement Data (from raw 'data' field):")
                    for key, value in parsed_adv.items():
                        print(f"      {key}: {value}")
            
            # You can add logic here to handle other subscription types
            # elif subscription.HasField('ble_subscription'):
            #     print("    BLE Subscription Data:")
            #     print(f"      Service UUID: {subscription.ble_subscription.service_uuid}")
            #     print(f"      Characteristic UUID: {subscription.ble_subscription.characteristic_uuid}")
            # ... and so on for other types in the oneof field

        print("-" * 40) # Separator for readability

    except Exception as e:
        print(f"Error parsing protobuf data from hex '{hex_data_string.strip()}': {e}", file=sys.stderr)

# --- Main execution block for reading from stdin ---
def main():
    print("Waiting for MQTT data... (Press Ctrl+C to exit)")
    for line in sys.stdin:
        line = line.strip()
        if not line: # Skip empty lines
            continue

        # Split the line into topic and hex_payload based on the first space
        parts = line.split(' ', 1)

        if len(parts) == 2:
            topic = parts[0]
            hex_payload = parts[1]
            decode_and_print_message(hex_payload, topic)
        else:
            # This case might happen if the line format is unexpected
            print(f"Warning: Unexpected line format, skipping: '{line}'", file=sys.stderr)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting decoder.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)