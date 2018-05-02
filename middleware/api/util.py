import logging
import os, errno,stat,traceback, sys, re
import configparser

abspath = os.path.abspath(os.path.dirname(__file__))
middleware = os.path.dirname(abspath)
parent = os.path.dirname(middleware)
sys.path.append(parent)

logger = logging.getLogger(__name__)


def get_etw_config():
    # if mag.config cannot found, throw error
    try:
        config_path = parent + '/conf/mag.config'
        if os.path.isfile(config_path):
            logger.info('mag.config path : %s', config_path)
            config = configparser.RawConfigParser()
            config.read(config_path)
            return config
        else:
            logger.error('Unable to find mag.config file. Make sure you have mag.config inside conf directory !')
            raise Exception('Unable to find mag.config file. Make sure you have mag.config inside conf directory !')
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        raise Exception('Unable to find mag.config file. Make sure you have mag.config inside conf directory !')


def get_etw_db_url():
    try:
        config = get_etw_config()
        db_host_name = config['DATABASE_INFO']['database-url']
        return db_host_name
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        logger.error('Unable to find mag.config file. Make sure you have mag.config inside conf directory !')
        raise Exception('Unable to find mag.config file !')


def get_etw_db_name():
    try:
        config = get_etw_config()
        db_name = config['DATABASE_INFO']['database-name']
        return db_name
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        logger.error('Unable to find mag.config file. Make sure you have mag.config inside conf directory !')
        raise Exception('Unable to find mag.config file !')


def get_etw_db_username():
    try:
        config = get_etw_config()
        db_username = config['DATABASE_INFO']['database-username']
        return db_username
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        logger.error('Unable to find mag.config file. Make sure you have mag.config inside conf directory !')
        raise Exception('Unable to find mag.config file !')


def get_etw_db_pwd():
    try:
        config = get_etw_config()
        db_pwd = config['DATABASE_INFO']['database-password']
        return db_pwd
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        logger.error('Unable to find mag.config file. Make sure you have mag.config inside conf directory !')
        raise Exception('Unable to find mag.config file !')