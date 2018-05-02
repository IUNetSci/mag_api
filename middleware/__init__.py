from os import path, remove
import os
import logging
import logging.config
import json


middleware = os.path.abspath(os.path.dirname(__file__))

# If applicable, delete the existing log file to generate a fresh log file during each execution
logfile_path = middleware + "/mag_api_logging.log"
if path.isfile(logfile_path):
    remove(logfile_path)

log_conf = middleware + '/logging-conf.json'
with open(log_conf, 'r') as logging_configuration_file:
    config_dict = json.load(logging_configuration_file)

logging.config.dictConfig(config_dict)

# Log that the logger was configured
logger = logging.getLogger(__name__)
logger.info('Completed configuring logger()!')
