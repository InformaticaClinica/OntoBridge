def post_person(table_df):
    if "race_concept_id" in table_df.columns:
        table_df["race_concept_id"] = table_df["race_concept_id"].fillna("0")
    
    if "gender_source_concept_id" in table_df.columns:
        table_df["gender_source_concept_id"] = table_df["gender_source_concept_id"].fillna("0")

    if "race_source_concept_id" in table_df.columns:
        table_df["race_source_concept_id"] = table_df["race_source_concept_id"].fillna("0")

    if "ethnicity_source_concept_id" in table_df.columns:
        table_df["ethnicity_source_concept_id"] = table_df["ethnicity_source_concept_id"].fillna("0")

    if "year_of_birth" in table_df.columns:
         table_df["year_of_birth"] = table_df["year_of_birth"].str.split("-").str[0]

    if "month_of_birth" in table_df.columns:
        table_df["month_of_birth"] = table_df["month_of_birth"].apply(lambda x: x.split('-')[1] if isinstance(x, str) and len(x.split('-')) > 1 else x)

    if "day_of_birth" in table_df.columns:
        table_df["day_of_birth"] = table_df["day_of_birth"].apply(lambda x: x.split('-')[2] if isinstance(x, str) and len(x.split('-')) > 2 else x)
    
    return table_df
