# ASAc Getting Started Example
ASAc enables you to run a firewall application directly on a Cisco Catalyst 9000 switch. This example shows the installation workflow together with the required IOS-XE and ASA-side network configuration.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Folder Overview](#folder-overview)
- [Deployment](#deployment)
- [Verify](#verify)
- [Useful Resources](#useful-resources)

## Prerequisites

Before starting, make sure you have:

1. A Cisco Catalyst 9000 switch with application hosting enabled.
2. The ASAc application package you want to deploy.

## Folder Overview

- [day0-config.txt](./day0-config.txt): Initial ASAc bootstrap configuration.
- [interface-config.txt](./interface-config.txt): Example interface configuration.
- [asac-sample-dayN-config.txt](./asac-sample-dayN-config.txt): Sample ASA-side day-N configuration.
- [switch-sample-dayN-config.txt](./switch-sample-dayN-config.txt): Sample switch-side day-N configuration.


## Deployment
Full installation steps for Cisco application hosting are documented [here](https://developer.cisco.com/docs/app-hosting/introduction/).

In general you need to follow these steps:
1. Download the ASAc application package and review the configuration artifacts in this folder:
	- [day0-config.txt](./day0-config.txt)
	- [interface-config.txt](./interface-config.txt)
2. Install the ASAc application on the switch by following the Cisco application hosting workflow.
3. Apply the switch-side and ASA-side configuration using these example files:
	- [switch-sample-dayN-config.txt](./switch-sample-dayN-config.txt)
	- [asac-sample-dayN-config.txt](./asac-sample-dayN-config.txt)

## Verify

After installation, verify that:

1. The ASAc application is installed and running in the application hosting environment.
2. The switch-side configuration from `switch-sample-dayN-config.txt` is applied successfully.
3. You can access the ASAc console and switch from the Linux shell to the ASA CLI with
    ```
    lina_cli
    ```
4. The ASA-side configuration from `asac-sample-dayN-config.txt` is applied as expected.

## Useful Resources

- [Cisco ASAc Application Deployment](https://developer.cisco.com/docs/app-hosting/introduction/)
