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

@app.route('/search')
def get_search():
    return 501

@app.route('/results/<query_id>')
def get_results(query_id):
    return 501

@app.route('/references/<paper_id>')
def get_references(paper_id):
    return 501

@app.route('/citations/<paper_id>')
def get_citations(paper_id):
    return 501

@app.route('/paper/<paper_id>')
def get_paper(paper_id):
    return 501

@app.route('/papers')
def get_multiple_papers():
    return 501
