import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_chemical_properties_by_cas(cas_number):
    """
    Fetches chemical properties for a given CAS number from ChemSpider.

    Parameters:
    cas_number (str): The CAS number of the chemical.

    Returns:
    A DataFrame containing the properties, styled for better visualization, and the URL to the chemical's detail page on ChemSpider.
    """
    search_url = "http://www.chemspider.com/Search.aspx?q="
    cas_url = search_url + cas_number
    
    with requests.Session() as session:
        try:
            response = session.get(cas_url)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return pd.DataFrame().style.set_caption("Error: HTTP Error"), None
        except requests.exceptions.RequestException as e:
            return pd.DataFrame().style.set_caption("Error: Request Failed"), None

        final_url = response.url
        soup = BeautifulSoup(response.text, 'html.parser')
        properties = {'Molecular Formula': None, 'Average mass': None, 'Monoisotopic mass': None}
        for prop in properties:
            element = soup.find('span', string=prop)
            if element and element.next_sibling:
                properties[prop] = element.next_sibling.text.strip()

        # Creating DataFrame
        data = pd.DataFrame(list(properties.items()), columns=['Property', 'Value'])
        
        # Styling the DataFrame
        data = data.style.set_properties(**{'text-align': 'left'}).set_table_styles([dict(selector='th', props=[('text-align', 'left')])])
        return data, final_url

# Usage of the function
cas_number = '1972-08-3'  # CAS for THC
properties_data, chemical_url = fetch_chemical_properties_by_cas(cas_number)
display(properties_data)  # This will display the styled table in Jupyter Notebook or similar
print(f"URL to chemical page: {chemical_url}")
