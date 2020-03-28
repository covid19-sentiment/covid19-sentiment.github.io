"""
Converts csv files from scraping process to json files in an appropriate
format to be fed to map.
"""

import csv, json

data = {}
with open('data/state_sentiment_example.csv', 'r') as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        # The States are used as keys for dictionary
        key = rows['State']
        data[key] = rows

with open('data/state_sentiment_example.json', 'w') as jsonFile:
    jsonFile.write(json.dumps(data, indent=3))
