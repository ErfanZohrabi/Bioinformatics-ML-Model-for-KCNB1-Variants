# Bioinformatics-ML-Model-for-KCNB1-Variants
Machine learning project to predict pathogenic variants in the KCNB1 gene. Uses Random Forest and cross-validation to classify variants as pathogenic or benign, comparing performance with in-silico tools like PolyPhen and SIFT. Includes data preprocessing, model evaluation, and visualization scripts for easy analysis.


Here's a comprehensive plan for setting up your GitHub repository, including the description, README file, data implementation details, and how to categorize your code:

- **Data Files**: These files will help users understand the data used for training and testing the models.
  - `data/GENE_KCNB1.txt`
  - `data/SET1_KCNB1.csv`
  - `data/SET2_KCNB1.csv`
  - `data/SET3_KCNB1.csv`
  - `data/SET4_KCNB1.csv`
  - `data/SET5_KCNB1.csv`
  - `data/KCNB1_features.csv`
  - `data/corrected_model_predictions.csv`

- **Scripts**:
  - `scripts/process_clinvar_file.py`
  - `scripts/merge_files.py`
  - `scripts/build_plots.py`
  - `scripts/rf_model_loocv.py`
  - `scripts/runningModels.py`
  - `scripts/performance.py`
  - `scripts/plot_performance.py`
  - `scripts/gpt_MLbuild.py`

- **Jupyter Notebooks**:
  - `notebooks/exploratory_analysis.ipynb`
  - `notebooks/final.ipynb`

- **Supporting Files**:
  - `requirements.txt`: List of required Python packages.
  - `README.md`: Project overview, instructions, and details.
  - `guide.txt`: Detailed step-by-step guide.
  - `LICENSE`: Licensing details.

---

**"Predictive Modeling of Pathogenic Variants in the KCNB1 Gene using Machine Learning"**

This project aims to predict the pathogenicity of gene variants in the KCNB1 gene using machine learning models like Random Forest, with a focus on comparing predictions against popular in-silico tools such as PolyPhen and SIFT. We include detailed scripts for data preprocessing, feature extraction, training, and evaluation, as well as visualizations to facilitate better understanding. 

Contributions are welcome to expand or enhance the models.

---


# Predictive Modeling of Pathogenic Variants in the KCNB1 Gene

## Overview
This project leverages machine learning to predict the pathogenicity of genetic variants in the **KCNB1** gene. The KCNB1 gene is associated with neurological functions, and its mutations may cause several disorders. The goal is to predict whether variants are pathogenic or benign using Random Forest classification and compare the model with well-known in-silico tools like PolyPhen and SIFT.

## Goals
- Develop a machine learning model to predict the pathogenicity of KCNB1 gene variants.
- Compare model performance with existing in-silico predictors.
- Provide a comprehensive guide to preprocessing, training, and evaluating the model.

## Repository Structure
```
predictive_modeling_KCNB1/
├── data/
│   ├── GENE_KCNB1.txt
│   ├── SET1_KCNB1.csv
│   ├── SET2_KCNB1.csv
│   ├── SET3_KCNB1.csv
│   ├── SET4_KCNB1.csv
│   ├── SET5_KCNB1.csv
│   ├── KCNB1_features.csv
│   └── corrected_model_predictions.csv
├── scripts/
│   ├── process_clinvar_file.py
│   ├── merge_files.py
│   ├── build_plots.py
│   ├── rf_model_loocv.py
│   ├── runningModels.py
│   ├── performance.py
│   ├── plot_performance.py
│   └── gpt_MLbuild.py
├── notebooks/
│   ├── exploratory_analysis.ipynb
│   └── final.ipynb
├── requirements.txt
├── README.md
└── guide.txt
```

## Installation
To use this project, clone the repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/predictive_modeling_KCNB1.git
cd predictive_modeling_KCNB1
pip install -r requirements.txt
```

## Usage
### 1. Data Preprocessing
Use the `process_clinvar_file.py` script to clean and prepare the raw ClinVar data:

```bash
python scripts/process_clinvar_file.py
```

### 2. Feature Extraction and Data Merging
Merge features with `merge_files.py`:

```bash
python scripts/merge_files.py data/SET1_KCNB1.csv data/KCNB1_features.csv
```

### 3. Model Training
Train a Random Forest model using Leave-One-Out Cross-Validation:

```bash
python scripts/rf_model_loocv.py
```

### 4. Model Evaluation
Evaluate the trained model against in-silico tools:

```bash
python scripts/performance.py
```

### 5. Visualization
Generate exploratory plots to understand features and model performance:

```bash
python scripts/plot_performance.py
```

## Data Description
- **Raw Data**: `GENE_KCNB1.txt` is obtained from ClinVar.
- **Processed Datasets**: `SET1` to `SET5` contain different versions of processed data at various stages of analysis.

## Contributing
We welcome contributions to enhance the project's functionality. You can:
- Report bugs or issues.
- Contribute new models or preprocessing methods.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For any questions, please contact the author:
**Erfan Zohrabi** - [Erfanzohrabi.ez@gmail.com](mailto:Erfanzohrabi.ez@gmail.com)

---

### **Data Implementation**

The data implementation phase involves several steps to prepare and transform data for the machine learning model.

1. **Data Cleaning** (`process_clinvar_file.py`):
   - Clean the raw data obtained from ClinVar and store it in a CSV format (`SET1_KCNB1.csv`).

2. **Feature Extraction** (`KCNB1_features.csv`):
   - Extract features such as BLOSUM62 scores, entropy, etc.
   - Features will be merged with the cleaned dataset to generate `SET2_KCNB1.csv`.

3. **Model Training Data** (`SET3_KCNB1.csv`):
   - A Random Forest model is trained on the extracted features, with cross-validation, to predict pathogenicity. The results are saved in this file.

4. **In-silico Tools Comparison** (`SET5_KCNB1.csv`):
   - Predictions from in-silico tools like PolyPhen and SIFT are saved for comparison purposes.

---

### **Code Documentation and Structure**

The **scripts** are designed to handle all aspects of the workflow:

1. **Data Preprocessing**:
   - `process_clinvar_file.py`: Cleans raw input data and saves it as `SET1_KCNB1.csv`.
   - `merge_files.py`: Combines feature datasets, ensuring all features are correctly merged for model training.

2. **Model Training**:
   - `rf_model_loocv.py`: Implements training with Leave-One-Out Cross-Validation to ensure reliable metrics.
   - `runningModels.py`: Runs various models for comparison and prints metrics.

3. **Model Evaluation**:
   - `performance.py`: Calculates evaluation metrics like Accuracy, Recall, F1 Score, and compares them against in-silico tools.
   - `plot_performance.py`: Generates ROC, scatter plots, and other visual metrics to visualize model performance.

4. **Additional Analysis**:
   - `gpt_MLbuild.py`: Implements additional ML components using GPT-based approaches for data interpretation or modeling.
