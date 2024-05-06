import csv
from SPARQLWrapper import SPARQLWrapper
import logging

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

# 5.4
from src.preprocessing.death.query import query_death

def send_query(query_options, namefile):
    """Send SPARQL query and save response to a CSV file."""
    logging.info(f"Sending query and writing results to {namefile}")
    sparql = SPARQLWrapper(get_endpoint())
    sparql.setQuery(query_options)
    sparql.setReturnFormat("csv")
    
    response = sparql.query().response
    if response:
        with open(namefile, "w", encoding='utf-8') as file:
            file.write(response.read().decode('utf-8'))

def get_query(read_folder):
    """Run all SPARQL queries for the OMOP clinical CDM model."""
    logging.info("Starting to run SPARQL queries for all data tables.")

    # Condition occurrence
    query_options = query_condition_occurrence() 
    send_query(query_options, read_folder + "CONDITION_OCCURRENCE.csv")

    # Device exposure
    query_options = query_device_exposure()     
    send_query(query_options, read_folder + "DEVICE_EXPOSURE.csv")

    # Drug exposure
    query_options = query_drug_exposure()     
    send_query(query_options, read_folder + "DRUG_EXPOSURE.csv")

    # Measurement
    query_options = query_measurement_concept()     
    send_query(query_options, read_folder + "MEASUREMENT-concept.csv")
    query_options = query_measurement_number()     
    send_query(query_options, read_folder + "MEASUREMENT-number.csv")

    # Observation
    query_options = query_observation_concept()
    send_query(query_options, read_folder + "OBSERVATION-concept.csv")
    query_options = query_observation_string()
    send_query(query_options, read_folder + "OBSERVATION-string.csv")
    query_options = query_observation_datetime()
    send_query(query_options, read_folder + "OBSERVATION-datetime.csv")
    query_options = query_observation_number()
    send_query(query_options, read_folder + "OBSERVATION-number.csv")

    # Person
    query_options = query_person()     
    send_query(query_options, read_folder + "PERSON.csv")

    # Procedure Occurrence
    query_options = query_procedure_occurrence()
    send_query(query_options, read_folder + "PROCEDURE_OCCURRENCE.csv")

    # Visit Occurrence
    query_options = query_visit_occurrence()
    send_query(query_options, read_folder + "VISIT_OCCURRENCE" + ".csv")

    # Visit detail
    query_options = query_visit_detail()
    send_query(query_options, read_folder + "VISIT_DETAIL" + ".csv")

    # Death
    query_options = query_death()     
    send_query(query_options, read_folder + "DEATH" + ".csv")

    logging.info("All queries have been executed and data written.")

