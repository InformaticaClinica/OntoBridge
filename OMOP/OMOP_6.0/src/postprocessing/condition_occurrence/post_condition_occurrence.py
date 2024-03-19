from src.postprocessing.share.utils import erase_column_unnamed, erase_quotes
def post_condition_occurrence(table_df):
    table_df = erase_column_unnamed(table_df)
    table_df = erase_quotes(table_df)
    if "condition_status_concept_id" in table_df.columns:
        table_df["condition_status_concept_id"] = table_df["condition_status_concept_id"].fillna("0")
    if "condition_source_concept_id" in table_df.columns:
        table_df["condition_source_concept_id"] = table_df["condition_source_concept_id"].fillna("0")
    return table_df

