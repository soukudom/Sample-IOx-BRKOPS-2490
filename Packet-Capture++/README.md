# Network Packet Capture++
This repository contains a Docker container that allows network packet capture using the Traffic Capture Interface (TCI) solution. TCI is capable of remote and on-demand packet capture in a distributed environment with multiple collection points.

Follow the instructions below to build, install, and run the app.

## Table of Contents

- [Deployment](#deployment)
  - [Build](#build)
  - [Install](#install)
  - [Run](#run)
- [Useful Resources](#useful-resources)

## Deployment
### Build
Installation instructions and build packages are available [here](https://github.com/FETA-Project/TrafficCaptureInfrastructure/tree/main). For packages, please check the Releases section.

If you would like to learn how to build a basic Docker image, please check the sample app for [Catalyst 9000](../Catalyst-9300-APP/README.md) or [Catalyst 9100](../Catalyst-AP-APP/README.md).


### Install
* The installation is done using the same workflow as described in the section [Catalyst-9300-APP](/Catalyst-9300-APP/README.md). It is possible to choose Catalyst Center or CLI option.

> *Note*: To capture live traffic, mirror network traffic to the IOx application (TCI Drone) using ERSPAN. The same approach applies to CyberVision. An example configuration is available in `erspan-config.txt`.

### Run
Follow the Getting Started documentation for the Drone component available [here](https://feta-project.github.io/TrafficCaptureInfrastructure/). After modification of the configuration file, the Drone will try to connect to the Hive component (collection and control point).

## Useful Resources
- [Traffic Capture Infrastructure (GitHub)](https://github.com/FETA-Project/TrafficCaptureInfrastructure/tree/main)
- [Traffic Capture Infrastructure Documentation](https://feta-project.github.io/TrafficCaptureInfrastructure/)
