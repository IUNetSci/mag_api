#!/usr/bin/env python
import os
import sys
import logging

logger = logging.getLogger(__name__)
abspath = os.path.abspath(os.path.dirname(__file__))
middleware = os.path.dirname(abspath)
sys.path.append(middleware)

from middleware.api.mag_api import app


if __name__ == '__main__':
    logger.info('Initializing MAG API !')
    logger.info('Starting MAG API !')
    app.run(host='localhost', port=5000, debug=True)
