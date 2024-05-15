import requests
from bs4 import BeautifulSoup
import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit import DataStructs
from sklearn.metrics import pairwise_distances
import numpy as np
from urllib.request import urlopen
from urllib.parse import quote




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




def calculate_molecular_similarity(mol_1 : str, mol_2 : str):

    """
    Calculate the similaritie between two molecules by index Jaccard and Tanimoto.
    -----
    Parameters: 
    
    mol_1 : reference molecule, the one used for comparison
    mol_2 : comparison molecule, which will be studied according to the first
    -----
    Return:
    
    Jaccard and Tanimoto index, between 0 and 1: the closer it is to 1, the more similar the two molecules are. 
    """
    # Générer des empreintes moléculaires pour le THC et le CBD
    fp_thc = AllChem.GetMorganFingerprintAsBitVect(mol_1, 2, nBits=1024)
    fp_cbd = AllChem.GetMorganFingerprintAsBitVect(mol_2, 2, nBits=1024)

    # Convertir en vecteurs numpy
    array_thc = np.zeros((1,))
    array_cbd = np.zeros((1,))
    DataStructs.ConvertToNumpyArray(fp_thc, array_thc)
    DataStructs.ConvertToNumpyArray(fp_cbd, array_cbd)

    # Calculer la similarité de Jaccard
    similarity_jaccard = 1 - pairwise_distances(array_thc.reshape(1, -1), array_cbd.reshape(1, -1), metric="jaccard")[0][0]

    # Calculer la similarité de Tanimoto
    similarity_tanimoto = DataStructs.TanimotoSimilarity(fp_thc, fp_cbd)

    return similarity_jaccard, similarity_tanimoto




def smiles_code(name):
    """
    urllib.request library is imported, it allows URL links to be opened.
    urllib.parse library is imported, it is able to combine URL components into URL strings
    
    Parameters:
    ----------
    -string , corresponding to molecule name (ex: 'Water', 'Methanol', ...)
    
    Returns:
    -------
    -string , corresponding to SMILES code (ex: 'O', 'COH',...)
    
    """
    try:
        url = 'http://cactus.nci.nih.gov/chemical/structure/' + quote(name) + '/smiles' #Opens up a page with SMILES code
        ans = urlopen(url).read().decode('utf8') #Reads answer
        return ans
    except:
        return 'Did not work' #If the molecule name is not well written or doesn't exist, it returns nothing


