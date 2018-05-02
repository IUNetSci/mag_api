#!/usr/bin/env python
import logging
import os, errno,stat,traceback, sys, re
import subprocess
from collections import OrderedDict
from datetime import datetime
from subprocess import Popen, PIPE
import configparser
from random import randint

abspath = os.path.abspath(os.path.dirname(__file__))
middleware = os.path.dirname(abspath)
parent = os.path.dirname(middleware)
sys.path.append(parent)

from flask import Flask, abort, request, jsonify, g, url_for, render_template, escape
from flask_cors import CORS
import json

# initialization
app = Flask(__name__,
            static_folder="../../frontend/dist/assets",
            template_folder="../../frontend/dist")
CORS(app)
app.config['SECRET_KEY'] = 'test key'

logger = logging.getLogger(__name__)

@app.route('/')
def index():
    return render_template("index.html")
