# build this image on x86_64 based architecuture 
FROM python:3-alpine

RUN apk add --update python3
RUN pip3 install bottle
ENV TZ=Europe/Zurich

EXPOSE 8000 

COPY main.py /main.py 
CMD ["python3", "/main.py"]
