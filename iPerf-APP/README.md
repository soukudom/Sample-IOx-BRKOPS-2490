## Simple iPerf App with Graphical User Interface

1. Create image, specify target platform
```
docker build --platform linux/amd64 -t iperf3-app .
```
2. save docker file
```
docker save iperf3-app -o demo.tar
```
3. Deploy the app on your Catalyst Switch. Find more infos [here](https://github.com/soukudom/Sample-IOx-BRKOPS-2490/blob/main/Catalyst-9300-APP/README.md).

