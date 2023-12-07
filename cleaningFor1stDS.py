import pandas as pd
# Load the data into a DataFrame
file_path = 'mpo_nafo_bottomtrawl_event_1970-2019.csv'
df = pd.read_csv(file_path)

# Check the first few rows of the DataFrame to understand its structure
df.head()

# Define a function to count the decimal places
def count_decimals(number):
    # Make sure the number is a string and split by the decimal point
    parts = str(number).split('.')
    # If there is a decimal part, count the number of digits
    return len(parts[1]) if len(parts) > 1 else 0

# Apply the function to count the decimals for latitude and longitude
df['lat_decimals'] = df['decimalLatitude'].apply(count_decimals)
df['lon_decimals'] = df['decimalLongitude'].apply(count_decimals)

# Sort the DataFrame based on the rules provided:
# 1. eventID
# 2. Number of decimal places in decimalLatitude, descending
# 3. Number of decimal places in decimalLongitude, descending
df_sorted = df.sort_values(by=['eventID', 'lat_decimals', 'lon_decimals'], ascending=[True, False, False])

# Drop duplicates based on eventID, keeping the first (which, due to the sorting, will be the one with the most decimal places for latitude or longitude)
df_unique = df_sorted.drop_duplicates(subset='eventID', keep='first')

# Drop the auxiliary columns used for sorting
df_unique = df_unique.drop(columns=['lat_decimals', 'lon_decimals'])

# Display the first few rows of the resulting DataFrame to verify the correct rows are kept
print(df_unique.head())
df_unique.to_csv('adjust_mpo_nafo_bottomtrawl_event_1970-2019.csv')
