import json

# Assuming you have a JSON file named 'data.json' in the same directory
# with content like:
# {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York"
# }

try:
    with open('data.json', 'r') as file:
        # Use json.load() to parse the JSON data from the file object
        data = json.load(file)

    print("JSON data loaded successfully:")
    print(data)
    print(f"Name: {data['name']}")
    print(f"Age: {data['age']}")
    print(f"City: {data['city']}")

except FileNotFoundError:
    print("Error: 'data.json' not found. Please ensure the file exists.")
except json.JSONDecodeError:
    print("Error: Could not decode JSON from 'data.json'. Check file format.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")