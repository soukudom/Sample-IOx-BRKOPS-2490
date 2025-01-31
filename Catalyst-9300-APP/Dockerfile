# build this image on x86_64 based architecuture 
# if using arm-based environment, use simple cross-compilation build x86_64 compatible image `docker build --platform linux/amd64 -t web-ap-app .`

FROM python:3-alpine

RUN apk add --update python3
RUN pip3 install bottle

EXPOSE 8000 

COPY main.py /main.py 
CMD ["python3", "/main.py"]
