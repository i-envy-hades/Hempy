from hempy.molecule_properties import cas_number



def test_cas_number():
    # Test with a sample molecule name, for example acetic acid
    molecule_name = "acetic acid"
    actual_cas_number = "64-19-7"
    expected_cas_number = cas_number(molecule_name)
    
    assert expected_cas_number == actual_cas_number

    #Test with an invalid name
    molecule_name = "invalid name"
    
    expected_cas_number = cas_number(molecule_name)

    assert expected_cas_number == 'PE html><html lang="en"><head>\n  <!-- Google Tag Manager -->\n  <script>(function(w'
    #This error message appears when an incorrect URL is entered