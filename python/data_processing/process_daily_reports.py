import pandas as pd 
import csv

def read_daily_confirmed_cases(date,state_abbrs,state_to_abbr_mapping,data_type=0):
    df = pd.read_csv('../../../COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/' + date + '-2020.csv')
    data = {}
    for state in state_abbrs:
        data[state] = 0

    for col in df.columns:
        if 'country' in col.lower():
            cn_col = col
        elif 'state' in col.lower():
            st_col = col
    US_data = df[df[cn_col] == 'US']
    US_states_list = list(US_data[st_col])
    US_confirmed_list =  list(US_data['Confirmed'])
    for i in range(len(US_data[cn_col])):
        state_entry =  US_states_list[i]
        state_abbr = state_entry
        if data_type == 0:
            state_abbr = US_states_list[i][-2:]
        else:
            if state_entry in state_to_abbr_mapping:
                state_abbr = state_to_abbr_mapping[state_entry]
            # else:
            #     print("WHAT IS THIS",state_entry)
            #     data['Unknown'] = US_confirmed_list[i]
        if state_abbr in data.keys():
            data[state_abbr] +=  US_confirmed_list[i]
            # print('Update',data[state_abbr])
        else:
            found = False 
            for state in state_abbrs:
                if state in state_entry:
                    data[state] += US_confirmed_list[i]
                    # print('Update',data[state])
                    found = True
                    break
            if not found:
                print('Location', state_abbr, "cant't be found.")
                data['Unknown'] = US_confirmed_list[i]
    return data

def write_data_to_csv(filename,fieldnames,date,data_dict):
    
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if date == "03-01":
            writer.writeheader()
        data_dict['Date'] = date
        writer.writerow(data_dict)
        print(date,"written")

#this function calculates and writes weekly NEW confirmed cases to a csv
def write_new_cases_to_csv(start_date,duration,daily_csv_file,new_csv_file_dir,state_abbrs,fieldnames):
    df = pd.read_csv(daily_csv_file)
    start_row = 0
    data_dict = {}
    for i in range(len(df['Date'])):
        if df['Date'][i] == start_date:
            start_row = i
            break
    
    # duration = 0
    # try:
    #     duration = min(7,31 - int(start_date[-2:]))
    # except:
    #     ValueError
    #     duration = min(7,31 - int(start_date[-1:]))

    # actual_duration = min(duration,31 - int(start_date[-2:]) + 1)

    end_row = min(start_row + duration - 1,len(df['Date']) - 1)
    for abbr in state_abbrs:
        data_dict[abbr] = list(df[abbr])[end_row] - list(df[abbr])[start_row]
        # print(abbr,data_dict[abbr],start_row,end_row,list(df[abbr])[start_row],list(df[abbr])[end_row])
    data_dict['Unknown'] = list(df['Unknown'])[end_row] - list(df['Unknown'])[start_row]

    # if duration <= 2:
    #     timeframe = 'daily'
    # elif duration <= 7:
    #     timeframe = 'weekly'
    # else:
    #     timeframe = 'unknown'

    filename = new_csv_file_dir + 'covid_weekly_new_confirmed_cases_US_March.csv'
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if start_date == '03-01':
            writer.writeheader()
        data_dict['Start Date'] = start_date
        writer.writerow(data_dict)
        print(start_date,"written")


def main():
    state_df = pd.read_csv("state_to_abbr.csv")
    state_to_abbr_mapping = {}
    for i in range(len(state_df['State'])):
        state_to_abbr_mapping[state_df['State'][i]] = state_df['Abbreviation'][i]
    state_abbrs = list(state_df['Abbreviation'])
    # print(state_to_abbr_mapping)

    fieldnames = state_abbrs.copy()
    fieldnames.insert(0,'Date')
    fieldnames.append('Unknown')

    #You only want to run this section of code to get one csv file with
    #all the daily confirmed cases data in the US in March 
    # for i in range(1,10):
    #     date = "03-0" + str(i)
    #     data_dict = read_daily_confirmed_cases(date,state_abbrs,state_to_abbr_mapping,data_type=0)
    #     write_data_to_csv('result/covid_daily_confirmed_cases_US.csv',fieldnames,date,data_dict)
    # for j in range(10,32):
    #     date = "03-" + str(j)
    #     data_dict = read_daily_confirmed_cases(date,state_abbrs,state_to_abbr_mapping,data_type=1)
    #     write_data_to_csv('result/covid_daily_confirmed_cases_US.csv',fieldnames,date,data_dict)
    
    # fieldnames[0] = 'Start Date'
    # write_new_cases_to_csv('03-01',7,'result/covid_daily_confirmed_cases_US.csv','result/',state_abbrs,fieldnames)
    # for start_date in ['03-07','03-14','03-21','03-28']:
    #     write_new_cases_to_csv(start_date,8,'result/covid_daily_confirmed_cases_US.csv','result/',state_abbrs,fieldnames)
    
    fieldnames[0] = 'Start Date'
    write_new_cases_to_csv('03-01',1,'result/covid_daily_confirmed_cases_US.csv','result/',state_abbrs,fieldnames)
    for i in range(2,32):
        start_date = "03-0" + str(i) if i < 10 else "03-" + str(i)
        write_new_cases_to_csv(start_date,2,'result/covid_daily_confirmed_cases_US.csv','result/',state_abbrs,fieldnames)
    

if __name__ == "__main__":
    main()