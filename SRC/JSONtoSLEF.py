import json
import sys

def json_to_slef(json_data):
    slef_data = []

    for entry in json_data:
        slef_entry = {
            "header": {
                "appName": "Inara",
                "appVersion": "1.0",
                "appURL": entry['header']['appURL'],
                "appCustomProperties": {
                    "anything": "here"
                }
            },
            "data": {
                "Ship": entry['data']['Ship'],
                "Modules": []
            }
        }

        for module in entry['data']['Modules']:
            slef_module = {
                "Slot": module['Slot'],
                "Item": module['Item']
            }
            if 'Engineering' in module:
                slef_module['Engineering'] = module['Engineering']
            slef_entry['data']['Modules'].append(slef_module)

        slef_data.append(slef_entry)

    return slef_data

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python converter.py <input_json_file>")
        sys.exit(1)

    input_json_file = sys.argv[1]

    try:
        with open(input_json_file, "r") as file:
            json_data = json.load(file)
    except FileNotFoundError:
        print("File not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print("Invalid JSON format in the file.")
        sys.exit(1)

    slef_data = json_to_slef(json_data)
    print(json.dumps(slef_data, indent=4))
