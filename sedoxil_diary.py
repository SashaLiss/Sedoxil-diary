from datetime import date, timedelta, datetime
import csv
from tabulate import tabulate
import re
import sys



today = date.today()
today =str(today.strftime("%Y/%m/%d"))

def main():
    print()
    print('WELCOME TO SEDOXIL DIARY!   We need to make some observations !\n')
    f=open("diary.csv")
    csv_dict = [row for row in csv.DictReader(f)]
    if len(csv_dict) == 0:
        print("You have not created a diary file for you yet. let's do it now!\n")
        f.close

        days_of_treatment = get_days_of_treatment()
        starting_date = get_starting_day()
        if progress(starting_date, today, days_of_treatment) == False :
            days_of_treatment = get_days_of_treatment()
            starting_date = get_starting_day()
        else:
            print("Have a nice trip!")
    else:
        with open("diary.csv") as f:
            reader = csv.DictReader(f)
            for row in reader:
                daynote = row
                starting_date = daynote["starting_date"]
                days_of_treatment = int(daynote["days_of_treatment"])
                date_today = daynote["date_today"]
                if date_today == today:
                    print('You already filled for today! Enjoy!')
                    sys.exit(0)


    newdaynote = fill_for_theday(starting_date, today, days_of_treatment)
    fill_daynote(newdaynote)

def get_days_of_treatment():
    while True:
        try:
            howlong = input("How many do days you need to take a treatment? ")
            print()
            matches = re.search(r"^([0-9]{1,2})$", howlong)
            if matches:
                days_of_treatment = int(matches.group(1))
            else:
                raise ValueError
        except ValueError:
                print("The duration is not recognized, please use the decimal numbers < 100\n")
        else:
            break
    return days_of_treatment


def get_starting_day():
    while True:  # getting from a user a date of starting the treatment.
        try:
            starting_date = input("What was the date you started to take Sedoxil?(MM/DD): 2023/ ").strip()
            print()
            matches = re.search(r"^([0-9]{1,2})\D+([0-9]{1,2}$)", starting_date)
            if matches:
                if (int(matches.group(1))>12) or (int(matches.group(2))> 31):
                    raise ValueError
                starting_date = ('2023/' + str(matches.group(1)) + '/' + str(matches.group(2)))
                print(type(starting_date))
                start_date = datetime.strptime(starting_date,"%Y/%m/%d")
                now_date = datetime.strptime(today,"%Y/%m/%d")
                if start_date > now_date:
                    #print(f"{start_date}>{now_date}")
                    raise ArithmeticErrorError
            else:
                raise ValueError
        except ValueError:
            print()
            print("The date is not recognized, please use the decimal numbers up to 12 for months and up to 31 for days \n")
        except ArithmeticError:
            print()
            print("You wrote the date in the future as the starting date, but you can't start the diary about the future! :) Sorry \n")
        else:
            break
    return starting_date




def progress(starting_date, today, days_of_treatment):
    start_date = datetime.strptime((starting_date),"%Y/%m/%d")
    now_date = datetime.strptime(today,"%Y/%m/%d")
    delta = now_date - start_date
    Nday_of_treatment = delta.days + 1
    if (Nday_of_treatment > days_of_treatment):
        print ("It looks like you already ended up the treatment "
             "according to the starting day or course duration shown. Please check your data\n")
        print(f"Acording to your information you started the course on {starting_date} and"
              "your treatment duration is {days_of_treatment} not {course_duration}!\n")
        print("Please fix the info!\n")
        return False

    days_of_treatment_left = days_of_treatment - Nday_of_treatment
    return (Nday_of_treatment, days_of_treatment_left)

