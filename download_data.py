import requests  # Importing the requests library for making HTTP requests
from bs4 import BeautifulSoup  # Importing BeautifulSoup for HTML parsing
from urllib.parse import urljoin  # Importing urljoin to join relative URLs
import os  # Importing os for file and directory operations
import yaml  # Importing yaml for reading YAML files
from tqdm import tqdm  # Importing tqdm for progress bar


def download_data(year, start_idx, end_idx):
    # Constructing the URL to access NOAA data for a specific year
    url = "https://www.ncei.noaa.gov/data/local-climatological-data/access/" + f"{year}" + "/"
    
    # Specifying the directory to store downloaded data
    download_path = "/Users/Salem Aslam/Documents/3. Academics/#Sem8/Lab/A4/Downloaded_Data/"
    
    # Creating the directory if it doesn't exist
    os.mkdir("/Users/Salem Aslam/Documents/3. Academics/#Sem8/Lab/A4/Downloaded_Data")
    
    # Sending a GET request to the URL to retrieve HTML content
    response = requests.get(url)
    
    # Parsing the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Storing names of CSV files found in the HTML
    csv_files = []
    for link in soup.find_all("a"): 
        href = link.get("href")
        if href.endswith(".csv"):
            csv_name = href.split("/")[-1]
            csv_files.append(csv_name)

    # Selecting a subset of CSV files based on start and end indices
    downloadable_csvs = csv_files[start_idx: end_idx]
    
    # Iterating over each selected CSV file
    for csv_name in tqdm(downloadable_csvs):
        # Constructing the URL for the CSV file
        csv_url = urljoin(url, csv_name)
        
        # Sending a GET request to download the CSV file
        response = requests.get(csv_url)
        
        # Saving the downloaded content into a local CSV file
        with open(os.path.join(download_path, csv_name), "wb") as f:
            f.write(response.content)

if __name__ == "__main__":
    # Loading parameters from a YAML file
    params = yaml.safe_load(open("params.yaml"))["download_data"]
    year = params["year"]
    start_idx = params["start_idx"]
    end_idx = params["end_idx"]
    
    # Calling the download_data function with specified parameters
    download_data(year, start_idx, end_idx)
