
# ECOR 1042 Lab 6 - Template submission for histogram

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Ajan Balaganesh, Thomas Birnie-Wortley, Anusha Shah, Arianne Beauchesne"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "NA"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-110"

#==========================================#
# Place your histogram function after this line
import matplotlib.pyplot as plt
def histogram(given_lst: list[dict], attribute: str) -> float:
    """Returns a histogram that displays the amounts of dictionaries with a certain attribute in a certain range. The function will return the max attribute if the attribute specified is numerical but will return -1 if the attribute specified is categorical.
    Precondition: All the dictionaries in the list of dictionaries have the same keys in the same order and the attribute provided must be a key in all the dictionaries.
    >>>histogram([{'Occupation': 'H', 'Health': 20}, {'Occupation': 'H', 'Health': 25}], 'Health')
    [Histogram Displayed]
    25
    >>>histogram([{'Occupation': 'H', 'Health': 20}, {'Occupation': 'H', 'Health': 25}], 'Occupation')
    [Histogram Displayed]
    -1
    >>>>>>histogram([{'Occupation': 'EB', 'Health': 21.5}, {'Occupation': 'EB 'Health': 19.1}], 'Health')
    [Histogram Displayed]
    21.5
    """
    count = {}
    lst_values = []
    for item in given_lst:
        lst_values.append(item[attribute])
        
    
    if isinstance(given_lst[0][attribute], int) or isinstance(given_lst[0][attribute], float):
        range_val = max(lst_values) / 20
        last_val = max(lst_values)
        for i in range (20):
            counter = 0
            for item in lst_values:
                if i * range_val <= item <= (i + 1) * range_val:
                    counter += 1
                count[str(int(i * range_val)) + " to " + str(int((i+1) * range_val))] = counter
    else:
        for i in range (len(lst_values)):
            count[lst_values[i]] = lst_values.count(lst_values[i])
        last_val = -1
        
             
    
    fig1 = plt.figure()
    plt.title(attribute + "s")
    plt.xlabel(attribute + " Ranges")
    plt.ylabel("Amount of Values")
    plt.bar(count.keys(), count.values(), color = "red")
    plt.show()
    
    return last_val
            
    

# Do NOT include a main script in your submission
