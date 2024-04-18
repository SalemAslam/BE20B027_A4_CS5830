# Importing necessary libraries
import pandas as pd  # For data manipulation
import yaml  # For reading YAML files
import os  # For file and directory operations

# Function to process input data
def process(path):
    # Directory to save processed input data
    os.mkdir("/Users/Salem Aslam/Documents/3. Academics/#Sem8/Lab/A4/Input_path")
    input_path = "/Users/Salem Aslam/Documents/3. Academics/#Sem8/Lab/A4/Input_path/"
    
    # Columns to keep for input data
    cols_to_keep = ['DATE', 'DailyMinimumDryBulbTemperature', 'DailyDepartureFromNormalAverageTemperature', 'DailyAverageDryBulbTemperature', 'DailyMaximumDryBulbTemperature']

    # List of CSV files in the specified directory
    csv_files = os.listdir(path)

    # Loop through each CSV file
    for file in csv_files:
        # Construct complete path to the CSV file
        complete_path = os.path.join(path, file)
        
        # Read data from the CSV file
        Data = pd.read_csv(complete_path)
        
        # Extract month from the 'DATE' column and select desired columns, then drop rows with missing values
        Data = Data.assign(DATE=Data['DATE'].str[5:7])[cols_to_keep].dropna()
        
        # Group data by month and calculate mean for numeric columns
        Data = Data.groupby('DATE').mean(numeric_only=True)
        
        # Check if the processed data contains sufficient samples
        if len(Data) > 10:
            # Save the processed input data to a new CSV file
            Data.to_csv(os.path.join(input_path, f'{file[:-4]}_inp.csv'))
    
# Main function
if __name__ == "__main__":
    # Load parameters from a YAML file
    params = yaml.safe_load(open("params.yaml"))["process"]
    
    # Get the path to the data directory
    path = params["path"]
    
    # Call the process function with the specified data path
    process(path)
