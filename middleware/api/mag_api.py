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
import middleware.api.util

from neo4j.v1 import GraphDatabase

def run_query(query):
    query_id = 12
    return query_id

# initialization
app = Flask(__name__,
            static_folder="../../frontend/dist/assets",
            template_folder="../../frontend/dist")
CORS(app)
app.config['SECRET_KEY'] = 'test key'

logger = logging.getLogger(__name__)


def check_paper(tx):
    tx.run("CALL apoc.export.csv.query('MATCH (a:paper) WHERE a.paper_title CONTAINS toLower(\"A statistical study of heterogeneous nucleation of ice by molecular dynamics\") RETURN ID(a)','/shared/tuna/mag_results/test1.csv', {})")


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/search', methods=['POST'])
def get_search():
    logger.info('Trying /search endpoint...')
    return_type = request.json.get('return_type')
    years = request.json.get('years')
    title = request.json.get('title')

    query_id = run_query("some query")
    driver = GraphDatabase.driver(middleware.api.util.get_msa_db_url(), auth=(middleware.api.util.get_msa_db_username(), middleware.api.util.get_msa_db_pwd()))

    with driver.session() as session:
        query1 = session.write_transaction(check_paper)
        print(query1)
        return 200

    return 501
    return jsonify({'query_id': query_id}), 202

@app.route('/results/<query_id>', methods=['GET'])
def get_results(query_id):
    logger.info('Trying /results/' + query_id + ' endpoint...')

    #check filesystem for query_ids[query_id].json

    return 501

@app.route('/references/<paper_id>', methods=['GET'])
def get_references(paper_id):
    logger.info('Trying /references/' + paper_id + ' endpoint...')

    query_id = run_query("some query")
    return jsonify({'query_id': query_id}), 202

@app.route('/citations/<paper_id>', methods=['GET'])
def get_citations(paper_id):
    logger.info('Trying /citations/' + paper_id + ' endpoint...')

    query_id = run_query("some query")
    return jsonify({'query_id': query_id}), 202

@app.route('/paper/<paper_id>', methods=['GET'])
def get_paper(paper_id):
    logger.info('Trying /paper/' + paper_id + ' endpoint...')

    query_id = run_query("some query")
    return jsonify({'query_id': query_id}), 202

@app.route('/papers', methods=['POST'])
def get_multiple_papers():
    logger.info('Trying /papers endpoint...')
    papers_array = request.json.get('paper_ids')

    query_id = run_query("some query")
    return jsonify({'query_id': query_id}), 202
