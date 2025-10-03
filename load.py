import csv  # to read the CSV files

def load_wind_data(filepath, country_column):
    # Open the CSV file
    file = open(filepath, 'r')
    
    # Create a CSV reader 
    reader = csv.DictReader(file)
    
    # Create empty lists to import data
    timestamps = []  # to store times
    values = []      # to store power values
    
    # Get the name of the first column
    first_column = reader.fieldnames[0]
    
    # Loop through each row in the CSV
    for row in reader:
        # Get the timestamp from the first column
        timestamp = row[first_column]
        timestamps.append(timestamp)
        
        # Try to get the wind value for the country
        if country_column in row and row[country_column] != '':
            wind_value = float(row[country_column])
        else:
            wind_value = 0.0 # Use zero if the box doesn't contain a value
        
        values.append(wind_value)
    
    # Close the file
    file.close()
    
    # Return the lists
    return timestamps, values