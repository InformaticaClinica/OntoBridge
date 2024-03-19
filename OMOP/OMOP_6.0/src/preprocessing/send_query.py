import csv
from SPARQLWrapper import SPARQLWrapper

from src.preprocessing.config import get_endpoint
from src.preprocessing.condition_occurrence.query import query_condition_occurrence
from src.preprocessing.device_exposure.query import query_device_exposure
from src.preprocessing.drug_exposure.query import query_drug_exposure
from src.preprocessing.measurement.query_concept import query_measurement_concept
from src.preprocessing.measurement.query_number import query_measurement_number
from src.preprocessing.observation.query_concept import query_observation_concept
from src.preprocessing.observation.query_string import query_observation_string
from src.preprocessing.observation.query_datetime import query_observation_datetime
from src.preprocessing.observation.query_number import query_observation_number
from src.preprocessing.person.query import query_person
from src.preprocessing.procedure_occurrence.query import query_procedure_occurrence
from src.preprocessing.visit_occurrence.query import query_visit_occurrence
from src.preprocessing.visit_detail.query import query_visit_detail

def send_query(query_options, namefile):
    sparql = SPARQLWrapper(get_endpoint())
    sparql.setQuery(query_options)
    sparql.setReturnFormat("csv")
    
    response = sparql.query().response
    if response:
        with open(namefile, "w", encoding='utf-8') as file:
            file.write(response.read().decode('utf-8'))

def get_query(OMOP_therm, read_folder, all, inicio = None):
    if OMOP_therm == "CONDITION_OCCURRENCE"  or all:
        namefile = read_folder + "CONDITION_OCCURRENCE" + ".csv"
        query_options = query_condition_occurrence() 
        send_query(query_options, namefile)

    if OMOP_therm == "DEVICE_EXPOSURE"  or all:
        namefile = read_folder + "DEVICE_EXPOSURE" + ".csv"
        query_options = query_device_exposure()     
        send_query(query_options, namefile)

    if OMOP_therm == "DRUG_EXPOSURE"  or all:
        namefile = read_folder + "DRUG_EXPOSURE" + ".csv"
        query_options = query_drug_exposure()     
        send_query(query_options, namefile)

    if OMOP_therm == "MEASUREMENT"  or all: 
        namefile = read_folder + "MEASUREMENT" + "-concept.csv"
        query_options = query_measurement_concept()     
        send_query(query_options, namefile)
        namefile = read_folder + "MEASUREMENT" + "-number.csv"
        query_options = query_measurement_number()     
        send_query(query_options, namefile)

    if OMOP_therm == "OBSERVATION"  or all: 
        query_options = query_observation_concept()
        namefile = read_folder + "OBSERVATION" + "-concept.csv"
        send_query(query_options, namefile)
        query_options = query_observation_string()
        namefile = read_folder + "OBSERVATION" + "-string.csv"
        send_query(query_options, namefile)
        query_options = query_observation_datetime()
        namefile = read_folder + "OBSERVATION" + "-datetime.csv"
        send_query(query_options, namefile)
        query_options = query_observation_number()
        namefile = read_folder + "OBSERVATION" + "-number.csv"
        send_query(query_options, namefile)

    if OMOP_therm == "PERSON"  or all: 
        namefile = read_folder + "PERSON" + ".csv"
        query_options = query_person()     
        send_query(query_options, namefile)

    if OMOP_therm == "PROCEDURE_OCCURRENCE"  or all: 
        namefile = read_folder + "PROCEDURE_OCCURRENCE" + ".csv"
        query_options = query_procedure_occurrence()
        send_query(query_options, namefile)
    
    if OMOP_therm == "VISIT_OCCURRENCE"  or all: 
        namefile = read_folder + "VISIT_OCCURRENCE" + ".csv"
        query_options = query_visit_occurrence()
        send_query(query_options, namefile)

    if OMOP_therm == "VISIT_DETAIL"  or all: 
        namefile = read_folder + "VISIT_DETAIL" + ".csv"
        query_options = query_visit_detail()
        send_query(query_options, namefile)

    if OMOP_therm == "OBSERVATION_PERIOD":
        print("Observation_period does not have queries")
        return None

