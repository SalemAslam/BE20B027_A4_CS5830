# Importing necessary libraries
from sklearn.metrics import r2_score  # Importing r2_score from scikit-learn
import pandas as pd  # Importing pandas for data manipulation
import yaml  # Importing yaml for reading YAML files
import json  # Importing json for JSON file handling
import os  # Importing os for file and directory operations

# Function to evaluate R2 score and save results as JSON
def evaluate(name_csv):
    # Specifying input and target CSV file paths
    input_path = "/Users/Salem Aslam/Documents/3. Academics/#Sem8/Lab/A4/Input_path/" + name_csv + "_inp.csv"
    target_path = "/Users/Salem Aslam/Documents/3. Academics/#Sem8/Lab/A4/Ground_truth/" + name_csv + "_GT.csv"
    
    # Loading input and target data into pandas DataFrames
    Data_x = pd.read_csv(input_path)
    Data_y = pd.read_csv(target_path)

    # Extracting column names from DataFrames
    cols_x = Data_x.columns[1:]
    cols_y = Data_y.columns[1:]

    # Handling missing dates in input or target data
    if len(Data_x) < len(Data_y):
        missing_date = [i + 1 for i in range(12) if i + 1 not in list(Data_x['DATE'])]
        Data_y = Data_y[~Data_y['DATE'].isin(missing_date)]
    elif len(Data_x) > len(Data_y):
        missing_date = [i + 1 for i in range(12) if i + 1 not in list(Data_y['DATE'])]
        Data_x = Data_x[~Data_x['DATE'].isin(missing_date)]

    # Calculating R2 scores for each column and weighted R2 score
    print(f"\n\n The R2_score of the csv id : {name_csv} is\n\n")
    r2_scores = {}
    for i in range(min(len(cols_x), len(cols_y))):
        x = Data_x[cols_x[i]].values
        y = Data_y[cols_y[i]].values
        
        r2_scores[cols_x[i]] = r2_score(y, x)
        print(f"For column {cols_x[i]}\n\n")
        print(f"{r2_score(y, x):.5f}")
        print("**********\n\n")
    
    X = Data_x.values
    Y = Data_y.values
    
    # Calculating weighted R2 score
    print("Weighted R2 score:\n\n")
    print(f"{r2_score(y, x, multioutput='variance_weighted'):.5f}\n\n")
    r2_scores['Weighted R2 score'] = r2_score(y, x, multioutput='variance_weighted')
    
    # Specifying output directory and saving R2 scores as JSON file
    out_dir = "/Users/Salem Aslam/Documents/3. Academics/#Sem8/Lab/A4/final_result_json"
    with open(os.path.join(out_dir, f"{name_csv}_r2_scores.json"), "w") as f:
        json.dump({name_csv: r2_scores}, f, indent=4)

# Main function
if __name__ == "__main__":
    # Loading parameters from a YAML file
    params = yaml.safe_load(open("params.yaml"))["evaluate"]
    name_csv = params["name_csv"]
    
    # Calling the evaluate function with specified CSV name
    evaluate(name_csv)
