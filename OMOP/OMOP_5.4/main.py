import time
inicio = time.time()

# IMPORTS 
import rdflib
from rdflib import URIRef
import pandas as pd
import datetime
import csv

# Support functions
from src.preprocessing.send_query import get_query
from src.postprocessing.post_omop import post_omop

ALL = True
OPERATION = 2 # 2 = ALL, 1 = POST-PROCESSING, 0 = PRE-PROCESSING
READ_FOLDER = "output/Pre-processing/"
WRITE_FOLDER = "output/Post-processing/"

def query_to_csv(OMOP_therms):
    if OPERATION == 2 or OPERATION == 0:
        get_query(OMOP_therms, READ_FOLDER, ALL, inicio)
        print("== Dataframe created ==" )
        print(time.time()-inicio)

    if OPERATION == 2 or OPERATION == 1:
        post_omop(OMOP_therms, READ_FOLDER, WRITE_FOLDER, ALL)
        print("== Write Data ==")
        print(time.time()-inicio)

query_to_csv("MEASUREMENT")