def fill_for_theday(starting_date, date, days_of_treatment):
    date_today = date
    print()
    Nday_of_treatment,days_of_treatment_left  = progress(starting_date, date_today, days_of_treatment)
    printreport = False
    if days_of_treatment_left == 1:
        print("Congrats! Today is yout last day of treatment and we will prill the report! :)")
        printreport = True
    print()
    print (f"So, on {date_today} it's your {Nday_of_treatment} day of taking Sedoxil. You have {days_of_treatment_left} days left.\n")

    print("HOW WAS YOUR SLEEP?")
    print("-------------------")
    sleep_report={
        "A" : ("Didn't sleep"),
        "B" : ("Woke up several times during the night"),
        "C" : ("Just couple of hours"),
        "D" : ("Sleeping was restless"),
        "E" : ("Was good but not enough")
    }
    for key,value in sleep_report.items():
        print (f"{key} - {value}")
    print()
    while True:  # getting from a user his feedback about night sleep.
        try:
            s_r_letter = input("Choose and print the key-letter to indicate your sleep: ").strip().upper()
            if s_r_letter in ['A', 'B', 'C', 'D', 'E']:
                sleep_state = sleep_report[s_r_letter]
                print()
            else:
                raise ValueError
        except ValueError:
            print("You chose the option that doesnt exist. Try again, please: ")
        else:
            break

    print('HOW DID YOU FIND YOURSELF IN THE MORNING?')
    print("-----------------------------------------")
    morningstate={
        "T": "Tired",
        "D": "Depressed",
        "S": "Sleepy",
        "R": "Rested",
        "F": "Full of energy",
        "C": "Calm",
        "U": "Uneasy",
        "A": "Aloof"
    }
    for key,value in morningstate.items():
        print (f"{key} - {value}")
    print()

    while True:  # getting from a user his feedback about his morning experience.
        try:
            morst_letter = input("Choose and print the letter to indicate your state in the morning: ").strip().upper()
            if morst_letter in ['T', 'D', 'S', 'R', 'F','C','U','A']:
                morning_state = morningstate[morst_letter]
                print()
            else:
                raise ValueError
        except ValueError:
            print("You chose the option that doesnt exist. Try again, please: ")
            print()
        else:
            break

    while True:
        try:
            morning_pill = input("Did you take the morning pill? type 'Yes' or 'No': " ).strip().upper()
            print()
            if  morning_pill in ('Y', 'YES'):
                morning_pill = 'YES'
            elif morning_pill in ('N', 'No'):
                morning_pill = 'No'
            else:
                raise ValueError

            second_pill_time = input("When do you decide to take the second pill? type 'A' for afternoon  and 'E' for evening: ").strip().upper()
            print()
            if second_pill_time in ('A', 'AFTERNOON'):
                second_pill_time = 'AFTERNOON'
            elif  second_pill_time in ('E', 'EVENING'):
                 second_pill_time = 'EVENING'

            else:
                raise TypeError

        except ValueError:
            print("You chose the option that doesnt exist. Try again, please: ")
            print()
        except TypeError:
            print("You chose the option that doesnt exist. Try again, please: ")
            print()
        else:
            break

    time_reason_for2pill = input('Why do you decide the take second pill this time: ? ').strip()
    print()


    newdaynote = {
        "date_today":date_today,
        "starting_date":starting_date,
        "days_of_treatment":days_of_treatment,
        "Nday_of_treatment":Nday_of_treatment,
        "days_of_treatment_left":days_of_treatment_left,
        "sleep_state":sleep_state,
        "morning_state":morning_state,
        "morning_pill":morning_pill,
        "second_pill_time": second_pill_time,
        "time_reason_for2pill":time_reason_for2pill,
        "printreport": printreport
    }

    while True:
        try:
            check_the_note = input('Do you want to see the summary for this day? Type Y or N: ').strip().upper()
            print()
            if  check_the_note in ('Y', 'Yes', 'Ok'):
                summary(newdaynote)
            elif check_the_note in ('N', 'NO', 'NOPE'):
                 print("ok")
            else:
                raise ValueError
        except ValueError:
            print ("You typed smth stupid :) Try again please.")
        else:
            break

    return (newdaynote)

