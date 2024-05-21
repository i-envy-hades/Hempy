from hempy.molecule_properties import calculate_molecular_similarity

#Required imports for the test
import numpy as np
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit import DataStructs
from sklearn.metrics import pairwise_distances


def test_calculate_molecular_similarity():
    
    mol_1 = Chem.MolFromSmiles("CCO")  # Molecule 1 example (ethanol)
    mol_2 = Chem.MolFromSmiles("CC(=O)O")  # Molecule 2 example (acetic acid)

    #Asigns molecule fingerprints
    fp_1 = AllChem.GetMorganFingerprintAsBitVect(mol_1, 2, nBits=1024)
    fp_2 = AllChem.GetMorganFingerprintAsBitVect(mol_2, 2, nBits=1024)

    # Converts into numpy vectors
    array_1 = np.zeros((1,))
    array_2 = np.zeros((1,))
    DataStructs.ConvertToNumpyArray(fp_1, array_1)
    DataStructs.ConvertToNumpyArray(fp_2, array_2)
    
    # Jaccard similarity calculation
    similarity_jaccard = 1 - pairwise_distances(array_1.reshape(1, -1), array_2.reshape(1, -1), metric="jaccard")[0][0]

    # Tanimoto similarity calculation
    similarity_tanimoto = DataStructs.TanimotoSimilarity(fp_1, fp_2)

    return similarity_jaccard, similarity_tanimoto


# Call the test functions and check the values
similarity_jaccard, similarity_tanimoto = test_calculate_molecular_similarity()
print(f"Similarity (Jaccard): {similarity_jaccard:.4f}")
print(f"Similarity (Tanimoto): {similarity_tanimoto:.4f}")

similarity_jaccard_ex, similarity_tanimoto_ex = calculate_molecular_similarity("CCO", "CC(=O)O")
print("Expected Similarity (Jaccard):", similarity_jaccard_ex)
print("Expected Similarity (Tanimoto):", similarity_tanimoto_ex)
