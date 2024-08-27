# ECOR 1042 Lab 5 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Ajan Balaganesh, Thomas Birnie-Wortley, Anusha Shah, Arianne Beauchesne"

# Update "" with your team (e.g. T102)
__team__ = "T110"

#==========================================#
# Place your sort_characters_agility_bubble function after this line
def sort_characters_agility_bubble(list_dicts: list[dict], order: str) -> list[dict]: 

  """Returns a list of input dictionaries in either ascending or descending order of agility values. If "Agility" is not a key in the dictionaries, function returns original list.

 

  Precondition : order == "A" or order == "D" and keys in all the dictionaries are the same.

 

  >>> sort_characters_agility_bubble ([{'Occupation': 'AT', 'Agility': 15}, {'Occupation': 'H', 'Agility': 10}, {'Occupation': 'EB', 'Agility': 5}], "A") 

  [{'Occupation': 'EB', 'Agility': 5}, {'Occupation': 'H', 

      'Agility': 10}, {'Occupation': 'AT', 'Agility': 15}] 

 

  >>> sort_characters_agility_bubble ([{'Occupation': 'DB', 'Agility': 2}, {'Occupation': 'H', 'Agility': 14}, {'Occupation': 'AT', 'Agility': 8}, {'Occupation': 'M', 'Agility': 6}], "D") 

  [{'Occupation': 'H', 'Agility': 14}, {'Occupation': 'AT', 'Agility': 8}, { 

      'Occupation': 'M', 'Agility': 6}, {'Occupation': 'DB', 'Agility': 2}] 

 

  >>> sort_characters_agility_bubble ([{'Occupation': 'M'}, {'Occupation': 'EB'}], "A") 

  "Agility" key is not present. 

  [{'Occupation': 'M'}, {'Occupation': 'EB'}] 

  """ 

  swap = True 

  while swap: 

      swap = False 

      for i in range(len(list_dicts) - 1): 

 

              if order == "A" and "Agility" in list_dicts[i]: 

                  if list_dicts[i]["Agility"] > list_dicts[i + 1]["Agility"]: 

                      list_dicts[i], list_dicts[i + 

                                                    1] = list_dicts[i + 1], list_dicts[i] 

                      swap = True 

 

              elif order == "D" and "Agility" in list_dicts[i]: 

                  if list_dicts[i + 1]["Agility"] > list_dicts[i]["Agility"]: 

                      list_dicts[i], list_dicts[i + 

                                                1] = list_dicts[i + 1], list_dicts[i] 

                      swap = True 

 

              else: 

                print("\"Agility\" key is not present.") 

 

  return list_dicts 

#==========================================#
# Place your sort_characters_intelligence_selection function after this line
def sort_characters_intelligence_selection(lists: list[dict], order: str) -> list[dict]: 

    """Return a list of dictionaries in descending or ascending order of intelligence values. If "Intelligence" is not a key in the dictionaries, function returns original list.  

    Precondition: Order must be inputted as A or D and keys in all the dictionaries are the same.

    >>>sort_characters_intelligence_selection([{'Occupation': 'EB', 

    'Intelligence': 9}, {'Occupation': 'H', 

    'Intelligence': 12}], "D") 

  

    [{'Occupation': 'H', 'Intelligence': 12}, {'Occupation': 'EB', 'Intelligence': 9}]  

    >>>sort_characters_intelligence_selection([{'Occupation': 'EB','Intelligence': 20}, {'Occupation': 'H', 

    'Intelligence': 9}], "A")  

    [{'Occupation': 'H', 'Intelligence': 9}, {'Occupation': 'EB', 'Intelligence': 20}] 

    >>>sort_characters_intelligence_selection([{'Occupation': 'AT'}, {'Occupation': 'EB'}], 'A') 

    "Intelligence" key is not present 

    [{'Occupation': 'AT'}, {'Occupation': 'EB'}] 

    """ 

    length = len(lists) 

    key = 'Intelligence' 

    string = '"Intelligence" key is not present' 

    if lists == []: 

        return [] 

    for i in range(length): 

        if not key in lists[i]: 

            print(string) 

            return lists 

    else: 

        if order == ('A'): 

            for t in range(length - 1): 

                min_index = t 

                for x in range(t + 1, length): 

                    if lists[min_index][key] > lists[x][key]: 

                        min_index = x 

                lists[t], lists[min_index] = lists[min_index], lists[t] 

        elif order == ('D'): 

            for t in range(length - 1): 

                max_index = t 

                for x in range(t + 1, length): 

                    if lists[x][key] > lists[max_index][key]: 

                        max_index = x 

                lists[t], lists[max_index] = lists[max_index], lists[t] 

  

        return lists 

