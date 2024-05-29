from hempy.molecule_visualization import draw_3D


import os 
# Installation of the "os" library needed

import nglview
from rdkit import Chem


def test_draw_3D(tmpdir):
    THC_smiles = "CCCCCC1=CC(=C2C3C=C(CCC3C(OC2=C1)(C)C)C)O"  
    THC_mol = Chem.MolFromSmiles(THC_smiles)
    filename = tmpdir.join("THC.pdb")
    
    view = draw_3D(THC_mol, str(filename)) 
    # Check if the file was created
    
    assert os.path.exists(str(filename)), "PDB file was not created" 
    # If the file does not exist, an error message is displayed.
    
    assert view is not None, "No view returned" 
    # checks if view is not None. If the draw_3D function has not returned a view, an error message is displayed.
    
    assert isinstance(view, nglview.NGLWidget), "Returned view is not an NGLWidget"
    # checks whether the object returned by draw_3D is an instance of nglview.NGLWidget. 
    #If not, an error message is displayed




    


