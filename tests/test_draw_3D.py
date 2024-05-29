from hempy.molecule_visualization import draw_3D
from rdkit import Chem

def test_draw_3D():
    THC_smiles = "CCCCCC1=CC(=C2C3C=C(CCC3C(OC2=C1)(C)C)C)O"
    THC_mol = Chem.MolFromSmiles(THC_smiles)
    filename = "THC.pdb"
    draw_3D(THC_mol, filename)


    


