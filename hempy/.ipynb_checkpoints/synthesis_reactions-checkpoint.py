from rdkit import Chem
from rdkit.Chem import Draw, AllChem
from IPython.display import display

def visualize_THC_synthesis():
    "This function returns the synthesis reaction of THC"
    # Smiles of molecules
    smiles_olivetol = 'C1=CC(=C(C=C1O)CCC(=O)O)O'
    smiles_gpp = 'CCOP(=O)(OCC)OC(=C)C'
    smiles_cbga = 'CCCCC(C)C1=CC2=C(C3C(CCC3C(=O)O)O)C(=C(C=CC2=C1)O)C'
    smiles_thca = 'CC1=CC2=C(C3C(C2(C(=C1)O)OC)(CC=C3C(=O)CO)C)C'
    smiles_thc = 'CCCCC1=CC2=C(C3C(C2(CCC3C(=C)CO)C)(C)C)C(=C1)O'

    # Reaction from Olivetol + GPP to CBGA
    print("Reaction from Olivetol + GPP to CBGA in the presnece of Geranyl-transferase(enzyme) :")
    reaction1 = AllChem.ReactionFromSmarts(f'{smiles_olivetol}.{smiles_gpp}>>{smiles_cbga}')
    image1 = Draw.ReactionToImage(reaction1)
    display(image1)

    # Reaction from CBGA to THCA
    print("Reaction from CBGA to CBDA in the presnece of THCA-transferase(enzyme) :")
    reaction2 = AllChem.ReactionFromSmarts(f'{smiles_cbga}>>{smiles_thca}')
    image2 = Draw.ReactionToImage(reaction2)
    display(image2)

    # Reaction from THCA to THC (Decarboxylation)
    print("Reaction from THCA to THC (Decarboxylation) :")
    reaction3 = AllChem.ReactionFromSmarts(f'{smiles_thca}>>{smiles_thc}')
    image3 = Draw.ReactionToImage(reaction3)
    display(image3)
visualize_THC_synthesis()

def visualize_CBD_synthesis():
    "This function returns the synthesis reaction of CBD"
    # Smiles of molecules
    smiles_olivetol = 'C1=CC(=C(C=C1O)CCC(=O)O)O'
    smiles_gpp = 'CCOP(=O)(OCC)OC(=C)C'
    smiles_cbga = 'CCCCC(C)C1=CC2=C(C3C(CCC3C(=O)O)O)C(=C(C=CC2=C1)O)C'
    smiles_cbda = 'CCCCC(C)C1=CC2=C(C3C(CCC3C(=O)O)O)C(C)(C=CC2=C1)O'
    smiles_cbd = 'C1=CC2=C(C3=C1C=CC(=C3)C)C(C)(C=CC2O)O'

    # Reaction from Olivetol + GPP to CBGA
    print("Reaction from Olivetol + GPP to CBGA in the presence of Geranyl-transferase(enzyme):")
    reaction1 = AllChem.ReactionFromSmarts(f'{smiles_olivetol}.{smiles_gpp}>>{smiles_cbga}')
    img1 = Draw.ReactionToImage(reaction1)
    display(img1)

    # Reaction from CBGA to CBDA
    print("Reaction from CBGA to CBDA in the presence of CBDA synthase(enzyme):")
    reaction2 = AllChem.ReactionFromSmarts(f'{smiles_cbga}>>{smiles_cbda}')
    img2 = Draw.ReactionToImage(reaction2)
    display(img2)

    # Reaction from CBDA to CBD (Decarboxylation)
    print("Reaction from CBDA to CBD (Decarboxylation):")
    reaction3 = AllChem.ReactionFromSmarts(f'{smiles_cbda}>>{smiles_cbd}')
    img3 = Draw.ReactionToImage(reaction3)
    display(img3)
visualize_CBD_synthesis()
