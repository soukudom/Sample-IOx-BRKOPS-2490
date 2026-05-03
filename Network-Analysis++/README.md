# Network-Analysis++
This example provides a Docker-based IOx application for network traffic analysis. It supports traffic capture with [tcpdump](https://www.tcpdump.org/) and flow-oriented analysis with [ipfixprobe](https://github.com/CESNET/ipfixprobe/tree/master).

Follow the instructions below to build, install, and run the app.

## Table of Contents

- [Build](#build)
- [Install](#install)
- [Run](#run)

## Build
Build the local Docker image from the `Dockerfile`:

```bash
docker build -t net-analysis .
```

Export the image as a package that you can upload to the switch:

```bash
docker save net-analysis:latest -o net-analysis.tar
```

## Install
Install the app using the same workflow as [Catalyst-9300-APP](/Catalyst-9300-APP/README.md) (Catalyst Center or CLI).
Use `net-analysis.tar` as the application package during deployment.


> *Note*: To capture live traffic, mirror network traffic to the IOx application (TCI Drone) using ERSPAN.  The same is valid for example for CyberVision. An example configuration is available in `erspan-config.txt`.

## Run
After the app is running, use one of the following tools inside the container based on your use case:
* `tcpdump` (e.g., `tcpdump -i eth0 -n`)
* `ipfixprobe` (e.g., `ipfixprobe -i 'raw;ifc=eth0;b=2;p=10' -o 'text'`)

