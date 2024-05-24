from hempy.molecule_visualization import draw_3D



def test_draw_3D():
    THC = "CCCCCC1=CC(=C2C3C=C(CCC3C(OC2=C1)(C)C)C)O" #Choose a random SMILES code, for example propane
    draw_3D(THC, "THC.pdb")
#Verify that something is drawn

