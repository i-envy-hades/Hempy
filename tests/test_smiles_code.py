from hempy.molecule_properties import smiles_code

def test_smiles_code():
    # Test with a valid name, for example caffeine (SMILES code: Cn1cnc2N(C)C(=O)N(C)C(=O)c12)
    assert smiles_code("caffeine") == "Cn1cnc2N(C)C(=O)N(C)C(=O)c12"
    
    # Test with an invalid name
    assert smiles_code("invalid_name") == "Did not work" 

#Nothing should be returned by this function, meaning smiles_code() works perfectly

test_smiles_code()