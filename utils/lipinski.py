import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors, Lipinski


def add_lipinski_descriptors(df: pd.DataFrame, smiles_column: str) -> pd.DataFrame:
    """
    Adds Lipinski descriptors directly as columns to an existing DataFrame.

    Parameters:
    - df (pd.DataFrame): Input DataFrame containing a SMILES column.
    - smiles_column (str): The name of the column with SMILES strings.

    Returns:
    - pd.DataFrame: The DataFrame with new Lipinski descriptor columns.
    """
    # Define a helper function to compute descriptors for a single SMILES string
    def compute_descriptors(smiles):
        mol = Chem.MolFromSmiles(smiles)
        if mol:
            return (
                Descriptors.MolWt(mol),
                Descriptors.MolLogP(mol),
                Lipinski.NumHDonors(mol),
                Lipinski.NumHAcceptors(mol)
            )
        else:
            return (None, None, None, None)

    # Apply the helper function to the SMILES column and unpack results into new columns
    df[['MW', 'LogP', 'NumHDonors', 'NumHAcceptors']] = df[smiles_column].apply(compute_descriptors).apply(pd.Series)

    return df