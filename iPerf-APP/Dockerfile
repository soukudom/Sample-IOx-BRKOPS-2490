
FROM python:3-alpine

WORKDIR /app

COPY app.py /app/

RUN pip install --no-cache-dir bottle iperf3 \
    && apk add --no-cache iperf3

EXPOSE 8080

CMD ["python", "app.py"]
