## Simple iPerf App with Graphical User Interface

1. Create image, specify target platform
```
docker build --platform linux/amd64 -t iperf3-app .
```
2. save docker file
```
docker save iperf3-app -o demo.tar
```
3. Deploy the app on your Catalyst Switch as described in section [Catalyst-9300-APP](/Catalyst-9300-APP/README.md). 
