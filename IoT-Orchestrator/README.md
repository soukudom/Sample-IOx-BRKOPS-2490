# IoT Orchestrator Asset Tracking Example

1. Onboard sensors
```
curl -k --location 'https://192.168.104.10:8081/scim/v2/Devices' \
--header 'x-api-key: a067144f95abbc66410333a883945fa83b49fee58daa7656ce88a72b6b6704cc' \
--header 'Content-Type: application/json' \
--data '
{
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:Device",
    "urn:ietf:params:scim:schemas:extension:ble:2.0:Device",
    "urn:ietf:params:scim:schemas:extension:endpointapps:2.0:Device"
  ],
  "deviceDisplayName": "BLE Heart Monitor",
  "adminState": true,
  "urn:ietf:params:scim:schemas:extension:ble:2.0:Device": {
    "versionSupport": [
      "5.3"
    ],
    "deviceMacAddress": "F6:04:FB:B0:92:2D",
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
    "onboardingUrl": "onboardApplication",
    "deviceControlUrl": [
      "controlApplication"
    ],
    "dataReceiverUrl": []
  }
} ```

2.

3.

4.

5.
