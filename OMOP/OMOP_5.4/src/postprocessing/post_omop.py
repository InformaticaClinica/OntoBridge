import pandas as pd
from src.postprocessing.drug_exposure.post_drug_exposure import post_drug_exposure
from src.postprocessing.person.post_person import post_person 
from src.postprocessing.death.post_death import post_death
from src.postprocessing.observation.post_observation import post_observation 
from src.postprocessing.measurement.post_measurement import post_measurement
from src.postprocessing.condition_occurrence.post_condition_occurrence import post_condition_occurrence
from src.postprocessing.visit_occurrence.post_visit_occurrence import post_visit_occurrence
from src.postprocessing.procedure_occurrence.post_procedure_occurrence import post_procedure_occurrence
from src.postprocessing.visit_detail.post_visit_detail import post_visit_detail
from src.postprocessing.device_exposure.post_device_exposure import post_device_exposure
from src.postprocessing.observation_period.post_observation_period import post_observation_period

def post_omop(OMOP_therm, read_folder, write_folder, all):
    if OMOP_therm == "PERSON" or all:
        print("here")
        container_df = pd.read_csv(read_folder +"PERSON.csv") 
        container_df = post_person(container_df) 
        container_df.to_csv(path_or_buf = write_folder + "PERSON.csv", index=False) 

    if OMOP_therm == "OBSERVATION" or all:
        container_df = post_observation(read_folder)
        container_df.to_csv(path_or_buf = write_folder + "OBSERVATION.csv", index=False) 

    if OMOP_therm == "MEASUREMENT" or all:
        container_df = post_measurement(read_folder)
        container_df.to_csv(path_or_buf = write_folder + "MEASUREMENT.csv", index=False) 

    if OMOP_therm == "CONDITION_OCCURRENCE" or all:
        container_df = pd.read_csv(read_folder + "CONDITION_OCCURRENCE.csv") 
        container_df = post_condition_occurrence(container_df)
        container_df.to_csv(path_or_buf = write_folder + "CONDITION_OCCURRENCE.csv", index=False) 

    if OMOP_therm == "VISIT_OCCURRENCE" or all:
        container_df = pd.read_csv(read_folder + "VISIT_OCCURRENCE.csv") 
        container_df = post_visit_occurrence(container_df)
        container_df.to_csv(path_or_buf = write_folder + "VISIT_OCCURRENCE.csv", index=False) 

    if OMOP_therm == "VISIT_DETAIL" or all:
        container_df = pd.read_csv(read_folder + "VISIT_DETAIL.csv") 
        container_df = post_visit_detail(container_df)
        container_df.to_csv(path_or_buf = write_folder + "VISIT_DETAIL.csv", index=False) 

    if OMOP_therm == "PROCEDURE_OCCURRENCE" or all:
        container_df = pd.read_csv(read_folder + "PROCEDURE_OCCURRENCE.csv") 
        container_df = post_procedure_occurrence(container_df)
        container_df.to_csv(path_or_buf = write_folder + "PROCEDURE_OCCURRENCE.csv", index=False) 

    if OMOP_therm == "DEVICE_EXPOSURE" or all:
        container_df = pd.read_csv(read_folder + "DEVICE_EXPOSURE.csv") 
        container_df = post_device_exposure(container_df) 
        container_df.to_csv(path_or_buf = write_folder + "DEVICE_EXPOSURE.csv", index=False) 

    if OMOP_therm == "DRUG_EXPOSURE" or all:
        container_df = pd.read_csv(read_folder + "DRUG_EXPOSURE.csv") 
        container_df = post_drug_exposure(container_df) 
        container_df.to_csv(path_or_buf = write_folder + "DRUG_EXPOSURE.csv", index=False) 

    if OMOP_therm == "OBSERVATION_PERIOD" or all:
        container_df = pd.read_csv(read_folder + "VISIT_OCCURRENCE.csv") 
        container_df = post_observation_period(container_df) 
        container_df.to_csv(path_or_buf = write_folder + "OBSERVATION_PERIOD.csv", index=False) 

    if OMOP_therm == "DEATH" or all:
        container_df = pd.read_csv(read_folder + "DEATH.csv") 
        container_df = post_death(container_df) 
        container_df.to_csv(path_or_buf = write_folder + "DEATH.csv", index=False) 



