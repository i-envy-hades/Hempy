from rdkit import Chem
from rdkit.Chem import Draw, AllChem
from IPython.display import display
#All imports required for the functions, just like the code

from hempy.synthesis_reactions import *

#Reactions of THC and CBD synthesis can easily be seen with these functions
visualize_THC_synthesis()
visualize_CBD_synthesis()