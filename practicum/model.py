#!/usr/bin/env python
"""
 AUTHOR: Gabriel Bassett
 DATE: 01-06-2015
 DEPENDENCIES: py2neo, networkx
 Copyright 2014 Gabriel Bassett

 LICENSE:
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
'''

 DESCRIPTION:
 Implmementation of a graph-based medical decision support system.

"""
# PRE-USER SETUP
import numpy as np

########### NOT USER EDITABLE ABOVE THIS POINT #################


# USER VARIABLES
NEODB = "http://192.168.121.134:7474/db/data"

# SET RANDOM SEED 
np.random.seed(5052015)

## TRUTH DATA STATIC VARIABLES
DIAGNOSES = 10000
SIGNS = 3000
SYMPTOMS = 150
SIGNS_PER_DIAG_MEAN = 5.5
SIGNS_PER_DIAG_SD = 0.5  # Increased from 0.25 to give a bit of variance consistent with physician suggestion
SYMPTOMS_PER_DIAG_MEAN = 7 
SYMPTOMS_PER_DIAG_SD = 0.5  # Increased from 0.5 to give a variance consistent with physician suggestion
PERCENT_CONTINUOUS_SIGNS = 0.05
PERCENT_CONTINUOUS_SYMPTOMS = 0.05
PREFERENTIALLY_ATTACH_SIGNS = True
PREFERENTIALLY_ATTACH_SYMPTOMS = False


## RECORDS STATIC VARIABLES


########### NOT USER EDITABLE BELOW THIS POINT #################


## IMPORTS
from py2neo import Graph as py2neoGraph
import networkx as nx
import argparse
import logging
from flask import Flask
from flask.ext.restful import reqparse, Resource, Api, abort
from collections import defaultdict
import copy

## SETUP
__author__ = "Gabriel Bassett"
# Parse Arguments (should correspond to user variables)
parser = argparse.ArgumentParser(description='This script processes a graph.')
parser.add_argument('-d', '--debug',
                    help='Print lots of debugging statements',
                    action="store_const", dest="loglevel", const=logging.DEBUG,
                    default=logging.WARNING
                   )
parser.add_argument('-v', '--verbose',
                    help='Be verbose',
                    action="store_const", dest="loglevel", const=logging.INFO
                   )
parser.add_argument('--log', help='Location of log file', default=None)
# <add arguments here>
parser.add_argument('db', help='URL of the neo4j graph database', default=NEODB)
#args = parser.parse_args()
## Set up Logging
#if args.log is not None:
#    logging.basicConfig(filename=args.log, level=args.loglevel)
#else:
#    logging.basicConfig(level=args.loglevel)
# <add other setup here>
# Connect to database
G = neo4j.GraphDatabaseService(NEODB)
g = nx.DiGraph()
NEODB = args.db


## EXECUTION
class decision_support_system():
    model = None  # in the form of a graph

