# Network Packet Capture++
This repository contains a Docker container that allows network packet capture unsing Traffic Capture Interface (TCI) solution. TCI is capable of remote and on demand packet captures in distributed environment with multiple collection points. 

Follow the instructions below to build, install and run the app.

## Build 
Installation instructions and build packages are available [here](https://github.com/FETA-Project/TrafficCaptureInfrastructure/tree/main). For packages please check the Release section. 

If you would like to learn how to build basic docker image, please check the sample app for Catalyst 9000 or Catalyst 9100 


## Install via Catalyst Center
* The installation is done using the same workflow  as described in the section [Catalyst-9300-APP](/Catalyst-9300-APP/README.md). It is possible to choose Catalyst Center or CLI option. 

Note: To make packet capture alive you need to mirror the traffic to the IOx application (TCI Drone). The same is valid for example for CyberVision. Please configure ERSPAN in the IOS-XE. The example is in the `erspan-config.txt`.

## Run
Follow the Getting started documentation for Drone component available [here](https://feta-project.github.io/TrafficCaptureInfrastructure/). After modification of the configuration file the Drone will try to connect to the Hive compoment (collection and control point). 
