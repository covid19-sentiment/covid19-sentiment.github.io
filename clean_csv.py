import csv

all_rows = []

state_names = {'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', \
'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', \
'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', \
'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', \
'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'}

state_abbrevs = {'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut', \
'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia', 'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa', 'KS': 'Kansas', \
'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland', 'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi', \
'MO': 'Missouri', 'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico', 'NY': 'New York', \
'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio', 'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina', \
'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont', 'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia', \
'WI': 'Wisconsin', 'WY': 'Wyoming'}

# replace file with .csv you are reading from
with open('/Users/eunjilee/Desktop/covid19-sentiment.github.io-master/python/scraping_tool/data/corona_tweets_small.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
	    if line_count == 0:
	        print(f'Column names are {", ".join(row)}')
	        line_count += 1
	    else:
	    	usable = False
	    	place_name = ''

	    	if row[5] != '':
	    		place_name = row[5]
	    		usable = True

	    	else:
	    		given_loc = row[0]
	    		for state_name in state_names:
	    			if given_loc.find(state_name) != -1:
	    				place_name = state_name
	    				usable = True
	    				break

	    		for state_abbrev in state_abbrevs.keys():
	    			if given_loc.find(state_abbrev) != -1:
	    				place_name = state_name
	    				usable = True
	    				break

	    	if usable:
	    		row = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], place_name]
	    		all_rows.append(row)

	    	line_count += 1

	print(f'Processed {line_count} lines.')

# replace file w .csv you are writing from
with open('/Users/eunjilee/Desktop/covid19-sentiment.github.io-master/python/scraping_tool/data/corona_tweets_cleaned.csv', mode = 'w') as csv_file:
	csv_writer = csv.writer(csv_file, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)

	for row in all_rows:
		csv_writer.writerow(row)

