from hempy.molecule_properties import fetch_chemical_properties_by_cas


def test_fetch_chemical_properties_by_cas():
    # Test with a valid CAS number, for example formaldehyde (CAS code: 50-00-0)
    cas_number = "50-00-0"  
    data, final_url = fetch_chemical_properties_by_cas(cas_number)
    assert "Error" not in data.to_string() 
    
    # Test with an invalid CAS number
    invalid_cas_number = "invalid_cas_number"
    data, final_url = fetch_chemical_properties_by_cas(invalid_cas_number)
    assert "Error" in data.to_string()  # Check if an error message is returned





