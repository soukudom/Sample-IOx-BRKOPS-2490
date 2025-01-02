# Catalyst AP APP
This is a sample application that demonstrates a simple web server running on Cisco Catalyst 9100 Access Points.

## Prerequisites
1. [Download ioxclient](https://developer.cisco.com/docs/iox/#!iox-resource-downloads). The tool `ioxclient` is required to convert docker image to the proper format for Catalyst APs. You can also install the IOx SDE which is an Ubuntu VM (14.04) with all the tools (docker, ioxclient) required to build an IOx application package pre-installed. 
2. Install Docker (see details based on your OS).

## Step by Step deployment 

### Create your Application File
1. Download or clone this GitHub repository to your local machine.
2. Navigate to the directory containing the Dockerfile and run:
    ```
    docker build -t web-ap-app .
    ```
    To verify the the image, use:
    ```
    docker images
    ```
    - On an x86_64-based architecture you can use QEMU to emulate the ARM architecture. To do this, uncomment lines 2 and 6 in the Dockerfile and run:
    `docker build --platform linux/arm64 -t arm64-web-ap-app .` 

    - If you build the docker image in a different environment than on your linux machine (where ioxclient is intstalled), save the docker image as .tar file, copy it and load it on the destination host: `docker save web-ap-app:latest -o demo.tar`, then load the docker image on the destiantion `docker load -i demo.tar`.

3. Once the docker image is created, use `ioxclient` to create the package file:
    ```
    ioxclient docker package -p ext2 web-ap-app ./conf
    ```
   Check if successfully has been created:
   ```
   ls -lr ./conf
   ```
6. Select installation tool and deploy the app. In section below you find details for Cisco Catalyst Center and ioxclient

Note: A Package of the sample app (`package.tar`) and a packaged `demo.tar` Docker container are available in the `/packages` directory.

### Set up the Infrastructure
Before installation enable the IOx feature on your C9800 controller:
```
conf t
ap profile default-ap-profile
apphost
end
``` 
To verify if apphost is enabled on your 9800 controller, use `sh ap apphost summary`.

### Install the Application

Select installation tool and deploy the app. In section below you find details for Cisco Catalyst Center and CLI.

#### Option 1: Install via Catalyst Center
1. In Catalyst Center, open *Provision > Services > IoT Services*.
2. Click "New App" and upload the `package.tar` file.
3. Click on the uploaded app dash, select "Install" and follow the installation wizard.

<img src="img/ap-app-hosting-catc.gif" width="700">

Note: Find more information and a detailed guide in the [Application Hosting on Catalyst Access Points Deployment Guide](https://www.cisco.com/c/en/us/products/collateral/wireless/access-points/guide-c07-744305.html).

#### Option 2: Install via ioxclient
1. Configure an `ioxclient` profile:
    ```
    ioxclient profiles create
    ```
    To verify the active profile, use `ioxclient profiles list`.
2.  Install the application using the command.
    ```
    ioxclient app install CLEUAPP package.tar
    ```
3.  To activate the app use:
    ```
    ioxclient app activate CLEUAPP --payload activation.json
    ``` 
4.  Now, start the app
    ```
    ioxclient app start CLEUAPP
    ``` 
![StartApp](./../img/install-activate-start.png)

Note: Find more information on the Cisco DevNet site on how to [Deploy IOx Application on AP Using ioxclient](https://developer.cisco.com/docs/app-hosting-ap/deploy-iox-application-on-ap-using-ioxclient/).

<img src="img/ioxclient.gif" width="700">

**Verify the app**
1. To Verify the installed apps, check the app status, or to validate configuration, use:
    ```iox
    ioxclient application list
    ioxclient application info CLEUAPP
    ```

**Verify and Test the app from the AP itself**
1. To Verify the app status, use:
    ```iox
    sh iox applications
    ```

2. Connect to the app 
    ```iox
    connect iox application
    ```
    Note that this command is not supported on Console, use SSH session to connect.
    
**Stop and Remove app**
1. Stop, remove and uninstall the app:
   ```iox
    ioxclient app stop CLEUAPP
    ioxclient app deactivate CLEUAPP
    ioxclient app uninstall CLEUAPP
   ```
![StopApp](./../img/uninstall-deactivate-stop.png)


---
## Useful Resources  

- [Cisco Developer Documentation - Application Hosting on Cisco Catalyst Access Points](https://developer.cisco.com/docs/app-hosting-ap/application-hosting-on-cisco-catalyst-access-points-application-hosting-on-cisco-catalyst-access-points/)  
  Comprehensive guide on application hosting, including setup, configuration, and examples.  

- [Application Hosting on Catalyst Access Points Deployment Guide](https://www.cisco.com/c/en/us/products/collateral/wireless/access-points/guide-c07-744305.html)  
  Deployment guide for application hosting on Cisco Catalyst Access Points.  

---


