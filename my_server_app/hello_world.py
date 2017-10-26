###############################################################################
# Caleydo - Visualization for Molecular Biology - http://caleydo.org
# Copyright (c) The Caleydo Team. All rights reserved.
# Licensed under the new BSD license, available at http://caleydo.org/license
###############################################################################

from phovea_server.ns import Namespace
from phovea_server.util import jsonify
from src import simplePythonFile

from flask import Flask
from flask.ext.pymongo import PyMongo

import os.path
import datetime
import logging

app = Namespace(__name__)
_log = logging.getLogger(__name__)

app.config['MONGO_DBNAME'] = 'snomed'
app.config['MONGO_URI'] = 'mongodb://pranavnath:pranavnath@ds157349.mlab.com:57349/snomed'



mongo = PyMongo(app)



@app.route('/', methods=['GET'])
def _hello():
  return jsonify({
    'message': 'Hello World'
  })


@app.route('/add')
def add():
  	users=mongo.db.v20160901
  	users.insert({'name' : 'pranavnath'})
  	return 'added!'

@app.route('/concepts/<name>', methods=['GET'])
def display_concepts(name):
	concept = mongo.db.s20160901

	output=[]

	for q in concept.find({'referencedComponentId' : name}):
		output.append(q)

	return jsonify(output)


@app.route('/icd9codes/<name>', methods=['GET'])
def display_icd9codes(name):
	concept = mongo.db.s20160901

	output=[]

	for q in concept.find({'icd9' : name}):
		output.append(q)

	return jsonify(output)

@app.route('/icd10codes/<name>', methods=['GET'])
def display_icd10codes(name):
	concept = mongo.db.s20160901

	output=[]

	for q in concept.find({'mapTarget' : name}):
		output.append(q)

	return jsonify(output)


@app.route('/descriptions/<term>', methods=['GET'])
def display_descriptions(term):
	concept1 = mongo.db.s20160901

 	output1=[]

	for q1 in concept1.find({'sctName': {"$regex":term, "$options":"i"}}):
		output1.append(q1)

 	return jsonify(output1)

@app.route('/icd9Names/<term>', methods=['GET'])
def display_icd9Names(term):
	concept1 = mongo.db.s20160901

 	output1=[]

	for q1 in concept1.find({'icd9_name': {"$regex":term, "$options":"i"}}):
		output1.append(q1)

 	return jsonify(output1)

@app.route('/icd10Names/<term>', methods=['GET'])
def display_icd10Names(term):
	concept1 = mongo.db.s20160901

 	output1=[]

	for q1 in concept1.find({'icdName': {"$regex":term, "$options":"i"}}):
		output1.append(q1)

 	return jsonify(output1)



@app.route('/test')
def _test():
   return jsonify({
     'message': simplePythonFile.simple_python_method()
   })

def create():
  return app
