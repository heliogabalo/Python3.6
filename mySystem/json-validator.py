import json

def validate_json(file_path):
    try:
        with open(file_path, 'r') as file:
            json.load(file)
        print("The JSON file is valid.")
    except json.JSONDecodeError as e:
        print(f"The JSON file is invalid: {e}")

# Usage
validate_json('your_file.json')