def fill_daynote(newdaynote):
    with open ("diary.csv", "a+", newline='') as f:
       writer = csv.DictWriter(f, fieldnames=["date_today", "starting_date", "days_of_treatment","Nday_of_treatment","days_of_treatment_left",
                                              "sleep_state","morning_state","morning_pill","second_pill_time","time_reason_for2pill", "printreport"])
       writer.writerow(newdaynote)

    if newdaynote["printreport"] == True: # printreport
        print()
        print(f"Thank for filling information for the day {newdaynote['date_today']}. Now it's recorded in your file. "
          "It's you last day of treatment and we print a report for your doctor. You can find it in the same directory named doctor_report.csv \n")
        print_report_for_a_doctor()
    else:
        print()
        print(f"Thank for filling information for the day {newdaynote['date_today']}. Now it's recorded in your file. "
          "At the end of the treatment you can print it for your doctor. \n")
        while True:
            try:
                want_to_see_a_report = input("But if you want to see an unfinished report already, you are welcome:"
                                "You can find it in the same directory named doctor_report.csv."
                                "Print a report? Type 'Y' or 'N': " ).strip().upper()
                if want_to_see_a_report in ['Y', 'YES', 'OK']:
                    print_report_for_a_doctor()
                elif want_to_see_a_report in ['N', 'NO', 'NOPE']:
                    print('Ok, Enjoy your day!')
                else:
                    raise ValueError
            except ValueError:
                 print("You typed smth stupid")
            else:
                break


def fill_empty(starting_date, days_of_treatment):
    dates=[]
    with open("diary.csv") as f:
            reader = csv.DictReader(f)
            for row in reader:
                date = row["date_today"]
                dates.append(date)
    print(f'dates filled in diary - {dates}')

    start= datetime.strptime(starting_date,"%Y/%m/%d")
    list_of_dates= []
    for i in range( days_of_treatment +1):
        next_day = start + timedelta(days = i)
        list_of_dates.append(str(next_day).strip('00:00:00').strip())
    print(f'the period  of dates to fill {list_of_dates}')

    gap_dates=[]
    for date in list_of_dates:
        if date not in dates:
            gap_dates.append(date)
    print(gap_dates)

    gap_reports=[]
    for date in gap_dates:
        missed_daynote = {}
        missed_daynote["date_today"] = date
        missed_daynote["starting_date"]='-'
        missed_daynote["days_of_treatment"]='-'
        missed_daynote["Nday_of_treatment"]='-'
        missed_daynote["days_of_treatment_left"]='-'
        missed_daynote["sleep_state"]='-'
        missed_daynote["morning_state"]='-'
        missed_daynote["morning_pill"]='-'
        missed_daynote["second_pill_time"]='-'
        missed_daynote["time_reason_for2pill"]= '-'
        missed_daynote["printreport"] = False
        gap_reports.append(missed_daynote)
    #print (gap_reports)
    return gap_reports

def print_report_for_a_doctor():
    reports=[]
    with open("diary.csv") as f:
            reader = csv.DictReader(f)
            for row in reader:
                daynote = row
                reports.append(daynote)
    starting_date, days_of_treatment = reports[0]['starting_date'], reports[0]['days_of_treatment']
    gap_reports= fill_empty(starting_date, days_of_treatment)
    wholereport= (reports+gap_reports)
    #print (wholereport)
    wholereport = sorted(wholereport, key=lambda daynote: daynote["date_today"])
    #print (wholereport)

    for daynote in  wholereport:
        with open ("doctor_report.csv", "a+", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["date_today","starting_date","days_of_treatment","Nday_of_treatment","days_of_treatment_left",
                                              "sleep_state","morning_state","morning_pill","second_pill_time","time_reason_for2pill","printreport"])
            writer.writerow(daynote)

def summary(newdaynote):

        print(tabulate(newdaynote.items()))
        print()
        starting_date = newdaynote['starting_date']
        days_of_treatment= newdaynote['days_of_treatment']
        date_today = newdaynote['date_today']
        change_the_note  = input("Do you want to change you note? Type 'yes' or 'no' : ").strip().upper()
        if change_the_note in ['Y', 'Yes', 'OK']:
                fill_for_theday(starting_date,date_today,days_of_treatment,)

if __name__ == "__main__":
    main()