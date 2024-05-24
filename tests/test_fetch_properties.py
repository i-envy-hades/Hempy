from hempy.molecule_properties import fetch_chemical_properties_by_cas


def test_fetch_chemical_properties_by_cas():
    # Test with a valid CAS number, for example formaldehyde (CAS code: 50-00-0)
    cas_number = "50-00-0"  
    data, final_url = fetch_chemical_properties_by_cas(cas_number)
    assert "Error" not in data.to_string() 
    
    # Test with an invalid CAS number
    invalid_cas_number = "invalid_cas_number"
    data, final_url = fetch_chemical_properties_by_cas(invalid_cas_number)
    assert "None" in data.to_string()  
   #If an invalid CAS number is given, the Values will be equal to "None", so the test function checks it





