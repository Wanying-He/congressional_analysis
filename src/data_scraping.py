
# data_scraping.py
# Author: Yetta

import pandas as pd

def load_data(file_path):
    """Load the mock congressional data from CSV."""
    df = pd.read_csv(file_path)
    print("[INFO] Data loaded successfully.")
    print(df.head())  # Display the first few rows
    return df

if __name__ == "__main__":
    load_data('../data/mock_congressional_data.csv')
