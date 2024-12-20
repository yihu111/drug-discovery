# Drug Discovery Project

This project focuses on drug discovery using cheminformatics techniques. It includes exploratory data analysis (EDA), feature extraction, molecular descriptor calculations, and machine learning for bioactivity prediction.

## Features
- **Data Preprocessing**: Includes cleaning and preparing molecular datasets.
- **Lipinski Descriptors**: Calculated using RDKit for molecular property analysis.
- **Fingerprint Generation**: Creates molecular fingerprints for machine learning.
- **Machine Learning Models**: Built and optimized using Random Forest for bioactivity prediction.

## Repository Structure
```bash
project/
├── data/                    
├── notebooks/               
│   ├── 01_bioactivity_data.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_create_molecular_fingerprints.ipynb
│   ├── 04_model_building_evaluation.ipynb
├── utils/                     
│   ├── lipinski.py          
├── models/                  
├── requirements.txt         
├── README.md                
└── .gitignore               
```

## Setup Instructions
### Prerequisites
- Python 3.8 or higher
- Install required dependencies:
  ```bash
  pip install -r requirements.txt
  ```

### How to Run
1. Exploratory Data Analysis: Open notebooks/eda.ipynb in Jupyter Notebook to explore and preprocess data.

2. Feature Extraction: Use notebooks/03_create_molecular_fingerprints.ipynb to generate molecular fingerprints.

3. Model Building: Train and evaluate machine learning models in notebooks/04_model_building_evaluation.ipynb.

4. Lipinski Descriptors: Use the utils/lipinski.py script to calculate descriptors directly: 

    ```bash
    from lipinski import add_lipinski_descriptors
    df = add_lipinski_descriptors(df, smiles_column="SMILES") 
    ```

## Key Dependencies
- RDKit
- Scikit-learn
- Pandas
- Seaborn
- PaDELpy

## Acknowledgments/References
A big thank you to the Chanin Nantasenamat who inspired this project.