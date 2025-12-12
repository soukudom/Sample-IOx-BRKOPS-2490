# IoT Orchestrator Asset Tracking Example
Cisco Spaces Connect for IoT Services solution enables delivery of advanced BLE capabilities over Cisco Catalyst Wireless infrastructure. 

## Prerequisite
Follow the complete [IoT Orchestrator Configuration Guide](https://www.cisco.com/c/dam/en/us/td/docs/wireless/spaces/iot-orchestrator/qsg/spaces-connect-iot-qsg.pdf) to set up the IoT Orchestrator on your 9800 Controller. 

Make sure that you uploaded the `server.key` and the certificate and that you have created the application keys in the IoT Orchestrator GUI.

This example specifically walks you through the process of:
1. Onboarding a BLE sensor.
2. Registering a data receiver application to consume sensor data.
3. Registering a topic to specify the type of BLE data to receive.
4. Subscribing to the MQTT topic to retrieve the BLE beacon advertisements.

## Variables
Please make sure you replace the placeholder variables below with values specific to your network and IoT Orchestrator setup.
- `[[IoT-IP]]` -> IP address of IoT Orchestrator APP
- `[[Name of the BLE device]]` -> Any name in string format that represents the BLE sensor
- `[[MAC ADDRESS]]` -> MAC address of the BLE sensor
- `[[ONBOARD APP ID]]` -> Onboarding App ID available in the IoT Orchestrator GUI* (# For example: **onboardApplication**)
- `[[CONTROL APP ID]]` -> Control App ID available in the IoT Orchestrator GUI* (For example: **controlApplication**)
- `[[DATA APP ID]]` -> Data App ID available in the IoT Orchestrator GUI* (For example: **dataApplication**)
- `[[ONBOARD APP KEY]]` -> Onboarding App Key available in the IoT Orchestrator GUI*
- `[[CONTROL APP KEY]]` -> Control App Key available in the IoT Orchestrator GUI*
- `[[BLE DEVICE ID]]` -> BLE device ID available in the IoT Orchestrator GUI after sensor registration**

*) Under *Administration > App Registration > Show Registered Apps*\
**) Under *Inventory > BLE Client*

## Steps

### 1. Onboard Sensors
```bash
curl -k --location 'https://[[IoT-IP]]:8081/scim/v2/Devices' \ # For example: 192.168.104.10
--header 'x-api-key: [[ONBOARD APP KEY]]' \
--header 'Content-Type: application/json' \
--data '{
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:Device",
    "urn:ietf:params:scim:schemas:extension:ble:2.0:Device",
    "urn:ietf:params:scim:schemas:extension:endpointapps:2.0:Device"
  ],
  "deviceDisplayName": "[[Name of the BLE device]]", # For example: BLE Monitor
  "adminState": true,
  "urn:ietf:params:scim:schemas:extension:ble:2.0:Device": {
    "versionSupport": [
      "5.3"
    ],
    "deviceMacAddress": "[[MAC ADDRESS]]", # For example: F6:04:FB:B0:92:2D
    "isRandom": false,
    "mobility": false,
    "pairingMethods": [
      "urn:ietf:params:scim:schemas:extension:pairingNull:2.0:Device",
      "urn:ietf:params:scim:schemas:extension:pairingJustWorks:2.0:Device"
    ],
    "urn:ietf:params:scim:schemas:extension:pairingNull:2.0:Device": null,
    "urn:ietf:params:scim:schemas:extension:pairingJustWorks:2.0:Device": {
      "key": null
    }
  },
  "urn:ietf:params:scim:schemas:extension:endpointAppsExt:2.0:Device": {
    "onboardingUrl": "[[ONBOARD APP ID]]",
    "deviceControlUrl": [
      "[[CONTROL APP ID]]"
    ],
    "dataReceiverUrl": []
  }
}'
```

### 2. Register the Data Receiver Application
```bash
curl -k --location 'https://[[IoT-IP]]:8081/control/registration/registerDataApp' \
--header 'Content-Type: application/json' \
--header 'x-api-key: [[CONTROL APP KEY]]' \
--data '
{
"controlApp": "[[CONTROL APP ID]]",
"topic": "enterprise/hospital/advertisements", # any MQTT Topic name
"dataApps": [
{
"dataAppID": "[[DATA APP ID]]"
}
]
}'
```

### 3. Register Topic
```bash
curl -k --location 'https://[[IoT-IP]]:8081/control/registration/registerTopic' \
--header 'x-api-key: [[CONTROL APP KEY]]' \
--header 'Content-Type: application/json' \
--data '
{
"technology": "ble",
"topic": "enterprise/hospital/advertisements",
"ids": [
  "[[BLE DEVICE ID]]" # For example: "57f85940-ea8e-405f-bc06-b744141db08c"
],
"controlApp": "[[CONTROL APP ID]]",
"ble": {
"type": "advertisements"
}
}'
```

### 4. Get Data
```bash
mosquitto_sub -h [[IoT-IP]] -p 41883 -t enterprise/hospital/advertisements -u "https://[[DATA APP ID]]" --pw [[CONTROL APP ID]]
```
