# How to build the code 
1. [Download the ioxclient](https://developer.cisco.com/docs/iox/#!iox-resource-downloads)
The tool ioxclient is required to convert docker image to the proper format for Catalyst APs. 
2. Install Docker (see details based on your OS)
3. Download this repository
4. Inside this directory run `docker build -t web-ap-app .`
5. Create IOx application `ioxclient docker package -p ext2 web-ap-app ./conf`
6. Select installation tool and deploy the app. In section below you find details for Cisco Catalyst Center and ioxclient

Note: Packages of sample app are available in the package directory

# Install via Catalyst Center
1. Go to Provision -> IoT Services
2. Select New App and upload the tar file for the ioxclient
3. Click on the uploaded app dash, select Install and follow the wizard

Note: In hierarchy you need to go to floor level to see available APs

# Install via ioxclient
1. Configure ioxclient profile and deploy the app based on the instructions [here](https://developer.cisco.com/docs/app-hosting-ap/#!deploy-iox-application-on-ap-using-ioxclient/activate-the-iox-application-on-ap)
2. After deployment use `ioxclient app info <app name>` to validate configuration

Note: For console access you can use ioxclient or  AP CLI command `connect iox application`

