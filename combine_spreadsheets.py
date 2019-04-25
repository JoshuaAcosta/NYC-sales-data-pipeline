"""
This module reads the numerous spreadsheets downloaded
by executing download_data.py
"""

import glob

import pandas as pd

def read_excel_data(filepath, skip_rows_num):
    """
    Reads all .xls files into pandas, selects specific columns.
    """
    use_col_names = ["BOROUGH", "NEIGHBORHOOD", "BUILDING CLASS CATEGORY",\
                     "ADDRESS", "APARTMENT NUMBER", "ZIP CODE",\
                     "RESIDENTIAL UNITS", "COMMERCIAL UNITS", "TOTAL UNITS",\
                     "LAND SQUARE FEET", "GROSS SQUARE FEET", "YEAR BUILT",\
                     "BUILDING CLASS AT TIME OF SALE",\
                     "SALE PRICE", "SALE DATE"]

    col_str = "A:C,I:Q, S, T, U"

    list_of_filenames = glob.glob(filepath + "*.xls")
    list_of_dfs = [pd.read_excel(filename, skiprows=skip_rows_num, dtype=str,\
                    usecols=col_str, names=use_col_names) for filename in list_of_filenames]
    df = pd.concat(list_of_dfs, ignore_index=True, sort=False)
    return df

def concat_dfs():
    """Coombined all dataframes created from separte spreadsheets """
    archived_2011_2017_df = read_excel_data("data/archived 2011-2017/", 4)
    archived_2003_2010_df = read_excel_data("data/archived 2003-2010/", 3)

    df = pd.concat([archived_2011_2017_df, archived_2003_2010_df], ignore_index=True, sort=False)

    return df

if __name__ == "__main__":
    combined_df = concat_dfs()
