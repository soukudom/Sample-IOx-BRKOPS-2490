# How to build the code
1. Install Docker (see details based on your OS)
2. Download this repository
3. Inside this directory run `docker build -t cleu24-app .`
4. Save docker image with `docker save cleu24-app:latest -o demo.tar`
5. Select installation tool and deploy the app. In section below you find details for Cisco Catalyst Center and CLI

Note: Unfortunately the demo.tar has more than 100 MB and cannot be uploaded to Github repository. On the other hand, it is the great opportunity to try docker commands :-) 


# Install via Catalyst Center
1. Select Provision -> App Hosting for Switches
2. Click New App and upload the saved docker tar file
3. Click on the uploaded app dash, select Install and follow the wizard 

# Install via CLI
1. Copy docker tar file to usbflash
2. Check if IOx is enabled & check its configuration (e.g., certificate validation)
3. Install the app using `app-hosting install appid <app-name> package usbflash1:<docker-tar-file>`
4. Configure network interface for the appid
5. Activate and Start the appid 


Note: More detailed information you can find [here](https://developer.cisco.com/docs/app-hosting/#!getting-cat9k-setup). There is much more examples including details, such as networking configuration.
