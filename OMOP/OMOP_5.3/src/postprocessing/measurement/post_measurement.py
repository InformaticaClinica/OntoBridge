import pandas as pd
from src.postprocessing.share.utils import erase_column_unnamed, erase_quotes, change_hour

NAMEFILE1 = "MEASUREMENT-concept"
NAMEFILE2 = "MEASUREMENT-number"

CODS_EXCEPTIONS = ["3003396", #LOINC 1925-5
                    "3002032", #LOINC 1927-3
                    "3006277", #LOINC 8632-2
                    "3012501", #LOINC 11555-0
                    "3003129", #LOINC 1926-5
                    "3004959", #LOINC 28638-5
                    "3007435"  #LOINC 28639-3
                    ]

def get_dataframe(read_folder):
    # TODO: Check if neither file exists 
    data_concept = read_dataframe(read_folder, NAMEFILE1)
    data_number = read_dataframe(read_folder, NAMEFILE2)
    table_df = pd.concat([data_concept, data_number])
    return table_df

def read_dataframe(read_folder, namefile):
    try:
        data = pd.read_csv(read_folder + namefile +".csv",  dtype= {"value_as_concept_id":int})
        #data = erase_column_unnamed(data)
        #return erase_quotes(data)
        return data
    except:
        print("Does not exist the file:")
        print(namefile)
        return None

def post_measurement(read_folder):
    table_df = get_dataframe(read_folder)
    table_df = change_hour(table_df)
    if "value_as_number" in table_df.columns:
        table_df["value_as_number"] = pd.to_numeric(table_df["value_as_number"], errors = "coerce")
        condition = (table_df["value_as_number"] < 0) & (~table_df['measurement_concept_id'].isin(CODS_EXCEPTIONS)
)
        table_df.loc[condition, "value_as_number"] = None 
    if "range_high" in table_df.columns:
       condition = pd.isnull(table_df["range_high"]) & pd.notnull(table_df['value_as_number'])
       table_df.loc[condition, "range_high"] = None 

    if "range_low" in table_df.columns:
       condition = pd.isnull(table_df["range_low"]) & pd.notnull(table_df['value_as_number'])
       table_df.loc[condition, "range_low"] = None 

    if "value_as_concept_id" in table_df.columns:
        table_df["value_as_concept_id"] = table_df["value_as_concept_id"].fillna("0")
        table_df["measurement_type_concept_id"] = table_df["measurement_type_concept_id"].fillna("0")

    return table_df
