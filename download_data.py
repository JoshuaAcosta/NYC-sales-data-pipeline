"""
Downloads excel spreadsheets by year and borough from NYC
Department of Finance website for property sales between 2003 and 2017.
"""

import os

import requests
from bs4 import BeautifulSoup

# Pandas setting
#pd.set_option('max_columns', 50)

def get_sales_links(url):
    """
    Get links to excel spreadsheets by year and borough from NYC
    Department of Finance website.
    """

    base = "https://www1.nyc.gov"
    website_text = requests.get(url).text
    soup = BeautifulSoup(website_text, "html5lib")
    links = soup.select("a[href$='.xls']")

    list_of_urls = [base + each['href'] for each in links]

    new_list = list_of_urls[8:]
    sales_list_11_17 = new_list[0:35]
    sales_list_03_10 = new_list[35:]

    return sales_list_11_17, sales_list_03_10

def check_for_data_dir(directory):
    """
    Check parent directory for a directory named data.
    Downloaded files containing data will be stored here
    """

    if not os.path.isdir("data/"):
        os.mkdir("data/")
    if os.path.isdir(directory):
        print(directory + " already exists")
    else:
        os.mkdir(directory)
        print(directory + " created")

def download_files(list_of_urls, data_directory):
    """
    Writes NYC property sales data from NYC Dept of Finance
    into a spreadsheet in the data directory.
    """
    check_for_data_dir(data_directory)

    for each in list_of_urls:
        response = requests.get(each)
        filename = each.rsplit('/', 1)[-1]
        path = data_directory + filename
        print(path)

        if filename in data_directory:
            continue
        else:
            with open(path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=5000):
                    file.write(chunk)

if __name__ == "__main__":

    SALES_DATA_URL = "https://www1.nyc.gov/site/finance/taxes/property-annualized-sales-update.page"

    LIST_2011_2017, LIST_2003_2010 = get_sales_links(SALES_DATA_URL)

    download_files(LIST_2011_2017, "data/archived 2011-2017/")

    download_files(LIST_2003_2010, "data/archived 2003-2010/")
