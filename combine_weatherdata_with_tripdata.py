"""
This Python program combines both the combined Divvy Bicycle Dataset and the combined Visual Crossing Weather Dataset.
"""

import pandas as pd


divvy_tripdata_df = pd.read_csv("divvy_tripdata.csv")
chicago_weatherdata_df = pd.read_csv("chicago_weatherdata.csv")

divvy_tripdata_df["started_at"] = pd.to_datetime(divvy_tripdata_df["started_at"])
chicago_weatherdata_df["datetime"] = pd.to_datetime(chicago_weatherdata_df["datetime"])

bike_sharing_df = pd.merge(chicago_weatherdata_df, divvy_tripdata_df, left_on='datetime', right_on='started_at', how='outer')

# Remove unnecessary 'started_at'
bike_sharing_df = bike_sharing_df.drop(columns=["started_at"])

# Remove index column to make it a proper bike rental dataset and save it
bike_sharing_df.to_csv("divvy_bike_rental.csv", index=False)