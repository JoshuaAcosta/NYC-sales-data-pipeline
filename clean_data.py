"""
Cleans and dedupes data.
"""
<<<<<<< HEAD
import numpy as np
import pandas as pd

from combine_spreadsheets import combined_df
=======
>>>>>>> 36bae1701b2061d3b2b58e106e1e2bad619773f7

def clean_column_names(df):
    """Changes pandas column names to be more pythonic """
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')\
                                .str.replace('(', '').str.replace(')', '')
    return df

def clean_neighborhood_names(df):
    """Removes whitespace in neighborhood names """
    df["neighborhood"] = df["neighborhood"].apply(str.rstrip)
    return df

def dedupe_rows(df):
    """Dedupes similar rows """
    df.drop_duplicates()
    return df

<<<<<<< HEAD
def clean_dtypes(df):
    """
    Replaces empty excel cells with nulls, updates dtypes for columns.
    """
    df.replace(r'^\s+$', np.nan, regex=True)

    update_cols_dtype = {"borough": "category", "sale_price":"float64",\
                        "sale_date":"datetime64[ns]",\
                        "zip_code":"int16", "residential_units":"int16",\
                        "commercial_units":"int16", "total_units":"int16",\
                        "land_square_feet":"int64", "gross_square_feet":"int64"}

    combined_df = combined_df.astype(update_cols_dtype)

    combined_df.year_built = combined_df.year_built.astype('float').astype(pd.Int16Dtype())

    return df

=======
>>>>>>> 36bae1701b2061d3b2b58e106e1e2bad619773f7
if __name__ == "__main__":
    combined_df = clean_column_names(combined_df)
    combined_df = clean_neighborhood_names(combined_df)
    combined_df = dedupe_rows(combined_df)
<<<<<<< HEAD
    combined_df = clean_dtypes(combined_df)
=======
>>>>>>> 36bae1701b2061d3b2b58e106e1e2bad619773f7
