import csv
import json

def convert_csv_to_json(csv_filename):
    try:
        data = []

        # Open the CSV file and read its contents
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data.append(row)

        # Write the JSON data to data.json
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False
    except Exception as e:
        # Optional: print(e) for debugging
        return False
