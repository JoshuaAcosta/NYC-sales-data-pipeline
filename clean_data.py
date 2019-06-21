"""
Cleans and dedupes data.
"""
import numpy as np
import pandas as pd

def clean_column_names(df):
    """
    Updates columns names by stripping white spaces, makes all characters
    lower case and replacing and spaces with an underscore.
    """
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

def clean_neighborhood_names(df):
    """strips whitespace from neighborhood names"""
    df["neighborhood"] = df["neighborhood"].apply(str.rstrip)

def clean_apt_nums(df):
    """removes all commas from cells in the apartment_number column"""
    df["apartment_number"] = df["apartment_number"].str.replace(',', '')

def dedupe_rows(df):
    """drops any duplicate rows in dataframe"""
    df.drop_duplicates()

def update_dtypes(df):
    """update dtypes for several columns to minimize memory size"""
    df["sale_date"] = df["sale_date"].astype("datetime64[ns]")
    df["sale_price"] = df["sale_price"].astype("float64")
    df["land_square_feet"] = df["land_square_feet"].astype("int64")
    df["gross_square_feet"] = df["gross_square_feet"].astype("int64")
    df["zip_code"] = df["zip_code"].astype("int16")
    df["residential_units"] = df["residential_units"].astype("int16")
    df["commercial_units"] = df["commercial_units"].astype("int16")
    df["total_units"] = df["total_units"].astype("int16")
    df["year_built"] = df["year_built"].astype("int16")

def clean_neighborhood_values(df):
    """updates neighborhood values with correct names"""
    df["neighborhood"].replace('1026', 'MIDTOWN EAST', inplace=True)
    df["neighborhood"].replace('3019', 'CROWN HEIGHTS', inplace=True)
    df["neighborhood"].replace('3004', 'BATH BEACH', inplace=True)
    df["neighborhood"].replace('1021', 'LITTLE ITALY', inplace=True)

def clean_year_built(df):
    """update year built of property address for accuracy"""
    df.loc[df.address == "762 MARCY AVENUE, 1B", 'year_built'] = 2018.0
    df.loc[df.address == "762 MARCY AVENUE, 4", 'year_built'] = 2018.0
    df.loc[df.address == "9 BARTLETT AVENUE, 0", 'year_built'] = 2018.0

def clean_zip_code(df):
    """update zip code of property address for accuracy"""
    df.loc[df.address == "762 MARCY AVENUE, 1B", 'zip_code'] = 11216.0
    df.loc[df.address == "762 MARCY AVENUE, 4", 'zip_code'] = 11216.0

def fill_na(df):
    """fill nans in sepecific columns"""
    df.replace([np.inf, -np.inf], np.nan)
    fill_zero = {"residential_units":0.0, "commercial_units":0.0, "total_units":0.0,\
                 "land_square_feet":0.0, "gross_square_feet":0.0}
    return df.fillna(value=fill_zero)

def update_borough_values(df):
    """update borough values to proper names"""
    df["borough"].replace({1 : "Manhattan", 2 : "Bronx", 3 : "Brooklyn", 4 : "Queens",\
                             5 : "Staten Island"}, inplace=True)

def split_address_apt(df):
    """
    Slice original dataframe to a another dataframe if the address
    value for a row contains a comma. Splits address value into two
    values if initial cell contained the column: one containing the
    property address and another containing apartment number.
    Apartment value then added to apartment_number column for row.
    """
    df2 = df[df['address'].str.contains(",")]
    for index_label, row_series in df2.iterrows():
        new_address, apt_num = row_series['address'].split(',', 1)
        df2.at[index_label, 'address'] = new_address
        df2.at[index_label, 'apartment_number'] = apt_num
    df.update(df2)

def clean_data_to_csv(df, filename):
    """
    saves dataframe in csv format to data directory
    """
    df.to_csv(filename)

if __name__ == "__main__":
    df = pd.read_csv("data/NYC_sales_data.csv", index_col=0)
    clean_column_names(df)
    clean_neighborhood_names(df)
    dedupe_rows(df)
    df = fill_na(df)
    clean_year_built(df)
    clean_zip_code(df)
    clean_neighborhood_values(df)
    update_borough_values(df)
    split_address_apt(df)
    clean_apt_nums(df)
    update_dtypes(df)
    clean_data_to_csv(df, "data/Clean_NYC_sales_data.csv")
