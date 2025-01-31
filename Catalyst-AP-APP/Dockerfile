# build this image on arm based architecuture 
# if using x86_64-based environment, use simple cross-compilation build arm compatible image `docker build --platform linux/arm64 -t web-ap-app .`

FROM arm64v8/alpine:latest

RUN apk --no-cache add python3 py3-bottle

EXPOSE 8000 

COPY main.py /main.py 
CMD ["python3", "/main.py"]

