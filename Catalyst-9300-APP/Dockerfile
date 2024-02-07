FROM python:3-alpine
RUN apk add --update python3
RUN pip3 install bottle
EXPOSE 8000 
COPY main.py /main.py 
CMD python3 /main.py

