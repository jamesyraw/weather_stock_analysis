import os
import pandas as pd

# The stock data exists as individual tickers. I'd rather interact with it all as one dataset, so I will first be merge all of them together.

input_directory = "C:\\Users\\James.Seelig\\Downloads\\archive\\stocks"  # The location of the source data
output_file = "master_stock_data.csv"  # The resulting output

# Creating an empty data frame to hold the new file 
merged_data = pd.DataFrame()

# Get a list of all CSV files in the directory
csv_files = [file for file in os.listdir(input_directory) if file.endswith(".csv")]
total_files = len(csv_files)

print(f"Found {total_files} CSV files to process...")

# Loop through all files in the directory with progress tracking
for index, file_name in enumerate(csv_files, start=1):
    file_path = os.path.join(input_directory, file_name)
    # Read the CSV file into a DataFrame
    data = pd.read_csv(file_path)
    # Add a column to identify the stock from the filename (optional)
    data['Stock'] = os.path.splitext(file_name)[0]
    # Append the data to the merged DataFrame
    merged_data = pd.concat([merged_data, data], ignore_index=True)
    
    # Print progress
    print(f"Processed {index}/{total_files} files: {file_name}")

# Save the merged DataFrame to a new CSV file
merged_data.to_csv(output_file, index=False)

# Give feedback that the task has completed
print(f"All files have been merged into {output_file}")