#    def new_model(self):
#        """
#        :return: Nothing
#
#        Takes nothing, returns an empty model for training.
#        """
#        pass

    def load_model(self, model = NEODB):
        """

        :param model: Neo4j database URI as string
        :return: booling success

        Takes a string refering to to a neo4j database and save the database handle to the class
        """
        try:
            self.model = py2neoGraph(model)
            logging.info("Model Loaded.")
            return True
        except exception as e:
            logging.error(e.__str__)
            logging.info("Model failed to load.")
            return False


    def sign_symptom_training(self, sign_symptom_map):
        """

        :param sign_symptom_map: dictionary of keys of diagnosis and list of tuples of (signs/symptoms, confidence, value)  (value is only used for continuous variables)
        :return: booling success

        Takes a single mapping of a sign/symptom to a diagnosis adds it to the Model
        """
        pass  # TODO
        #  TODO : For continuous variables, the total for that variable (regardless of relation to the diagnosis), may need to be kept to normalize Y axis.

        # TODO: (Need a way to categorize signs/symptoms as continuous, factors, or bool)

        # TODO: if needed, create the sign/symptom & label it's type (sign or symptom), it's class (factor, continuous, or bool)

        # TODO: If needed, create a diagnosis

        # TODO: if it doesn't exist, create an edge between the sign/symptom and the diagnosis.  Create initial confidence (factor table, function, or bool)
        # TODO:  If you cannot incrimentally update, the model will need to keep the entire value set and at the end build a distribution for each of the continuous variables

        # TODO: if it already exists update the confidence (factor table, function, or bool count)

        # NOTE: sign/symptom - diagnosis relationships may be negative in confidence indicating a lacking.  However negative and positive relationships should have their own edges.


    def test_symptom_training(self, test_symptom_map):
        """

        :param test_symptom_map: dictionary of keys of tests and list of tuples of (symptoms, confidence)
        :return: booling success

        Takes a single mapping of a sign/symptom to a diagnosis adds it to the Model
        """
        pass  # TODO


    def diagnosis_treatment_training(self, diagnosis_treatment_map):
        """

        :param diagnosis_treatment_map: dictionary of keys of treatment and values of (diagnosis, impact)
        :return: booling success

        Takes a single mapping of a treatment to diganosis and adds it to the Model
        """
        pass  # TODO


    def query(self, signs_symptoms):
        """

        : param signs_symptoms: A list of signs and/or symptoms
        : return: a dictionary of form {diagnoses: {diagnosis: score}, tests:{test: score}, treatments:{treatment:score}}
        """

        d = {}
        d['diagnosis'] = query_diagnosis(signs_symptoms)
        d['test'] = query_test(d['diagnosis'])
        d['treatements'] = query_treatments(d['diagnosis'])

        return d


    def query_diagnosis(self, signs_symptoms):
        """

        : param signs_symptoms: A list of signs and/or symptoms
        : return: a dictionary of form {diagnosis: score}
        """
        pass  # TODO
        # TODO: Get all signs & symptoms from graph

        # TODO: Get all out edges associated with each sign/symptom

        # TOOD: If necessary, calculate distribution

        # TODO: Normalize to out degree (bool) or feature/distribution (categorical/conditnuous) # May be done during import, but only 

        # TODO: Find the single value of categorical/continuous signs/symptoms as confidence

        # TOOD: sum the confidence by destination of each edge

        # TODO: find all edges into the diagnosis.  Reduce the confidence summation of each diagnosis by the sum of the confidences of it's missing edges.

        # TODO: Return the diagnosis:score dictionary

    def query_test(self, diagnoses):
        """

        : param diagnoses: a dictionary of diagnoses and scores associated with their likelihood
        : return: a dictionary of form {test: score}
        """
        pass  # TODO


    def query_treatments(self, diagnoses):
        """

        : param diagnoses: a dictionary of diagnoses and scores associated with their likelihood
        : return: a dictionary of form {treatment:score}
        """
        pass  # TODO


    def validate_model(sign_symptoms, actual):
        """

        : param sign_symptoms: a list of lists of signs/symptoms
        : param actual: a list of actual diagnosis
        : return: a list of bools representing whether the actual diagnosis was in the top 5 diagnoses
        """
        pass  # TODO

        diagnosis = self.query_diagnosis(signs_symptoms)

        # TODO: Sort the diagnosis by score

        # TODO: If the diagnosis is the top diagnosis, incriment the top1 counter
        
        # TODO: if the diagnosis is in the top 5, increment the top5 counter
        
        # TODO: Increment the total counter

        # TODO: Return the 1% and 5% precisions.  (Could we also calculate recall?)


def main():
    logging.info('Beginning main loop.')

    # Initialize the arguements
    api_parser = reqparse.RequestParser()
    #api_parser.add_argument('ASN1', type=str, help="First ASN of query. (Order doesn't matter.)", default=None)
    #api_parser.add_argument('ASN2', type=str, help="Second ASN of query.  (Order doesn't matter.)", default=None)
    #api_parser.add_argument('verizon', type=bool, help="Report on verizon existance in ASN's paths.", default=False)
    #api_parser.add_argument('source', type=str, help="An ASN representing the source of the traffic", default=False)
    #api_parser.add_argument('destination', type=str, help="An IP address or subnet destination." , default=False)

    app = Flask(__name__)
    api = Api(app)
    api.add_resource(ASNSearch, '/')
    app.run(debug=True)
    logging.info('Ending main loop.')

if __name__ == "__main__":
    main()    
