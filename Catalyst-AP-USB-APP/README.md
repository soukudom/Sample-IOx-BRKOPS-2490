# Catalyst AP USB APP
This is a getting application to demontrate a simple use case with USB based appliacation. For demonstration we use USB dongle with Zigbee support and [Zigbee2mqtt application](https://www.zigbee2mqtt.io/)

## Prerequisites
1. [Download ioxclient](https://developer.cisco.com/docs/iox/#!iox-resource-downloads). The tool `ioxclient` is required to convert docker image to the proper format for Catalyst APs. You can also install the IOx SDE which is an Ubuntu VM (14.04) with all the tools (docker, ioxclient) required to build an IOx application package pre-installed. 
2. Install Docker (see details based on your OS).
3. Get compatible USB dongle (see [Access AP's Internal USB interface](https://developer.cisco.com/docs/app-hosting-ap/create-an-iox-application-package/#create-an-iox-application-package) section). For this example we used SkyConnect dongle and Sonoff ZBDongle-P dongle. 

## Step by Step deployment 

### Create your Application File
1. Download or clone this GitHub repository to your local machine. 

2. User directly `package.tar` for installation and continue with next section, or pull the docker image for zigbee2mqtt app 

3. Once the docker image is pulled, use `ioxclient` to create the package file:
    ```
    ioxclient docker package -p ext2 zigbee2mqtt:latest ./conf
    ```
   Check if successfully has been created:
   ```
   ls -lr ./conf
   ```

### Set up the Infrastructure
Before installation enable the IOx feature on your C9800 controller:
```
conf t
ap profile default-ap-profile
apphost
usb-enable
end
``` 
To verify if apphost is enabled on your 9800 controller, use `sh ap apphost summary`.
Note: for USB based apps it is necessary to have required PoE budget (typically 60W and more)

### Install the Application

Use `ioxclient` to install the app since it supports enhanced options required for USB based apps 

1. Configure an `ioxclient` profile. For this, you need to specify a name, the AP's IP address, the AP's username & password and change the IOx platform's SSH Port to 22:
    ```
    ioxclient profiles create
    ```
    To verify the active profile, use `ioxclient profiles list`.
2.  Install the application by pointing to your locally stored package file:
    ```
    ioxclient app install zigbee2mqtt package.tar
    ```
3.  Then, activate the app togeher with the `activation.json` file
    ```
    ioxclient app activate zigbee2mqtt --payload activation.json
    ``` 
4.  Now, start the app:
    ```
    ioxclient app start zigbee2mqtt
    ``` 

**Verify the app**
1. To Verify the installed apps, check the app status, or to validate configuration, use:
    ```iox
    ioxclient application list
    ioxclient application info zigbee2mqtt
    ```

**Start the webserver environment for configuration**
1. Connect to the app 
    ```iox
    connect iox application
    ```
    Note that this command is not supported on Console, use SSH session to connect.
2. Start the web server
    ```
    cd app
    node index.js
    ```
**Configure the zigbee2mqtt app**
1. In web browser open http://<access-point-IP>:8080
2. Validate path for USB dongle, set valid driver and define mqtt broker connect
    * USB path: /dev/ttyUSB
    * Driver: zstack (for Sonoff), ember (for SkyConnect) 
    * Select frontend access (for easier control of the Zigbee network)
3. Rest of parameter can we in default. They can be changed later.
4. Save the initial configuration and validate the zigbee2mqtt live logs in the console

Note: If you select wrong USB driver or the connection towards mqtt broker does not work, the app will not shut down 
    

---
## Useful Resources  

- [Cisco Developer Documentation - Application Hosting on Cisco Catalyst Access Points](https://developer.cisco.com/docs/app-hosting-ap/application-hosting-on-cisco-catalyst-access-points-application-hosting-on-cisco-catalyst-access-points/)  
  Comprehensive guide on application hosting, including setup, configuration, and examples.  

- [Application Hosting on Catalyst Access Points Deployment Guide](https://www.cisco.com/c/en/us/products/collateral/wireless/access-points/guide-c07-744305.html)  
  Deployment guide for application hosting on Cisco Catalyst Access Points.  

---


