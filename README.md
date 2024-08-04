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
pip install -r requirements.txt  //Installs all necessary files for running .py file
cd streamlit
streamlit run main.py


ml_bootcamp/
├── data                             # Dataset files
│   ├── new_preprocessed_loan_data.csv
│   ├── processed_loan_data.csv
│   └── ...                          # Other dataset files
├── notebooks                        # Jupyter notebooks
│   ├── ML_Bootcamp_Day_1.ipynb
│   ├── ML_Bootcamp_Day_2_(Final).ipynb
│   └── ...                          # Other notebook files
├── streamlit                        # Streamlit application files
│   ├── main.py
│   └── ...                          # Other streamlit files
├── Colab                            # Colab notebooks
├── requirements.txt                 # Required packages
└── README.md                        # This README file
