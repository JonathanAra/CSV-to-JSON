import csv
import json

# Read the CSV and add the data to a dictionary
csv_file_path = 'datagym.csv'
json_file_path = 'jsondata.json'

data = []
with open(csv_file_path) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for row in csvReader:
        data.append(row)

# Write the data to a JSON file
with open(json_file_path, 'w') as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))