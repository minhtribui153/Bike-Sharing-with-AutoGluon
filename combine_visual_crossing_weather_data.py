"""
This Python program combines all the datasets I've collected from the Visual Crossing Weather Database for
Chicago, US under the folder 'chicago_weatherdata'

If you would like to download datasets from the Visual Crossing Weather database, please collect from:
https://www.visualcrossing.com/weather/weather-data-services
"""

import pandas as pd
import glob
import os
from tqdm import tqdm

import pandas as pd
import glob
import os
from tqdm import tqdm

directory_path = "./chicago_weatherdata"
output_file = "chicago_weatherdata.csv"

# Get all CSV files in the specified directory
csv_files = glob.glob(os.path.join(directory_path, "*.csv"))

# Check if there are any CSV files
if not csv_files:
    print("No CSV files found in the specified directory.")
    exit(1)

# List to store individual dataframes
dfs = []

# Read each CSV file and append to the list
progress = tqdm(range(len(csv_files)))
for file in csv_files:
    progress.display(f"Reading file {os.path.basename(file)}...", progress.pos + 1)
    df = pd.read_csv(file)

    # Name is not necessary, because the dataset are all Chicago, US datasets
    # We only need variables specific to the weather forecast
    df = df.drop(columns = [
        "tempmax", "tempmin", "feelslikemax", "feelslikemin", "feelslike",
        "name", "preciptype", "precipprob", "precipcover", "snow",
        "winddir", "severerisk", "sunrise", "sunset", "moonphase",
        "conditions", "description", "icon", "stations"
    ])
    df['datetime'] = pd.to_datetime(df['datetime'])
    
    dfs.append(df)
    progress.update()
progress.close()

# Combine all dataframes
combined_df = pd.concat(dfs, ignore_index=True)

# Sort the combined dataframe by date
combined_df = combined_df.sort_values('datetime')

# Reset the index
combined_df = combined_df.reset_index(drop=True)

# Save the ride counts to a new CSV file
combined_df.to_csv(output_file, index=False)

print(f"Combined datasets. Saved as {output_file}")