from datetime import date, timedelta, datetime
import csv
from tabulate import tabulate
import re
import sys



today = date.today()
today =today.strftime("%Y/%m/%d")
def main():
    """
    Creates a diary file if a user doesn't have one yet or open the existing one and gets the variables for making an observation for this day.

    :param :
    :type of input :
    :raise FileNotFoundError: If there is no a csv file.
    :return:
    :rtype:
    """
    print()
    print('WELCOME TO SEDOXIL DIARY!   We need to make some observations !\n')
    f=open("diary.csv")
    csv_list_of_dicts = [row for row in csv.DictReader(f)]
    if len(csv_list_of_dicts) == 0:
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
            list_of_diaries=[row for row in csv.DictReader(f)]
            starting_date, days_of_treatment = list_of_diaries[0]["starting_date"],int(list_of_diaries[0]["days_of_treatment"])
            #print (starting_date, days_of_treatment)
            for daynote in list_of_diaries:
                date_today = daynote["date_today"]
                if date_today == today:
                    print('You have already filled for today! Enjoy!')
                    sys.exit(0)


    newdaynote = fill_for_theday(starting_date, today, days_of_treatment)
    fill_daynote(newdaynote)

def get_days_of_treatment():
    """
    Receives from the user the duration of the treatment.

    :param : Gets the user's input
    :type of input: int (expected)
    :raise ValueError: If user's input is not an int < 100
    :return: A number of day for treatment
    :rtype: int
    """
    while True:
        try:
            howlong = input("How many do days you need to take a treatment? ")
            print()
            matches = re.search(r"^([0-9]{1,2})$", howlong) #re looks in an input for desimals up to two numbers
            if matches: # if it finds, it convert this to int and saves in a variable
                days_of_treatment = int(matches.group(1))
            else:
                raise ValueError
        except ValueError:
                print("The duration is not recognized, please use the decimal numbers < 100\n")
        else:
            break
    return days_of_treatment


def get_starting_day():
    """
    Receives from the user the date she/he started the treatment.

    :param : Gets the user's input
    :type n: str
    :raise ValueError: If an input doesn't look like a valid date and :raise TypeError: if date is in futere.
    :return: A string of a date like YYYY/MM/DD
    :rtype: str
    """
    while True:  # getting from a user a date of starting the treatment.
        try:
            starting_date = input("What was the date you started to take Sedoxil?(MM/DD): 2023/ ").strip()
            matches = re.search(r"^([0-9]{1,2})\D+([0-9]{1,2}$)", starting_date)
            if matches:
                if (int(matches.group(1))>12) or (int(matches.group(2))> 31):
                    raise ValueError
                starting_date = ('2023/' + str(matches.group(1)) + '/' + str(matches.group(2)))

                if start_date > now_date:
                    raise TypeError
            else:
                raise ValueError
        except ValueError:
            print()
            print("The date is not recognized, please use the decimal numbers up to 12 for months and up to 31 for days \n")
        except TypeError:
            print()
            print("You wrote the date in the future as the starting date, but you can't start the diary about the future! :) Sorry \n")
        else:
            break
    return starting_date




