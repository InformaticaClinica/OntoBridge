def erase_column_unnamed(table_df):
    #num_cols = str(len(table_df.columns) - 1)
    #table_df = table_df.drop(columns=['Unnamed: ' + num_cols])
    return table_df

def erase_quotes(table_df):
    #table_df.columns = table_df.columns.str.strip(' "')
    #table_df = table_df.map(lambda x: x.strip(' "'))
    return table_df

