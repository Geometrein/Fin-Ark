from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd
from tqdm import tqdm

# Link of the search page & number of pages to scrap
SEARCH_LINK = "https://www.finder.fi/search?what=Arkkitehtitoimisto%2C%20suunnittelutoimisto" + "&page="
NUMBER_OF_PAGES = 100

# Creating lits to store scraped information
names = []
addresses = []
profiles = []

def container_scrapper(containers, names, addresses, profiles):
    """
    This function iterates through each search result container on the page
    and extracts office name, address and link.
    The results are appended to lists.
    If no value is found "NaN" will be appended instead.(All lists must have the same length.)
    """
    for container in containers:
        try:
            office_name_container = container.findAll("div", {"class": "SearchResult__Name"})
            office_name = office_name_container[0].text  
        except:
            office_name = float("NaN")

        names.append(office_name)

        try:
            office_address_container = container.findAll("a", {"class": "SearchResult__Link"})
            office_address = office_address_container[0].text
        except:
            office_address = float("NaN")

        addresses.append(office_address)

        try:
            link = container.find('a', href=True)  
        except:
            link = float("NaN")
            
        profiles.append(str("https://www.finder.fi" + link["href"]))

def append_to_file(names, addresses, profiles):
    """
    This function appends information scraped from each page to .csv file
    """
    df = pd.DataFrame({"name": names, "address": addresses, "profile": profiles})
    
    try:
        df.to_csv(f'raw_data/raw_names.csv', mode='a', index=False, encoding="utf-8", header=False)
    except:
        print("Probelm appending to file.")
        quit()
  
def main():
    """
    - Luke, I am your main()!
    - Noooo
    """
    # Name of the resulting .csv file
    print("Saving office names, addresses and links to a .csv file")
    # Loop for every page with office containers
    for page_number in tqdm(range(NUMBER_OF_PAGES)):

        pages = SEARCH_LINK + str(page_number)
        url_client = uReq(pages)
        page_html = url_client.read()
        url_client.close
        page_soup = soup(page_html, "html.parser")

        # Finding all office container in one page of the search result
        containers = page_soup.findAll("div", {"class":"SearchResult--compact"})

        # Scraping and appending to a file
        container_scrapper(containers, names, addresses, profiles)
        append_to_file( names, addresses, profiles)

        # Clearing the lists after each page is scraped
        names.clear()
        addresses.clear()
        profiles.clear()

if __name__== "__main__":
    main()