from src.postprocessing.share.utils import erase_column_unnamed, erase_quotes
def post_drug_exposure(table_df):
    table_df = erase_column_unnamed(table_df)
    table_df = erase_quotes(table_df)
    if "drug_concept_id" in table_df.columns:  
        table_df["drug_concept_id"] = table_df["drug_concept_id"].fillna("0")
    if "drug_source_concept_id" in table_df.columns:
        table_df["drug_source_concept_id"] = table_df["drug_source_concept_id"].fillna("0")
    if "days_supply" in table_df.columns:
        table_df["days_supply"] = table_df["days_supply"].fillna(1)
    if "drug_type_concept_id" in table_df.columns:
        table_df["drug_type_concept_id"]=table_df["drug_type_concept_id"].fillna(32817)
    return table_df

