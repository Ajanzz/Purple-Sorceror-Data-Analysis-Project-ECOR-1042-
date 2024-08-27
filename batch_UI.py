# ECOR 1042 Lab 6 - Template Individual submission for batch_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Ajan Balaganesh, Thomas Birnie-Wortley, Anusha Shah, Arianne Beauchesne"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "NA"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T110"

#==========================================#
# Place your script for your batch_UI after this line

from load_data import *
from sort import *
from curve_fit import *
from histogram import *

true = True

while true:
    try:
        file = input('Please enter the name of the file where your commands are stored: ')
        txtfile = open(file, "r")
        true = False

    except FileNotFoundError:
        true == True

for line in txtfile:
    line = line.strip()
    line = line.split(";")

    if line[0] == 'L':
        if line[2] == "Strength" or line[2] == "Luck":
            loaded_data = load_data(line[1], (line[2], float(line[3])))
            print('data loaded')
        else:
            loaded_data = calculate_health(load_data(line[1], (line[2], line[3])))
            print('data loaded')

    elif line[0] == 'S':
        if line[1] == 'Agility':
            data = sort_characters_agility_bubble(loaded_data, line[2])
            if line[3] == 'Y':
                print('Data sorted.')
                print(data)
            else:
                print('Data sorted.')

        elif line[1] == 'Intelligence':
            data = sort_characters_intelligence_selection(loaded_data, line[2])
            if line[3] == 'Y':
                print('Data sorted.')
                print(data)
            else:
                print('Data sorted.')

        elif line[1] == 'Health':
            data = sort_characters_health_insertion(loaded_data, line[2])
            if line[3] == 'Y':
                print('Data sorted.')
                print(data)
            else:
                print('Data sorted.')

        elif line[1] == 'Armor':
            data = sort_characters_armor_bubble(loaded_data, line[2])
            if line[3] == 'Y':
                print('Data sorted.')
                print(data)
            else:
                print('Data sorted.')

    elif line[0] == 'C':
        print(curve_fit(loaded_data, line[1], int(line[2])))

    elif line[0] == 'H':
        histogram(data, line[1])

    elif line[0] == 'E':
        break

txtfile.close()
