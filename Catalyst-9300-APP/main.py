#!/usr/bin/python
import os
import sys
import logging
from bottle import route, run, request

### Option1 LOGGING: Set up logging to file only ####
caf_log_dir = os.environ.get('CAF_APP_LOG_DIR')
log_file = 'server.log'
if caf_log_dir:
    log_file = os.path.join(caf_log_dir, log_file)

logging.basicConfig(
    level=logging.INFO,
    format='%(message)s',
    handlers=[
        logging.FileHandler(log_file, mode='a')
    ]
)

logging.info(f"Setting up logging to file {log_file}")

@route("/")
def hello():
    client_ip = request.environ.get('HTTP_X_FORWARDED_FOR') or request.environ.get('REMOTE_ADDR')
    logging.info(f"Request from {client_ip}")
    
    ### Option2 SYSLOG: Write to syslog via serial port ###
    syslog_test = f"Request from {client_ip}\n"
    try:
        fd = os.open("/dev/ttyS2", os.O_WRONLY | os.O_NONBLOCK)
        os.write(fd, syslog_test.encode())
        os.close(fd)
        logging.info("Syslog message sent successfully")
    except Exception as e:
        logging.error(f"Failed to write to syslog: {e}")
    
    logging.info("Response sent..")

    return "<b>Hello Cisco Live!</b>!"

logging.info("Server running at http://0.0.0.0:8000/")

run(host='0.0.0.0', port=8000, quiet=True)
