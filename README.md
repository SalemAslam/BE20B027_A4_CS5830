# Project Overview

## Description
This project is part of the CS5830: Big Data Laboratory course, aiming to utilize Git and DVC for system and data versioning while assessing the consistency of datasets obtained from the NCEI website.

## Objectives
The primary objective is to leverage Git for source version control and DVC for data version control within the project framework. Additionally, the project aims to evaluate the consistency of datasets from a specified year using hourly and monthly data sourced from the NCEI website.

## Code Flow Explanation
1. **params.yaml**: This YAML file contains experiment parameters such as the target year and the number of locations for data retrieval.
2. **download_data.py**: Responsible for downloading files corresponding to the specified year and number of locations.
3. **process.py**: Computes monthly averages for selected parameters using the hourly data and saves the results as a CSV file.
4. **prepare.py**: Gathers ground truth values from the NCEI website, compiling them with computed averages into stationwise CSV files.
5. **evaluate.py**: Evaluates dataset consistency by calculating the R2 score for compliant pairs of computed and ground truth averages. Consistency is determined based on an R2 score threshold of 0.9.

## Observations
Experiments show that all datasets considered (year=2023) exhibited high consistency, which is evident as the R2 scores exceeds 0.99.