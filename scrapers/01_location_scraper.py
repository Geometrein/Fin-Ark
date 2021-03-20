import pandas as pd
from tqdm import tqdm
from geopy import Nominatim
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

def address_cleaner(string):
    """
    This function cleans the address for Nominatim.

    Note: Regex would be faster here. I don't prefer it because of readability.
    """
    return " ".join(str(string).split()[:2])

def address_separator(dataframe):
    """
    This function seperarates street address, postcode and city into separate columns
    """
    df = dataframe.copy()

    address =  df["address"].str.split(",", 1, expand=True).rename(columns={0:"street", 1:"postcode_and_city"})
    address["clean_address"] = address["street"].apply(address_cleaner)

    postcode = address["postcode_and_city"].str.split(" ", 2, expand=True).rename(columns={1:"postcode", 2:"city"})

    address_dict = {"street":address.street,
                    "postcode": postcode.postcode,
                    "city": postcode.city,
                    "name": df.name,
                    "profiles": df.profile}

    return pd.DataFrame(address_dict)

def coordinate_scraper(dataframe):
    """
    This function scrapes office coordinates based on the office address.
    Function appends the coordinates to the input dataframe and saves it.
    """
    # Naming the project. This is necessary for Nominatim to keep track of requests and their frequency.
    geolocator = Nominatim(user_agent="Architectural_Office_Coordinate_Locator")

    # Creating lists for coordinates
    cor_latitude = []
    cor_longitude = []
 
    df = dataframe.copy()

    # getting coordinates from addresses
    print("Scraping office coordinates...")
    for address in tqdm(df["street"]):
        try:
            location = geolocator.geocode(address)
            if location:
                cor_latitude.append(location.latitude)
                cor_longitude.append(location.longitude)
            else:
                raise Exception
        except:
            cor_latitude.append(float("NaN"))
            cor_longitude.append(float("NaN"))


    # Converting coordinate lists into dataframe with two columns
    all_coordinates = pd.DataFrame({"latitude": cor_latitude, "longitude": cor_longitude})

    # Combining
    dff = pd.concat([df.reset_index(drop=True), all_coordinates.reset_index(drop=True)] , axis=1)
    dff = dff[["name", "street", "postcode", "city","latitude", "longitude", "profiles"]]
    dff.to_csv(r"scrapers/raw_data/raw_coordinates.csv", index=False)

def main():
    """
    """
    dataframe = pd.read_csv(r'scrapers/raw_data/raw_names.csv', "r", delimiter = ",")
    df = address_separator(dataframe)

    coordinate_scraper(df)

if __name__ == "__main__":
    main()