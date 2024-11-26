# Prerequisites

Make sure Docker is installed on your system. You can find installation instructions specific to your operating system on the Docker website.

# Step by Step guide

## Set up your infrastructure

1. Enable app hosting on the Switch:

   ```
   conf t
   iox
   end
   ```

   To verify, run:

   ```
   sh iox-service 
   ```

   Get info on any installed apps, use the `   sh app-hosting ?` command.
2. If required, disable validation

   ```
   conf t
   no app-hosting signed-verification
   ```

## Containerize the Application

1. Download or clone this GitHub repository to your local machine.
2. Inside this directory run
   ```
   docker build -t cleu24-app .
   ```
3. Save docker image
   ```
   docker save cleu24-app:latest -o demo.tar
   ```

Note: Unfortunately the demo.tar has more than 100 MB and cannot be uploaded to Github repository. On the other hand, it is the great opportunity to try docker commands :-)

## Install the application

Select installation tool and deploy the app. In section below you find details for Cisco Catalyst Center and CLI

### Install via Catalyst Center

1. In Catalyst Center, open *Provision > Services > Application Hosting*.
2. Click New App and upload the saved docker .tar file.
3. Click on the uploaded app dash, select Install and follow the wizard.

Note: Find more information and a detailed guide in the [Catalyst Center End User Guide](https://www.cisco.com/c/en/us/td/docs/cloud-systems-management/network-automation-and-management/catalyst-center/2-3-7/user_guide/b_cisco_catalyst_center_user_guide_237/b_cisco_dna_center_ug_2_3_7_chapter_01111.html?bookSearch=true#id_132431).

### Install via CLI

1. Copy the `demo.tar` file to the SSD (usfblash1) of your Switch.
2. Check if IOx is enabled & check its configuration (e.g., certificate validation)
3. Install the app using 
    ```
    app-hosting install appid <app-name> package usbflash1:<docker-tar-file>
    ```
4. Configure network interface for the appid
5. Activate and Start the appid
    ```
    app-hosting active appid MYAPP
    app-hosting start appid MYAPP
   ```

**Verify and Test the app**

To Verify the app status, use:
```
sh app-hosting detail appid MYAPP 
```

Connect to the app 
```
app-hosting connect appid MYAPP session   
```

Note: More detailed information you can find [here](https://developer.cisco.com/docs/app-hosting/#!getting-cat9k-setup). There is much more examples including details, such as networking configuration.