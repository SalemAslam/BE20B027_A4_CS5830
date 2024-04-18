# Importing necessary libraries
import pandas as pd  # For data manipulation
import os  # For file and directory operations
import yaml  # For reading YAML files

# Function to prepare target data
def prepare(path):
    # Columns to keep for target data
    cols_for_target = ['DATE', 'MonthlyMinimumTemperature', 'MonthlyDepartureFromNormalAverageTemperature', 'MonthlyMeanTemperature', 'MonthlyMaximumTemperature']
    
    # Directory to save prepared target data
    save_dir = "/Users/Salem Aslam/Documents/3. Academics/#Sem8/Lab/A4/Ground_truth/"
    
    # Creating the directory if it doesn't exist
    os.mkdir("/Users/Salem Aslam/Documents/3. Academics/#Sem8/Lab/A4/Ground_truth")
    
    # List to store CSV file names
    csv_files = []
    
    # Loop through files in the specified directory
    for file in os.listdir(path):
        # Check if file is a CSV file
        if file.endswith('.csv'):
            csv_files.append(file)

    # Loop through CSV files
    for file in csv_files:
        # Construct full path to the CSV file
        full_path = os.path.join(path, file)
        
        # Read data from the CSV file
        data = pd.read_csv(full_path)
        
        # Extract month from the 'DATE' column and select target columns
        data = data.assign(DATE=data['DATE'].str[5:7])[cols_for_target]
        
        # Set 'DATE' column as index
        data = data.set_index('DATE')
        
        # Drop rows with missing values
        target_data = data.dropna()
        
        # Check if the remaining data is adequate
        if len(target_data) < 10:
            print("Inadequate data so deleting the file.")
            # Delete the file if data is inadequate
            os.remove(full_path)
        else:
            # Save the prepared target data to a new CSV file
            target_data.to_csv(os.path.join(save_dir, f'{file[:-4]}_GT.csv'))

# Main function
if __name__ == "__main__":
    # Load parameters from a YAML file
    params = yaml.safe_load(open("params.yaml"))["prepare"]
    
    # Get the path to the data directory
    data_path = params["path"]
    
    # Call the Prepare function with the specified data path
    prepare(data_path)
