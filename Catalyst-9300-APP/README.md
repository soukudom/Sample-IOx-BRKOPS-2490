# Prerequisites

Make sure Docker is installed on your system. You can find installation instructions specific to your operating system on the Docker website.

# Step by Step guide

## Set up your infrastructure

1. Enter configuration mode and enable iox:
   ```
   conf t
   iox
   end
   ```
   Verify the IOX service:
   ```
   sh iox-service 
   ```
   Get info on any installed apps, use the `sh app-hosting ?` command.

2. (Optional) If you need to disable signed verification for app hosting, execute:
   ```
   conf t
   no app-hosting signed-verification
   ```

## Containerize the Application

1. Download or clone this GitHub repository to your local machine.
2. Navigate to the directory containing the Dockerfile and run:
   ```
   docker build -t cleu24-app .
   ```
3. Export the image to a .tar file:
   ```
   docker save cleu24-app:latest -o demo.tar
   ```

Note: Unfortunately the demo.tar has more than 100 MB and cannot be uploaded to Github repository. On the other hand, it is the great opportunity to try docker commands :-)

## Install the Application

Select installation tool and deploy the app. In section below you find details for Cisco Catalyst Center and CLI.

### Option 1: Install via Catalyst Center

1. In Catalyst Center, open *Provision > Services > Application Hosting*.
2. Click "New App" and upload the demo.tar file.
3. Select the uploaded app, click "Install," and follow the installation wizard.

Note: Find more information and a detailed guide in the [Catalyst Center End User Guide](https://www.cisco.com/c/en/us/td/docs/cloud-systems-management/network-automation-and-management/catalyst-center/2-3-7/user_guide/b_cisco_catalyst_center_user_guide_237/b_cisco_dna_center_ug_2_3_7_chapter_01111.html?bookSearch=true#id_132431).

### Option 2: Install via CLI

1. Copy the `demo.tar` file to the SSD (usfblash1) of your Switch.
2. Install the application using the command:
    ```
    app-hosting install appid <app-name> package usbflash1:<docker-tar-file>
    ```
3. Configure network interface for the application
4. Activate and Start the the application
    ```
    app-hosting active appid <app-name> 
    app-hosting start appid <app-name> 
   ```

Note: More detailed information you can find [here](https://developer.cisco.com/docs/app-hosting/#!getting-cat9k-setup). There is much more examples including details, such as networking configuration.


**Verify and Test the app**

1. To Verify the app status, use:
   ```
   sh app-hosting detail appid MYAPP 
   ```

2. Connect to the app 
   ```
   app-hosting connect appid MYAPP session   
   ```

**Stop and Remove app**
1. Stop app
   ```iox
   app-hosting stop appid MYAPP
   ```
2. Deactivate app
   ```iox
   app-hosting deactivate appid MYAPP
   ```
3. Uninstall app
   ```iox
   app-hosting uninstall appid MYAPP
   ```
4. Remove the app-hosting config
   ```iox
   conf t
   no app-hosting appid MYAPP   
   ```