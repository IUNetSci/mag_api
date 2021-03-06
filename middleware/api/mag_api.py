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
import csv

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

print()
print("initialized")
print(datetime.now())
print()



# initialization
app = Flask(__name__,
            static_folder="../../frontend/dist/assets",
            template_folder="../../frontend/dist")
CORS(app)
app.config['SECRET_KEY'] = 'test key'

logger = logging.getLogger(__name__)

query_id_filepaths = {
    #query_id : filename
    "fc16b50f294f407297486f189f0eb7ac":"cd1b5ce10ebb4cbba192041b8a47373b"
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
    logger.info("\nquery_id: " + query_id + ", filename: " + filename + "\n")
    print("run query - " + query_id)
    query_id_filepaths[query_id] = filename
    print(query_id_filepaths[query_id])
    # params["filename"] = filename
    q = 'CALL apoc.export.csv.query("'+query+'","/shared/tuna/mag_results/'+filename+'.csv", {})'
    print(q)
    db = get_db()
    db.run(q)
    #print(result)
    print("done")
    return query_id

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search', methods=['POST'])
def get_search():
    logger.info('Trying /search endpoint...')
    return_type = request.json.get('return_type')
    year = str(request.json.get('year'))
    title = request.json.get('title')

    print(title)
    title = title.replace("'", "\\'").replace('"', '\\"')

    query = ""
    query += "MATCH (a:paper) "
    query += "WHERE "
    query += " a.paper_year = {year} "
    query += " AND "
    query += " a.paper_title CONTAINS toLower('{title}') "
    query += "RETURN ID(a) AS paper_id"

    query = query.format(year=str(year), title=title)
    print(query)
    query_id = run_query_get_id(query, {'year': str(year), 'title': title})

    return jsonify({'query_id': query_id}), 202


@app.route('/results/<query_id>', methods=['GET'])
def get_results(query_id):
    logger.info('Trying /results/' + query_id + ' endpoint...')

    #check filesystem for query_ids[query_id].json
    filename = query_id_filepaths[query_id]
    filepath = '/shared/tuna/mag_results/'+filename+'.csv'


    # Open the CSV
    f = open( filepath, 'rU' )
    # Change each fieldname to the appropriate field name. I know, so difficult.
    reader = csv.DictReader(f)
    # Parse the CSV into JSON
    out = json.dumps( [ row for row in reader ] )
    print("Parsed JSON")
    print(out)

    return out, 202
    # Save the JSON
    # f = open( '/path/to/parsed.json', 'w')
    # f.write(out)
    # print "JSON saved!"

    # return 501

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
