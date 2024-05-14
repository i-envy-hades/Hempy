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



from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit import DataStructs
from sklearn.metrics import pairwise_distances
import numpy as np

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

# Exemple d'utilisation de la fonction
THC_smiles = "CCCCCC1=CC(=C2C3C=C(CCC3C(OC2=C1)(C)C)C)O"
CBD_smiles = "CCCCCC1=CC(=C(C(=C1)O)C2C=C(CCC2C(=C)C)C)O"

THC_mol = Chem.MolFromSmiles(THC_smiles)
CBD_mol = Chem.MolFromSmiles(CBD_smiles)

similarity_jaccard, similarity_tanimoto = calculate_molecular_similarity(THC_mol, CBD_mol)
print("Similarity (Jaccard):", similarity_jaccard)
print("Similarity (Tanimoto):", similarity_tanimoto)    
