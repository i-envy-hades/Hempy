# Test for calculate_molecular_similarity(), with THC and CBD SMILES code which can be obtained with smiles_code()
#imports: Chem, AllChem, DataStructs, pairwise_distances
THC_smiles = "CCCCCC1=CC(=C2C3C=C(CCC3C(OC2=C1)(C)C)C)O"
CBD_smiles = "CCCCCC1=CC(=C(C(=C1)O)C2C=C(CCC2C(=C)C)C)O"

THC_mol = Chem.MolFromSmiles(THC_smiles)
CBD_mol = Chem.MolFromSmiles(CBD_smiles)

similarity_jaccard, similarity_tanimoto = calculate_molecular_similarity(THC_mol, CBD_mol)
print("Similarity (Jaccard):", similarity_jaccard)
print("Similarity (Tanimoto):", similarity_tanimoto)
