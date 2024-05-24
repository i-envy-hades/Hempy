from hempy.molecule_visualization import draw_2D



def test_draw_2D():
    molecule_1 = "O" #Choose a random SMILES code, for example water
    draw_2D(molecule_1)

    molecule_2 = "invalid" #Select an invalid name
    assert draw_2D(molecule_2) == "Impossible de dessiner la molécule, mauvais format pour les Smiles." 
#Verify that the incorrect SMILES raises an error


