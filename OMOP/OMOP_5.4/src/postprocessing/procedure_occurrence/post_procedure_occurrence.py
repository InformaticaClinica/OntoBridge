from src.postprocessing.share.utils import erase_column_unnamed, erase_quotes, change_hour

def post_procedure_occurrence(table_df):
    table_df = erase_column_unnamed(table_df)
    table_df = erase_quotes(table_df)
    table_df = change_hour(table_df)
    if "modifier_concept_id" in table_df.columns:
        table_df["modifier_concept_id"] = table_df["modifier_concept_id"].fillna("0")
    if "procedure_source_concept_id" in table_df.columns:
        table_df["procedure_source_concept_id"] = table_df["procedure_source_concept_id"].fillna("0")
    if "procedure_type_concept_id" in table_df.columns:
        table_df["procedure_type_concept_id"]=table_df["procedure_type_concept_id"].fillna("32817")
    return table_df
