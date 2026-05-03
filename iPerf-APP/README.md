# Simple iPerf App with Graphical User Interface

This sample app packages an iPerf3-based throughput test utility with a simple web UI. It is intended for Cisco Catalyst app hosting environments where you want a quick way to run bandwidth tests from a hosted application.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Deployment](#deployment)
  - [Build](#build)
  - [Install](#install)
- [Useful Resources](#useful-resources)

## Prerequisites

- Docker installed on your build machine
- A Cisco Catalyst switch with application hosting enabled

## Deployment

### Build
1. Create image, specify target platform
```
docker build --platform linux/amd64 -t iperf3-app .
```
2. save docker file
```
docker save iperf3-app -o iperf-demo.tar
```
### Install
3. Deploy the app on your Catalyst Switch as described in section [Catalyst-9300-APP](/Catalyst-9300-APP/README.md). 
For more info check this [link](https://www.cisco.com/c/en/us/support/docs/switches/catalyst-9200-series-switches/220197-use-iperf-on-catalyst-9000-switches-to-p.html)

## Useful Resources
- [Catalyst 9000 iPerf Usage Guide](https://www.cisco.com/c/en/us/support/docs/switches/catalyst-9200-series-switches/220197-use-iperf-on-catalyst-9000-switches-to-p.html)
- [Catalyst 9300 App Hosting Sample](../Catalyst-9300-APP/README.md)
- [Cisco Application Hosting Introduction](https://developer.cisco.com/docs/app-hosting/introduction/)
