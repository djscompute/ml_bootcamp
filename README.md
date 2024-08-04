# ML Bootcamp

This repository contains materials and scripts from the ML Bootcamp organized by DJS Compute and DJS S4DS. It includes Jupyter notebooks, datasets, and scripts for machine learning tasks.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

To set up the environment, clone this repository and install the required packages:

```sh
git clone https://github.com/djscompute/ml_bootcamp.git
cd ml_bootcamp
pip install -r requirements.txt
pip install joblib xgboost streamlit
streamlit run main.py


ml_bootcamp/
├── Colab                           # Colab notebooks
├── ML_Bootcamp_Day_1.ipynb         # Jupyter notebook for Day 1
├── ML_Bootcamp_Day_2_(Final).ipynb # Jupyter notebook for Day 2
├── main.py                         # Streamlit application
├── new_preprocessed_loan_data.csv  # New preprocessed dataset
├── processed_loan_data.csv         # Original processed dataset
├── requirements.txt                # Required packages
└── README.md                       # This README file
