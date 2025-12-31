#!/usr/bin/python
import os
import sys
import logging
from bottle import route, run, request

# Set up logging to file and stdout
# If running in CAF environment, use the CAF_APP_LOG_DIR location to write the log file
caf_log_dir = os.environ.get('CAF_APP_LOG_DIR')
log_file = 'server.log'
if caf_log_dir:
    log_file = os.path.join(caf_log_dir, log_file)

# Configure logging to write to both file and stdout
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s',
    handlers=[
        logging.FileHandler(log_file, mode='a'),
        logging.StreamHandler(sys.stdout)
    ]
)

logging.info(f"Setting up logging to file {log_file}")

@route("/")
def hello():
    # Get client IP address (check for x-forwarded-for header first)
    client_ip = request.environ.get('HTTP_X_FORWARDED_FOR') or request.environ.get('REMOTE_ADDR')
    logging.info(f"Request from {client_ip}")
    logging.info("Response sent..")
    return "<b>Hello Cisco Live!</b>!"

# Put a friendly message on the terminal
logging.info("Server running at http://0.0.0.0:8000/")

run(host='0.0.0.0', port=8000, quiet=True)