#==========================================#
# Place your sort_characters_health_insertion function after this line
def sort_characters_health_insertion(list_of_dicts: list[dict], direction: str) -> list[dict]: 
    """Return a list of dictionaries sorted in ascending or descending order based on the value of the 
    health attribute given a direction in which to sort. If "Health is not a key in the dictionary, function returns original list.

    Preconditions: Valid arguments for direction are "A" or "D" and keys in all the dictionaries are the same.

    >>> sort_characters_health_insertion([], "D") 
    "Health is not a Key in the dictionary" 

    >>> sort_characters_health_insertion([{'Occupation': 'EB', 'Health': 62.37}, {'Occupation': 'H', 'Health': 62.83}], "A") 
    [{'Occupation': 'EB','Health': 62.37}, {'Occupation': 'H', 'Health': 62.83}] 

    >>> sort_characters_health_insertion([{'Occupation': 'EB', 'Health': 62.37}, {'Occupation': 'H', 'Health': 62.71},{'Occupation': 'EB', 'Health': 62.77}, {'Occupation': 'H', 'Health': 62.41},{'Occupation': 'EB', 'Health': 62.27}, {'Occupation': 'H', 'Health': 62.91}], "D") 
    [{'Occupation': 'H', 'Health': 62.91}, {'Occupation': 'EB', 'Health': 62.77},  
    {'Occupation': 'H', 'Health': 62.71}, {'Occupation': 'H', 'Health': 62.41},  
    {'Occupation': 'EB', 'Health': 62.37}, {'Occupation': 'EB', 'Health': 62.27}] 
    """ 

    if list_of_dicts == []: 
        print("Health is not a Key in the dictionary") 
        return list_of_dicts 

    if direction == "A": 
        if "Health" in list_of_dicts[0]: 
            for i in range(1, len(list_of_dicts)): 
                key = list_of_dicts[i] 
                j = i -1 
                while j >= 0 and key["Health"] < list_of_dicts[j]["Health"]: 
                    list_of_dicts[j + 1] = list_of_dicts[j]  
                    j-= 1 
                list_of_dicts[j + 1] = key 
            return list_of_dicts 
        else: 
            print("Health is not a key in the dictionary") 

    else: 
        if "Health" in list_of_dicts[0]: 
            for i in range(1, len(list_of_dicts)): 
                key = list_of_dicts[i] 
                j = i -1 
                while j >= 0 and key["Health"] > list_of_dicts[j]["Health"]: 
                    list_of_dicts[j + 1] = list_of_dicts[j]  
                    j-= 1 
                list_of_dicts[j + 1] = key 
            return list_of_dicts 
        else: 
            print("Health is not a key in the dictionary") 
    return list_of_dicts


#==========================================#
# Place your sort_characters_armor_bubble function after this line
def sort_characters_armor_bubble(given_lst: list[dict], order: str) -> list[dict]:
    """Returns a list of dictionaries in ascending or descending order of armor values given an initial list of dictionaries and the order
    in which the armor values should be sorted. If "Armor" is not a key in the dictionaries, function returns original list.
    Preconditions: The order parameter can only take A or D as an argument and keys in all the dictionaries are the same.
    >>>sort_characters_armor_bubble([{'Occupation': 'EB', 'Armor': 11}, {'Occupation': 'H', 'Armor': 10}], D)
    [{'Occupation': 'EB', 'Armor': 11}, {'Occupation': 'H', 'Armor': 10}]
    >>>sort_characters_armor_bubble([{'Occupation': 'EB'}, {'Occupation': 'H'}], D)
    [{'Occupation': 'EB'}, {'Occupation': 'H'}]
    >>>sort_characters_armor_bubble([{'Occupation': 'EB', 'Armor': 10}, {'Occupation': 'H', 'Armor': 11}], A)
    [{'Occupation': 'EB', 'Armor': 10}, {'Occupation': 'H', 'Armor': 11}]
    """
    if given_lst == []:
        print("\"Armor\" key not present")
        return given_lst
    if order == "A":
        if "Armor" in given_lst[0]:
            swap = True
            while swap:
                swap = False
                for i in range(len(given_lst) - 1):
                    if given_lst[i]["Armor"] > given_lst[i + 1]["Armor"]:
                        given_lst[i], given_lst[i + 1] = given_lst[i + 1], given_lst[i]
                        swap = True
        else:
            print("\"Armor\" key not present")
    else:
        if "Armor" in given_lst[0]:
            swap = True
            while swap:
                swap = False
                for i in range(len(given_lst) - 1):
                    if given_lst[i]["Armor"] < given_lst[i + 1]["Armor"]:
                        given_lst[i], given_lst[i + 1] = given_lst[i + 1], given_lst[i]
                        swap = True
        else:
            print("\"Armor\" key not present")
    return given_lst

#==========================================#
# Place your sort function after this line
def sort(list_of_dict: list[dict], order: str, attribute: str) -> list[dict]:
    """Returns a list of dictionaries sorted in either descending order or ascending order based on a specified attribute(Agility, Intelligence, Health, Armor).
    If the attribute specified is an invalid input it will return the original list.
    Precondition: Order must be specified as "A" or "D" and keys in all the dictionaries are the same.
    >>>sort([{'Occupation': 'EB','Intelligence': 20}, {'Occupation': 'H', 'Intelligence': 12}], D, "Intelligence")
    [{'Occupation': 'EB','Intelligence': 20}, {'Occupation': 'H', 'Intelligence': 12}]
    >>>sort([{'Occupation': 'EB','Intelligence': 20}, {'Occupation': 'H', 'Intelligence': 12}], D, "Strength")
    [{'Occupation': 'EB','Intelligence': 20}, {'Occupation': 'H', 'Intelligence': 12}]
    >>>sort([{'Occupation': 'EB','Intelligence': 20}, {'Occupation': 'H', 'Intelligence': 12}], A, "Intelligence")
    [{'Occupation': 'H', 'Intelligence': 12}, {'Occupation': 'EB','Intelligence': 20}]
    """
    if attribute == "Agility":
        return sort_characters_agility_bubble(list_of_dict, order)
    elif attribute == "Intelligence":
        return sort_characters_intelligence_selection(list_of_dict, order)
    elif attribute == "Health":
        return sort_characters_health_insertion(list_of_dict, order)
    elif attribute == "Armor":
        return sort_characters_armor_bubble(list_of_dict, order)
    else:
        print("Cannot be sorted by " + attribute)
        return list_of_dict
    

# Do NOT include a main script in your submission

