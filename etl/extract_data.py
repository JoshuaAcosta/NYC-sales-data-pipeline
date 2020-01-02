"""
Collects excel spreadsheets data by year and borough from NYC
Department of Finance website for property sales between 2003 and 2018.
"""

import os
import pandas as pd
import requests
from bs4 import BeautifulSoup


def get_sales_links(url):
    """
    Get links to excel spreadsheets by year (from 2003 to 2018) and 
    borough from NYC Department of Finance website.
    Two seperate lists are created due to the change in which row
    column headers begin after 2010.
    """
    try:
        print("Getting list of urls...")
        base = "https://www1.nyc.gov"
        website_text = requests.get(url).text
        soup = BeautifulSoup(website_text, "html5lib")
        links = soup.select("a[href*='.xls']")

        list_of_urls = [base + each['href'] for each in links]

        del list_of_urls[:17]
        sales_list_11_18 = list_of_urls[0:40]
        sales_list_03_10 = list_of_urls[40:]

    except requests.RequestException as exception:
        return exception

    return sales_list_11_18, sales_list_03_10


def check_for_data_dir():
    """
    Check parent directory for a directory named data.
    One is created if it doesn't exist to store .csv file
    containing all transactions.
    """

    if not os.path.isdir("../data/"):
        print("Creating a data directory...")
        os.mkdir("../data/")


def read_excel_data(list_of_urls, skip_rows_num):
    """
    Creates a list of dataframes, one df per spreadsheet, and then concats them into
    one combined dataframe. For each spreadsheet, columns desired are specified.
    Tax related columns and those with mostly null values are not added.
    Numeber of rows to skip for each df is specific due to change made by NY DOF 
    after 2010.
    """
    use_col_names = ["BOROUGH", "NEIGHBORHOOD", "BUILDING CLASS CATEGORY",
                     "ADDRESS", "APARTMENT NUMBER", "ZIP CODE",
                     "RESIDENTIAL UNITS", "COMMERCIAL UNITS", "TOTAL UNITS",
                     "LAND SQUARE FEET", "GROSS SQUARE FEET", "YEAR BUILT",
                     "BUILDING CLASS AT TIME OF SALE",
                     "SALE PRICE", "SALE DATE"]

    col_str = "A:C,I:Q, S, T, U"

    list_of_dfs = [pd.read_excel(filename, skiprows=skip_rows_num,
                   dtype=str, usecols=col_str, names=use_col_names)
                   for filename in list_of_urls]

    dataframe = pd.concat(list_of_dfs, ignore_index=True, sort=False)

    return dataframe


def concat_dfs():
    """
    Combines all dataframes created from separate spreadsheets.
    Saves one .csv file with all transactions under the data directory.

    """
    sales_data_url = ("https://www1.nyc.gov/site/"
                      "finance/taxes/property-annualized-sales-update.page")

    sales_2011_2018, sales_2003_2010 = get_sales_links(sales_data_url)

    print("Creating dataframes for years 2011 through 2018...")
    archived_2011_2018_df = read_excel_data(sales_2011_2018, 4)
    print("Creating dataframes for years 2003 through 2010..")
    archived_2003_2010_df = read_excel_data(sales_2003_2010, 3)

    print("Concatenating all dataframes...")

    combined_df = pd.concat([archived_2011_2018_df, archived_2003_2010_df],
                            ignore_index=True, sort=False)

    check_for_data_dir()

    print("Saving csv file into /data")

    combined_df.to_csv("../data/NYC_sales_data.csv")


if __name__ == "__main__":

    concat_dfs()
