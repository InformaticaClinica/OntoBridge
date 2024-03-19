from src.postprocessing.share.utils import change_hour

def post_death(table_df):

    change_hour(table_df)
    
    return table_df
