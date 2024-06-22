"""
This Python program combines all the datasets I've collected from the Divvy Database under the folder 'divvy_tripdata'
and count the rides for each day.

If you would like to download datasets from the Divvy Bicycles database, please collect from:
https://divvybikes.com/system-data
"""

import pandas as pd
import glob
import os
from tqdm import tqdm

directory_path = "./divvy_tripdata"
output_file = "divvy_tripdata.csv"

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

    df['started_at'] = pd.to_datetime(df['started_at'])
    
    dfs.append(df)
    progress.update()
progress.close()

# Combine all dataframes
combined_df = pd.concat(dfs, ignore_index=True)

# Sort the combined dataframe by date
combined_df = combined_df.sort_values('started_at')

# Reset the index
combined_df = combined_df.reset_index(drop=True)

# Count the number of rides for each day
counted_df = combined_df.groupby(combined_df['started_at'].dt.date).size().reset_index(name='ride_count')

# Save the ride counts to a new CSV file
counted_df.to_csv(output_file, index=False)

print(f"Combined and counted datasets. Saved as {output_file}")