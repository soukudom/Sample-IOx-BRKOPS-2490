# Copyright (c) 2026 Cisco and/or its affiliates.

# This software is licensed to you under the terms of the Cisco Sample
# Code License, Version 1.0 (the "License"). You may obtain a copy of the
# License at

#                https://developer.cisco.com/docs/licenses

# All use of the material herein must be in accordance with the terms of
# the License. All rights not expressly granted by the License are
# reserved. Unless required by applicable law or agreed to separately in
# writing, software distributed under the License is distributed on an "AS
# IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied.

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
