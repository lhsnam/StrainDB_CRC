import glob
import pandas as pd

# Get a list of all CSV files in the current directory
csv_files = glob.glob("*.csv")

# Create an empty DataFrame to hold the results
result_df = pd.DataFrame()

# Loop through each CSV file
for file in csv_files:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file)

    # Check if 'name' column exists
    if 'name' in df.columns:
        # Filter rows where 'name' contains 'Fusobacterium'
        filtered_rows = df[df['name'].str.contains("Fusobacterium", na=False)]

        # Determine the 'database' value based on the file name
        if "reps" in file.lower():
            filtered_rows['database'] = "rs214_reps_only"
        elif "fuso" in file.lower():
            filtered_rows['database'] = "rs214_fuso"
        else:
            filtered_rows['database'] = "rs214_only"  # Default value

        # Append the filtered rows to the result DataFrame
        result_df = pd.concat([result_df, filtered_rows], ignore_index=True)

# Check if there are any results to write
if not result_df.empty:
    # Write the result DataFrame to a new CSV file
    result_df.to_csv("filtered_fusobacterium.csv", index=False)
    print("Filtered results saved to 'filtered_fusobacterium.csv'")
else:
    print("No rows found containing 'Fusobacterium'.")
