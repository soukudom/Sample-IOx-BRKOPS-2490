# Network-Analysis++
This repository contains a Docker container that processes network traffic using [ipfixprobe](https://github.com/CESNET/ipfixprobe/tree/master) or allows to capture traffic using tcpdump. 

Follow the instructions below to build, install and run  the app
## Build 
* `docker build -t net-analysis .`

## Install 
* The same approach as described in section [Catalyst-9300-APP](/Catalyst-9300-APP/README.md). It is possible to choose Catalyst Center or CLI option.

Note: To make packet capture alive you need to mirror the traffic to the IOx application (TCI Drone). The same is valid for example for CyberVision. Please configure ERSPAN in the IOS-XE. The example is in the `erspan-config.txt`.

## Run
Based on the target use case, you can run one of the available tools to process network traffic from the container environment:
* tcpdump (e.g., tcpdump -i eth0 -n)
* ipfixprobe (e.g., ipfixprobe -i 'pcap;file=capture.pcap' -o 'text')

