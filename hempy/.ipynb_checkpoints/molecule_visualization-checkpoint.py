from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit import DataStructs
from sklearn.metrics import pairwise_distances
import numpy as np

from rdkit.Chem import Draw
from rdkit.Chem import Draw

def draw_2D(smiles):
    """
    Draw molecules in 2D according to these smiles with the fonctionnel group hightlight, here the hydroxyl.
    -----
    Parameters: 
    
    smiles of the molecule found in PubChem
    -----
    Return:

    the molecule drawn in 2D 
    """
    IPythonConsole.ipython_useSVG = True
    molecule = Chem.MolFromSmiles(smiles)
    if molecule:
        return Draw.MolToImage(molecule)
    else:
        return "Impossible de dessiner la molécule, mauvais format pour les Smiles."
      

THC_molecule = Chem.MolFromSmiles("CCCCCC1=CC(=C2C3C=C(CCC3C(OC2=C1)(C)C)C)O") #Dronabinol from PubChem 
print(THC_molecule)
#Synonyms: Dronabinol, tetrahydrocannabinol, delta9-THC

CBD_molecule = Chem.MolFromSmiles("CCCCCC1=CC(=C(C(=C1)O)C2C=C(CCC2C(=C)C)C)O") #Cannabidiol from PubChem
print(CBD_molecule)
#Synonyms : Cannabidiol


from nglview import show_structure_file

def draw_3D(molecule: str, filename: str):
    """
    Generates a 3D structure from a RDKit Molecule object.

    Parameters:

    molecule: name of the molecule with them smiles
    filename: name of the file's molecule
    --------
    Return:

    the molecule appears in 3D with the functional groups in red, here the hydroxil.
    
    
    """
    # Ajouter des hydrogènes aux molécules
    mol = Chem.AddHs(molecule)

    # Générer les coordonnées 3D
    AllChem.EmbedMolecule(mol)

    # Convertir les molécules en format PDB
    Chem.MolToPDBFile(mol, filename)

    # Charger les fichiers PDB dans nglview
    view = show_structure_file(filename)

    # Ajouter des représentations visuelles
    view.add_ball_and_stick()
    view.add_unitcell()
    view.center()

    # Afficher la vue
    return view



