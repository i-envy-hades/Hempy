from hempy.molecule_properties import smiles_code

def test_smiles_code()
    expected_smiles = smiles_code("Acetic acid")
    actual_smiles = "CC(=O)O"

    assert expected_smiles == actual_smiles