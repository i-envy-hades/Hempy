from hempy.molecule_visualization import draw_3D


import os 
import nglview
from rdkit import Chem



def test_draw_3D(tmpdir):
    THC_smiles = "CCCCCC1=CC(=C2C3C=C(CCC3C(OC2=C1)(C)C)C)O"  # Ethanol SMILES string 
    THC_mol = Chem.MolFromSmiles(THC_smiles)
    filename = tmpdir.join("THC.pdb")
    view = draw_3D(THC_mol, str(filename)) # Check if the file was created
    assert os.path.exists(str(filename)), "PDB file was not created" 
    # Verify the view 
    assert view is not None, "No view returned" 
    assert isinstance(view, nglview.NGLWidget), "Returned view is not an NGLWidget"
    # Additional checks could include verifying contents of the file, etc.




    


