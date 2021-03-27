import csv
import pandas as pd
import time
from tqdm import tqdm
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

YEAR = "2019"

"""
Liikevaihto (tuhatta euroa)             Turnover (thousand euros)
Liikevaihdon muutos                     Change in turnover
Tilikauden tulos (tuhatta euroa)        Profit for the financial year (thousand euros)
Liikevoitto                             Gains   
Henkilöstö                              Personnel

Omavaraisuusaste                        Equity ratio
Taseen loppusumma (tuhatta euroa)       Balance sheet total (thousand euros)
Quick ratio                             Quick ratio
Current ratio                           Current ratio
Käyttökate                              EBITDA

"""

def profile_links_iterator(link_list):
    """
    This function iterates through the list of all links in
    input list and extracts the financial information for a specified year
    """
    for link in tqdm(link_list):
        columns = []
        office_df = []

        url_client = uReq(link)
        page_html = url_client.read()
        url_client.close
        page_soup = soup(page_html, "html.parser")

        try:
            office_name_container = page_soup.findAll("div", {"class": "Profile__Name listing-name"})
            office_name = office_name_container[0].text
        except IndexError:
            office_name_container = page_soup.findAll("div", {"class": "Profile__Name Profile__Name--short listing-name"})
            office_name = office_name_container[0].text

        try: # Reading the links with Pandas
            office_profile_link_html = pd.read_html(link)
            for dataframe in office_profile_link_html:
                dataframe.loc[:, dataframe.columns.str.startswith(YEAR)]
                for title in dataframe.columns:
                    short_title = title[:-3]
                    columns.append(short_title)

            office_row = pd.DataFrame(data={"column": ["turnover", "change in turnover", "profit", "operative profit", "personnel"]})

            office_row[f"{office_name}"] = dataframe[YEAR]
            office_df = office_row.transpose()
            office_df.columns = office_df.iloc[0]
            office_df.drop(office_df.index[0], inplace=True)
            office_df.to_csv(f'scrapers/raw_data/raw_finances.csv', mode='a', encoding="utf-8", header=False)

        except:
            print("Table not found on page")
        
def main():
    """
    """
    df = pd.read_csv(r"scrapers/raw_data/raw_coordinates.csv", "r", delimiter= ",")

    profile_links = df["profiles"]

    profile_links_iterator(profile_links)

if __name__ == "__main__":
    main()