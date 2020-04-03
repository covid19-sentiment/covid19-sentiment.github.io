"""
Converts csv files from scraping process to json files in an appropriate
format to be fed to map.
"""
import pandas as pd 
import csv, json

state_df = pd.read_csv("state_to_abbr.csv")
state_abbrs = list(state_df['Abbreviation'])

data = {}
df = pd.read_csv('result/covid_weekly_new_confirmed_cases_US_March.csv')
states = list(df.columns[1:])
for i in range(len(df['Start Date'])):
    # The States are used as keys for dictionary
    row = df.iloc[i,:]
   
    # fill_key = round(float(row['Sentiment_value']), 1)
    # row['fillKey'] = str(fill_key)
    for state in states:
        data_obj = {}
        data_obj['state'] = state
        new_cases = row[state]
        data_obj['newCases'] = str(new_cases)
        if new_cases > 0: 
            if new_cases < 10:
                data_obj['fillKey'] = "level_1"
            elif new_cases < 100:
                data_obj['fillKey'] = "level_2"
            elif new_cases < 1000:
                data_obj['fillKey'] = "level_3"
            elif new_cases < 10000:
                data_obj['fillKey'] = "level_4"
        else: 
            data_obj['fillKey'] = "level_0"
        data[state] = data_obj
    print(data)
    with open('result/state_new_cases_example_wk' + str(i + 1) + '.json', 'w') as jsonFile:
        jsonFile.write(json.dumps(data, indent=3))
