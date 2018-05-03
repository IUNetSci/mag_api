#!/usr/bin/env python
import logging
import os, errno,stat,traceback, sys, re
import subprocess
from collections import OrderedDict
from datetime import datetime
from subprocess import Popen, PIPE
import configparser
from random import randint
import uuid

abspath = os.path.abspath(os.path.dirname(__file__))
middleware = os.path.dirname(abspath)
parent = os.path.dirname(middleware)
sys.path.append(parent)

from flask import Flask, abort, request, jsonify, g, url_for, render_template, escape
from flask_cors import CORS
import json
import middleware.api.util
# import asyncio

from neo4j.v1 import GraphDatabase


# initialization
app = Flask(__name__,
            static_folder="../../frontend/dist/assets",
            template_folder="../../frontend/dist")
CORS(app)
app.config['SECRET_KEY'] = 'test key'

logger = logging.getLogger(__name__)

query_id_filepaths = {
    #query_id : filename
}

driver = GraphDatabase.driver(middleware.api.util.get_msa_db_url(), auth=(middleware.api.util.get_msa_db_username(), middleware.api.util.get_msa_db_pwd()))

def get_db():
    if not hasattr(g, 'neo4j_db'):
        g.neo4j_db = driver.session()
    return g.neo4j_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'neo4j_db'):
        g.neo4j_db.close()

def run_query_get_id(query, params):
    query_id = uuid.uuid4().hex
    filename = uuid.uuid4().hex
    logger.info("query_id: " + query_id + ", filename: " + filename)

    query_id_filepaths[query_id] = filename
    # params["filename"] = filename
    q = "CALL apoc.export.csv.query('"+query+"','/shared/tuna/mag_results/"+filename+".csv', {})"

    db = get_db()
    db.run(q, params)
    return query_id


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/search', methods=['POST'])
def get_search():
    logger.info('Trying /search endpoint...')
    return_type = request.json.get('return_type')
    year = request.json.get('year')
    title = request.json.get('title')

    query = ""
    query += "MATCH (a:paper) "
    query += "WHERE a.paper_year = {year} "
    query += "AND a.normalized_title CONTAINS toLower({title}) "
    query += "RETURN ID(a) "

    query_id = run_query_get_id(query, {'year': year, "title": title})

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
