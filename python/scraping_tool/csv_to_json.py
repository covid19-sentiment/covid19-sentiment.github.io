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
        key = row['state']
        sentimen_value = float(row['sentimentVal'])
        if sentimen_value > 0: 
            if sentimen_value < 0.5:
                row['fillKey'] = "weak positive"
            else:
                row['fillKey'] = "strong positive"
        elif sentimen_value < 0:
            if sentimen_value > -0.5:
                row['fillKey'] = "weak negative"
            else:
                row['fillKey'] = "strong negative"
        else: 
            row['fillKey'] = "neutral"
        # fill_key = round(float(row['Sentiment_value']), 1)
        # row['fillKey'] = str(fill_key)
        data[key] = row


with open('data/state_sentiment_example3.json', 'w') as jsonFile:
    jsonFile.write(json.dumps(data, indent=3))
