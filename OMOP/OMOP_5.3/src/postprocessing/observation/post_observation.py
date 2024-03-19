import pandas as pd 

from src.postprocessing.share.utils import erase_column_unnamed, erase_quotes, change_hour

NAMEFILE1 = "OBSERVATION-concept"
NAMEFILE2 = "OBSERVATION-number"
NAMEFILE3 = "OBSERVATION-string"
NAMEFILE4 = "OBSERVATION-datetime"

def get_dataframe(read_folder):
    # TODO: Check if neither file exists 
    data_concept = read_dataframe(read_folder, NAMEFILE1)
    print(data_concept)
    data_number = read_dataframe(read_folder, NAMEFILE2)
    print(data_number)
    table_df = pd.concat([data_concept, data_number])

    # data_string = read_dataframe(read_folder, NAMEFILE3)
    # if data_string != None:
    #     table_df = pd.concat([table_df, data_string])

    # data_datetime = read_dataframe(read_folder, NAMEFILE4)
    # if data_datetime != None:
    #     table_df = pd.concat([table_df, data_datetime])

    return table_df

def read_dataframe(read_folder, namefile):
    print(read_folder + namefile +".csv")
    try:
        data = pd.read_csv(read_folder + namefile +".csv", dtype = {'value_as_concept_id':int}) 
        ##data = erase_column_unnamed(data)
        # return erase_quotes(data)
        return data
    except Exception as e:
        print(e)
        print("Does not exist the file:")
        print(namefile)
        return None
    
def post_observation(read_folder):
    table_df = get_dataframe(read_folder)
    table_df = change_hour(table_df)
    print(table_df.head())
    if "observation_source_concept_id" in table_df.columns:
        table_df["observation_source_concept_id"] = table_df["observation_source_concept_id"].fillna("0")
    if "observation_type_concept_id" in table_df.columns:
        table_df["observation_type_concept_id"]=table_df["observation_type_concept_id"].fillna("32817")
    return table_df