def progress(starting_date, today, days_of_treatment):
    """
    Gets a progress in the timeline of treatment.

    :param n: the day of starting the treatment and duration
    :type n: str and int
    :raise TypeError: If n is not a str or an int
    :return: the day of treatment and how many day left.
    :rtype: int or False
    """
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
    """
    Provides a user a questionnaire to fill the day observations and saves it in a dictionary.

    :param n: Number of times to meow
    :type n: int
    :raise ValueError: If the user input is not in the range of the expected response
    :return: A string of n meows, one per line
    :rtype: dictionary
    """
    date_today = date
    print()
    Nday_of_treatment,days_of_treatment_left  = progress(starting_date, date_today, days_of_treatment)
    printreport = False
    if days_of_treatment_left == 0:
        print("Congrats! Today is your last day of treatment and we will print the report! :)")
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
    """
    Fills the row in a diary csv file with day observations.

    :param n: dictionary
    :type n: dict
    :raise FileNotFoundError: If there is no a csv file.
    :return:
    :rtype:
    """
    with open ("diary.csv", "a+", newline='') as f:
       writer = csv.DictWriter(f, fieldnames=["date_today", "starting_date", "days_of_treatment","Nday_of_treatment","days_of_treatment_left",
                                              "sleep_state","morning_state","morning_pill","second_pill_time","time_reason_for2pill", "printreport"])
       writer.writerow(newdaynote)

    if newdaynote["printreport"] == True: # print final report roe a docto in a separete csv file.
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
    """
    Finds the gap dates(unfilled) in diary and creates the empty dictionary for the empty line in a doctor report.
    :param n: Starting date of treatment, number of days for treatment.
    :type n: str, int
    :raise FileNotFoundError: If there is no a csv file.
    :return: A string of n meows, one per line
    :rtype: list of dictionaries with empty perorts for that days.
    """
    with open("diary.csv") as f:
        dates = [row["date_today"] for row in csv.DictReader(f)]   # creates a list of dates whith the observations were completed.

    #print(f'dates filled in diary - {dates}')


    start= datetime.strptime(starting_date,"%Y/%m/%d")  #converts the first day of treatment into timedate format as it comes as str.

    list_of_dates_to_fill=[(start + timedelta(days = i)).strftime("%Y/%m/%d") for i in range( days_of_treatment)] # creates a list of all dates during the
                                                                                                                   #treatment period in str format(.strftime("%Y/%m/%d"))
    #print(f'list_of_dates_to_fill {list_of_dates_to_fill}')


    gap_dates = [date for date in list_of_dates_to_fill if date not in dates] #creates the list af dates when the ovservations were not made.

    #print(f'gap_dates {gap_dates}')


    gap_reports=[{"date_today" : date, "starting_date":'-',"days_of_treatment": '-',"Nday_of_treatment":'-', "days_of_treatment_left":'-', "sleep_state": '-',
             "morning_state":'-', "morning_pill":'-', "second_pill_time":'-', "time_reason_for2pill":'-',"printreport": False} for date in gap_dates]
    #create unfilled day observations with a sertain date.
    return gap_reports

def print_report_for_a_doctor():
    """
    Creates a final report for a doctor for the whole treatment period including unfilled dates.

    :param n: no
    :type n:
    :raise FileNotFoundError: If there is no a csv file.
    :return:
    :rtype:
    """

    with open("diary.csv") as f:
        reports = [row for row in csv.DictReader(f)]  #gets the information for filled days

    starting_date, days_of_treatment = reports[0]['starting_date'], int(reports[0]['days_of_treatment'])     #retrieves the arguments for fill_empty function.
    gap_reports= fill_empty(starting_date, days_of_treatment)  #creates missed reports.

    wholereport = sorted((reports+gap_reports), key=lambda daynote: daynote["date_today"])              #combines reports together sorted by date.


    with open ("doctor_report.csv", "w", newline='') as f:  # writes a doctor report
        for daynote in  wholereport:
            #print(daynote)
            writer = csv.DictWriter(f, fieldnames=["date_today","starting_date","days_of_treatment","Nday_of_treatment","days_of_treatment_left",
                                              "sleep_state","morning_state","morning_pill","second_pill_time","time_reason_for2pill","printreport"])
            writer.writerow(daynote)
    print(" Now you can see your treatment report in doctor_report.csv file. Thank you!")
def summary(newdaynote):
    """
    Shows in a simple table the information that was just provided and gives the user the chance to change it.

    :param n: dictionary with filled information about the day observation.
    :type n: dictionary
    :raise ValueError: If the user input is not in the range of the expected response
    :return:
    :rtype:
    """
    print(tabulate(newdaynote.items())) # draw a table with new day observation.
    print()
    while True:
        try:
            change_the_note  = input("Do you want to change you note? Type 'yes' or 'no' : ").strip().upper()
            if change_the_note in ['Y', 'Yes', 'OK']:
                fill_for_theday(newdaynote['starting_date'],newdaynote['date_today'],newdaynote['days_of_treatment'])

        except ValueError:
            print('ok')
        else:
           break

if __name__ == "__main__":
    main()
