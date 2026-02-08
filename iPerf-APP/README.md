## Simple iPerf App with Graphical User Interface

1. Create image, specify target platform
```
docker build --platform linux/amd64 -t iperf3-app .
```
2. save docker file
```
docker save iperf3-app -o iperf-demo.tar
```
3. Deploy the app on your Catalyst Switch as described in section [Catalyst-9300-APP](/Catalyst-9300-APP/README.md). 
For more info check this [link](https://www.cisco.com/c/en/us/support/docs/switches/catalyst-9200-series-switches/220197-use-iperf-on-catalyst-9000-switches-to-p.html)
