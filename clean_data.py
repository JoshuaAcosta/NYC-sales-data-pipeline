"""
Cleans and dedupes data.
"""
import numpy as np
import pandas as pd

def clean_column_names(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    
    
def clean_neighborhood_names(df):
    df["neighborhood"] = df["neighborhood"].apply(str.rstrip)
    
    
def dedupe_rows(df):
    df.drop_duplicates()


def update_dtypes(df):
    update_cols_dtype = {"sale_price":"float64", "sale_date":"datetime64[ns]",\
                        "land_square_feet":"int64", "gross_square_feet":"int64",\
                         "zip_code": "int16","residential_units": "int16",\
                         "commercial_units": "int16", "total_units" : "int16", "year_built":"int16"}
    
    df = df.astype(update_cols_dtype)
    return df

def clean_neighborhood_values(df):
    df["neighborhood"].replace('1026','MIDTOWN EAST', inplace=True)
    df["neighborhood"].replace('3019','CROWN HEIGHTS', inplace=True)
    df["neighborhood"].replace('3004','BATH BEACH', inplace=True)
    df["neighborhood"].replace('1021','LITTLE ITALY', inplace=True)
    

def clean_year_built(df):
    df.loc[df.address == "762 MARCY AVENUE, 1B", 'year_built'] = 2018
    df.loc[df.address == "762 MARCY AVENUE, 4", 'year_built'] = 2018
    df.loc[df.address == "9 BARTLETT AVENUE, 0", 'year_built'] = 2018
    
def clean_zip_code(df):
    df.loc[df.address == "762 MARCY AVENUE, 1B", 'zip_code'] = 11216
    df.loc[df.address == "762 MARCY AVENUE, 4", 'zip_code'] = 11216

def fill_na(df):
    df.update(df[["residential_units","commercial_units", "total_units", "land_square_feet", "gross_square_feet"]].fillna(0.0))

def update_borough_values(df):
    
    df["borough"].replace({1 : "Manhattan", 2 : "Bronx", 3 : "Brooklyn", 4 : "Queens", 5 : "Staten Island"},inplace=True)

def clean_data_to_csv(df):
    
    df.to_csv("data/Clean_NYC_sales_data.csv")
    
if __name__ == "__main__":
    df = pd.read_csv("data/NYC_sales_data.csv", index_col=0)
    clean_column_names(df)
    clean_neighborhood_names(df)
    dedupe_rows(df)
    clean_neighborhood_values(df)
    clean_year_built(df)
    clean_zip_code(df)
    fill_na(df)
    update_borough_values(df)
    df = update_dtypes(df)
    clean_data_to_csv(df)
