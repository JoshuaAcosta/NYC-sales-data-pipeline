"""
Downloads excel spreadsheets by year and borough from NYC
Department of Finance website for property sales between 2003 and 2017.
"""

import os

import pandas as pd
import requests
from bs4 import BeautifulSoup


def get_sales_links(url):
    """
    Get links to excel spreadsheets by year and borough from NYC
    Department of Finance website.
    """
    try:
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
    Downloaded files containing data will be stored here
    """

    if not os.path.isdir("data/"):
        os.mkdir("data/")


def read_excel_data(list_of_urls, skip_rows_num):
    """
    Reads all .xls url links into pandas, selects specific columns.
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
    Combines all dataframes created
    from separate spreadsheets
    """
    sales_data_url = "https://www1.nyc.gov/site/\
                    finance/taxes/property-annualized-sales-update.page"
    sales_2011_2018, sales_2003_2010 = get_sales_links(sales_data_url)

    archived_2011_2018_df = read_excel_data(sales_2011_2018, 4)
    archived_2003_2010_df = read_excel_data(sales_2003_2010, 3)

    combined_df = pd.concat([archived_2011_2018_df, archived_2003_2010_df],
                            ignore_index=True, sort=False)

    check_for_data_dir()

    combined_df.to_csv("data/NYC_sales_data.csv")


if __name__ == "__main__":

    concat_dfs()
