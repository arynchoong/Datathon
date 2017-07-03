# Datathon
Repository for NUS-MIT Datathon 2017 Team 02

eICU-CRD Dataset

Introduction & Documentation: https://eicu-crd.mit.edu/about/eicu/
 
Github repository: https://github.com/mit-eicu/eicu-code
 
Example code: https://github.com/mit-eicu/eicu-code/blob/master/concepts/icustay_detail.sql

## Repository structure
```
    ├── data <- Data files
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── src <- Souce codes
    │   ├── data <- source codes to download/clean data
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   ├── models         <- Scripts to train models and then use trained models to make predictions
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │
    ├── viz <--Visualisations
    │   └── notebook <- Jupyter notebooks
    │   └── tableau <- Tableau files
    │
    └── web <- web based repository documentations and info
```
