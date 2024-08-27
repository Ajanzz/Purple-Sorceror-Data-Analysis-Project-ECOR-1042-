# ECOR 1042 Lab 6 - Template text UI
# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Ajan Balaganesh, Thomas Birnie-Wortley, Anusha Shah, Arianne Beauchesne"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "NA"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-110"

#==========================================#
# Place your script for your text_UI after this line
from load_data import *
from sort import *
from histogram import *
from curve_fit import *

exited = False
restart = True
escape = False
loading = "Incomplete / Nothing was loaded"

while restart:

    while escape == False:  # Using this to restart the program at the start/re-display the UI
        print("The available commands are:")
        print("   L)oad Data")
        print("   S)ort Data")
        print("   C)urve Fit")
        print("   H)istogram")
        print("   E)xit")
        select_command = input("Please type your command:")

    # Code for the Load Data command

        if select_command.lower() == "l":

            try:
                file = input("Please enter the name of the file:")
                input_file = open(file, "r")
                attribute = input("Please enter the attribute to use as a filter:")

                while attribute.lower() not in ['weapon', 'occupation', 'strength', 'luck', "all"]:
                    attribute= input("Invalid attribute, please enter another one.")
                if attribute.lower() != 'all':
                    value = input("Please enter the value of the attribute.")

                if attribute.lower() == 'occupation':
                    loading = load_data(file, ('Occupation', value.upper()))
                    data = calculate_health(loading)
                elif attribute.lower() == 'strength':
                    loading = load_data(file, ('Strength', float(value)))
                    data = loading
                elif attribute.lower() == "luck":
                    loading = load_data(file, ('Luck', float(value)))
                    data = loading
                elif attribute.lower() == "weapon":
                    loading = load_data(file, ('Weapon', value[0].upper() + value[1:].lower()))
                    data = calculate_health(loading)
                else:
                    loading = load_data(file, ('All', ''))
                    data = calculate_health(loading)
                
                
                print("Data loaded")

                escape = True

            except FileNotFoundError:
                print("File not found.")
                escape = True

    # Code for the Sort Data command

        elif select_command.lower() == "s":  # Code for the Sort Data command
            
            
            if loading == "Incomplete / Nothing was loaded":
                print("File not loaded. Please, load a file first.")
                break
                ##escape = True
            ##else:
            sort_attribute = input("Please enter the attribute to use for sorting:")
            while sort_attribute.lower() not in ['armor', 'agility', 'intelligence', 'health']:
                sort_attribute = input("Please enter another attribute.")            

            if sort_attribute == "armor":
                sort_attribute = "Armor"
            elif sort_attribute == "agility":
                sort_attribute = "Agility"
            elif sort_attribute == "intelligence":
                sort_attribute = "Intelligence"
            elif sort_attribute == "health":
                sort_attribute = "Health"
            
            

            order = input("Ascending (A) or Descending (D) order:")

            if order.lower() != "a" and order.lower() != "d":
                print("Invalid command")
                escape = True

            sorting = sort(data, order.upper(), sort_attribute)
            display = input("Data sorted. Do you want to display the data?")

            if display.upper() == 'Y':
                print(sorting)
            elif display.upper() == 'N':
                pass
            else:
                print("Invalid command.")
                escape = True
           

    # Code for the Curve Fit command

        elif select_command.lower() == "c":

            if loading == "Incomplete / Nothing was loaded":
                print("File not loaded. Please, load a file first.")
                escape = True
            else:
                attribute_curve = input(
                    "Please enter the attribute you want to use to find the best fit for Health:")

                while attribute_curve.lower() not in ['strength', 'agility', 'luck', 'armor', 'personality', 'intelligence', 'stamina']:
                    print("Invalid command.")
                    attribute_curve = input ("Select a valid attribute")
                
                order_polynomial = input("Please enter the order of the polynomial to be fitted:")
                try:
                    int_order_polynomial = int(order_polynomial)
                        # So only the first letter of the word is capitalized
                    attribute_curve = attribute_curve[0].upper() + attribute_curve[1:].lower()
                    curve_fit_result = curve_fit(data, attribute_curve, int_order_polynomial)
                    print(curve_fit_result)
                except:
                    print("Invalid command.")
                    escape = True

        elif select_command.lower() == "h":  # Code for the Histogram command

            if loading == "Incomplete / Nothing was loaded":
                print("File not loaded. Please, load a file first.")
                escape = True
            else:
                attribute_hist = input("Please enter the attribute you want to use for plotting:")
                while attribute_hist not in ['strength', 'agility', 'luck', 'armor', 'personality', 'intelligence', 'stamina']:
                    attribute_hist = input("Please reenter the attribute")
                try:
                    # So only the first letter of the word is capitalized
                    attribute_hist = attribute_hist[0].upper() + attribute_hist[1:].lower()
                    hist = histogram(data, attribute_hist)
                    print(hist)
                except:
                    print("Invalid command.")

                escape = True

        elif select_command.lower() == "e":  # Code for the Exit command
            restart = False
            exited = True
            break

        else:
            print("Invalid command.")
            escape = True

    escape = False
    
    if exited:
        print("Thanks for playing, goodbye! ")
