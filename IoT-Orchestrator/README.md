# IoT Orchestrator Asset Tracking Example
Cisco Spaces Connect for IoT Services solution enables delivery of advanced BLE capabilities over Cisco Catalyst Wireless infrastructure. In this example you can see required steps for recieving BLE beacons.
Please make sure you replated variables with values from your network. In the example we have the following variables:
<<IoT-IP>> -> IP address of IoT Orchestrator APP
<<Name of the BLE device>> -> Any name in string format that represents the BLE sensor
<<Mac address of the BLE device>> -> MAC address of the BLE sensor
<<onboarding app ID>> -> Onboarding App ID available in the IoT Orchestrator GUI
<<control app ID>> -> Control App ID available in the IoT Orchestrator GUI
<<ble device id>> -> BLE device ID available in the IoT Orchestrator GUI after sensor registration


Complete configuration guide: https://www.cisco.com/c/dam/en/us/td/docs/wireless/spaces/iot-orchestrator/qsg/spaces-connect-iot-qsg.pdf
1. Onboard sensors
```
curl -k --location 'https://<<IoT-IP>>:8081/scim/v2/Devices' \ # For example: 192.168.104.10
--header 'x-api-key: <<onboard application key>>' \
--header 'Content-Type: application/json' \
--data '
{
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:Device",
    "urn:ietf:params:scim:schemas:extension:ble:2.0:Device",
    "urn:ietf:params:scim:schemas:extension:endpointapps:2.0:Device"
  ],
  "deviceDisplayName": "<<Name of the BLE device>>", # For example: BLE Monitor
  "adminState": true,
  "urn:ietf:params:scim:schemas:extension:ble:2.0:Device": {
    "versionSupport": [
      "5.3"
    ],
    "deviceMacAddress": "<<Mac address of the BLE device>>", # For example: F6:04:FB:B0:92:2D
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
    "onboardingUrl": "<<onboarding app ID>>", # For example: onboardApplication
    "deviceControlUrl": [
      "<<control app ID>>" # For example: controlApplication
    ],
    "dataReceiverUrl": []
  }
} 
```

2. Register the Data Receiver Application
```
curl -k --location 'https://<<IoT-IP>>:8081/control/registration/registerDataApp' \
--header 'Content-Type: application/json' \
--header 'x-api-key: <<control application key>>' \
--data '
{
"controlApp": "<<control app ID>>",
"topic": "enterprise/hospital/advertisements", # any MQTT Topic name
"dataApps": [
{
"dataAppID": "<<data app ID>>" # For example: dataApplication
}
]
}'
```

3. Register Topic
```
curl -k --location 'https://<<IoT-IP>>:8081/control/registration/registerTopic' \
--header 'x-api-key: <<control application key>>' \
--header 'Content-Type: application/json' \
--data '
{
"technology": "ble",
"topic": "enterprise/hospital/advertisements",
"ids": [
  "<<ble device id>>" # For example: "57f85940-ea8e-405f-bc06-b744141db08c"
],
"controlApp": "<<control app ID>>",
"ble": {
"type": "advertisements"
}
}
'
```

4. Get Data
```
mosquitto_sub -h <<IoT-IP>> -p 41883 -t enterprise/hospital/advertisements -u "https://<<data app ID>>" --pw <<control app ID>>
```
