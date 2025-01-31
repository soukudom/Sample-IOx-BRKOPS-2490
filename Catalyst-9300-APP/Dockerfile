# build this image on x86_64 based architecuture 
# if using arm-based environment, use simple cross-compilation build `docker build --platform linux/arm64 -t web-ap-app .`

FROM python:3-alpine

RUN apk add --update python3
RUN pip3 install bottle

EXPOSE 8000 

COPY main.py /main.py 
CMD ["python3", "/main.py"]
