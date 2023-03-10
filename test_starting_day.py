import re
from datetime import date


#### TYPE DIFERENT INPUTS FOR TESTING.####


today = date.today()
today =today.strftime("%Y/%m/%d")
while True:  # getting from a user a date of starting the treatment.
    try:
        starting_date = input("What was the date you started to take Sedoxil?(MM/DD): 2023/ ").strip()
        matches = re.search(r"^([0-9]{1,2})\D*([0-9]{1,2}$)", starting_date)
        if matches:
            #print(f"matches.group(1){matches.group(1)},matches.group(2){matches.group(2)}" )

            if (int(matches.group(1)) > 12) or (int(matches.group(1)) < 0 ) and ((int(matches.group(2)) > 31) or (int(matches.group(2)) < 0)) :
                raise ValueError
            starting_date = ('2023/' + str(matches.group(1)) + '/' + str(matches.group(2)))

            if starting_date > today:
                raise TypeError
        else:
            raise ValueError

    except ValueError:
           print()
           print("The date is not recognized, please use the decimal numbers up to 12 for months and up to 31 for days and bigger than 0 :)\n")
    except TypeError:
           print()
           print("You wrote the date in the future as the starting date, but you can't start the diary about the future! :) Sorry \n")
    else:
        break
print (starting_date)
