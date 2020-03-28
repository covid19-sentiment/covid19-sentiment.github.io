"""
Converts csv files from scraping process to json files in an appropriate
format to be fed to map.
"""

import csv, json

data = {}
with open('data/state_sentiment_example2.csv', 'r') as csvFile:
    csvReader = csv.DictReader(csvFile)
    for row in csvReader:
        # The States are used as keys for dictionary
        key = row['State']
        fill_key = round(float(row['Sentiment_value']), 1)
        row['fillKey'] = str(fill_key)
        data[key] = row


with open('data/state_sentiment_example2.json', 'w') as jsonFile:
    jsonFile.write(json.dumps(data, indent=3))
