# ECOR 1042 Lab 6 - Template for curve_fit function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Ajan Balaganesh, Thomas Birnie-Wortley, Anusha Shah, Arianne Beauchesne"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "NA"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T110"

#==========================================#
# Place your curve_fit function after this line
def curve_fit(data_list: list[dict], attribute: str, degree: int) -> str:
    """
    Return a string containing the line of best fit for a given data set, with the specified attribute and degree of the polynomial given
    
    Preconditions: 
    - data_list is a list of dictionaries that all contain the "Health" attribute
    - attribute is a string containing the attribute that will be compared with the health values
    - degree is an integer that represents the chosen degree of the polynomial
    
    >>> curve_fit([{"Height": 144, "Health": 4}, {"Height": 184, "Health": 6}, {"Height": 195, "Health": 3}], "Height", 2)
    y = -0.0063279857397503525x^2 + 2.1255793226381248x^1 + -170.86631016042716
    
    >>> curve_fit([{"Height": 144, "Health": 4}, {"Height": 184, "Health": 6}, {"Height": 195, "Health": 3}], "Height", 7)
    None
    
    >>> curve_fit([{"Height": 123, "Health": 9}, {"Height": 175, "Health": 2}, {"Height": 185, "Health": 4}], "Height", 1)
    y = -0.09837545126353792x^1 + 20.8384476534296
    """
    import numpy as np
    health_lvl = {}
    for data in data_list:
        key_value = data[attribute]
        health_value = data["Health"]
        if key_value not in health_lvl:
            health_lvl[key_value] = []
        health_lvl[key_value].append(health_value)
    
    health_avg = {key_value: np.mean(health_value) for key_value, health_value in health_lvl.items()}
    health_avg_sort = sorted(health_avg.items())
    x_values = np.array([level[0] for level in health_avg_sort])
    y_values = np.array([level[1] for level in health_avg_sort])

    if degree < 1 or degree > 5:
        return None
    
    if degree <= len(x_values):
        coeffs = np.polyfit(x_values, y_values, degree)
    else:
        coeffs = np.polyfit(x_values, y_values, len(x_values) - 1)

    equation_of_line = "y = "
    coef = len(coeffs)

    for x in range(coef):
        exp = coef - x - 1
        if x < coef - 1:
            equation_of_line += f"{coeffs[x]}x^{exp} + "
        else:
            equation_of_line += f"{coeffs[x]}"
    
    return equation_of_line



# Do NOT include a main script in your submission
