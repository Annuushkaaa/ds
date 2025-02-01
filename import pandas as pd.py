import pandas as pd

# Create a dictionary of data
data = {
    'Name': ['John', 'Mary', 'Alice', 'Bob'],
    'Age': [25, 30, 22, 28],
    'Gender': ['Male', 'Female', 'Female', 'Male'],
    'Height': [5.9, 5.5, 5.6, 6.0]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save DataFrame to a CSV file
df.to_csv('healthex.csv', index=False)