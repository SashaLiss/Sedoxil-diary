from datetime import date, timedelta, datetime
import csv



date_s = '2023/02/26'            #type different dates  and duration fo testing
dur = 8


with open("diary.csv") as f:
    dates = [row["date_today"] for row in csv.DictReader(f)]
    #print(f'new way{dates}')

start= datetime.strptime(date_s,"%Y/%m/%d")

list_of_dates_to_fill=[(start + timedelta(days = i)).strftime("%Y/%m/%d") for i in range( dur)]

print(f'list_of_dates_to_fill {list_of_dates_to_fill}')

gap_dates = [date for date in list_of_dates_to_fill if date not in dates]
print(f'gap_dates {gap_dates}')

gap_reports=[{"date_today" : date, "starting_date":'-',"days_of_treatment": '-',"Nday_of_treatment":'-', "days_of_treatment_left":'-', "sleep_state": '-',
                "morning_state":'-', "morning_pill":'-', "second_pill_time":'-', "time_reason_for2pill":'-',"printreport": False} for date in gap_dates]

print (gap_reports)


