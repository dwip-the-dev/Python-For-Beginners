import json

# Sample data (a Python dictionary)
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "isStudent": False,
    "courses": ["Math", "Science", "History"]
}

# Define the filename for the JSON output
json_filename = "output.json"

# Open the file in write mode ('w') and use json.dump() to write the data
try:
    with open(json_filename, 'w') as f:
        json.dump(data, f, indent=4) # indent=4 makes the JSON output human-readable
    print(f"Data successfully written to {json_filename}")
except IOError as e:
    print(f"Error writing to file: {e}")