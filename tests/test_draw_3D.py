from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit import DataStructs
from sklearn.metrics import pairwise_distances
import numpy as np

from rdkit.Chem import Draw
from rdkit.Chem import Draw
#All imports required for the functions, just like the code

from hempy.molecule_visualization import *




def test_draw_3D():
    molecule_1 = "CCC" #Choose a random SMILES code, for example propane
    draw_3D(molecule_1)

    molecule_2 = "invalid" #Select an invalid name
    assert draw_3D(molecule_2) == "Impossible de dessiner la molécule, mauvais format pour les Smiles." 
#Verify that the incorrect smiles raises an error



test_draw_3D()