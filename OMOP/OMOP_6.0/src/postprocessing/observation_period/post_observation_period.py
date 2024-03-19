from src.postprocessing.share.utils import erase_column_unnamed, erase_quotes

def post_observation_period(table_df):
    table_df = erase_column_unnamed(table_df)
    table_df = erase_quotes(table_df)
    table_df = table_df.groupby("person_id").agg(
        visit_start_date=("visit_start_date", "min"),
        visit_end_date=("visit_end_date", "max"),
    ).reset_index()
    return table_df
