import pandas as pd
from src.postprocessing.share.utils import erase_column_unnamed, erase_quotes, change_hour

def post_drug_exposure(table_df):
    table_df = erase_column_unnamed(table_df)
    table_df = erase_quotes(table_df)
    table_df = change_hour(table_df)

    if "drug_concept_id" in table_df.columns:  
        table_df["drug_concept_id"] = table_df["drug_concept_id"].fillna("0")
    if "drug_source_concept_id" in table_df.columns:
        table_df["drug_source_concept_id"] = table_df["drug_source_concept_id"].fillna("0")
    if "days_supply" in table_df.columns:
        table_df["days_supply"] = table_df["days_supply"].fillna("1")
    if "drug_type_concept_id" in table_df.columns:
        table_df["drug_type_concept_id"]=table_df["drug_type_concept_id"].fillna("32817")

    if "drug_exposure_start_datetime" in table_df.columns:
        table_df['drug_exposure_start_date'] = pd.to_datetime(table_df['drug_exposure_start_date'])
        table_df['drug_exposure_start_datetime'] = table_df['drug_exposure_start_date'].dt.strftime('%Y-%m-%d') + ' ' + table_df['drug_exposure_start_datetime'].astype(str)

    if "drug_exposure_end_datetime" in table_df.columns:
        table_df['drug_exposure_end_date'] = pd.to_datetime(table_df['drug_exposure_end_date'])
        table_df['drug_exposure_end_datetime'] = table_df['drug_exposure_end_date'].dt.strftime('%Y-%m-%d') + ' ' + table_df['drug_exposure_end_datetime'].astype(str)

    return table_df

