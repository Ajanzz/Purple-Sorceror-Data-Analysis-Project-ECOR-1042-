
# ECOR 1042 Lab 4 - team submission

#import check module here
import check
#import load_data module here
from load_data import *

# Update "" with your the name of the active members of the team
__author__ = "Ajan Balaganesh, Thomas Birnie-Wortley, Anusha Shah, Arianne Beauchesne"

# Update "" with your student number (e.g., 100100100)

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-110"

#==========================================#

# Place test_return_list function here 



def test_return_list(): 

    # test that character_occupation_list returns a list (3 different test cases required) 

    check.equal(isinstance(character_occupation_list('characters-test.csv', 'AT'), list), True) 

    check.equal(isinstance(character_occupation_list('characters-test.csv', 'H'), list), True) 

    check.equal(isinstance(character_occupation_list('characters-test.csv', 'WA'), list), True) 

   

    # test that character_strength_list returns a list (3 different test cases required) 

    check.equal(isinstance(character_strength_list("characters-test.csv", (7, 0)), list), True) 

    check.equal(isinstance(character_strength_list("characters-test.csv", (17, 20)), list), True) 

    check.equal(isinstance(character_strength_list("characters-test.csv", (8, 16)), list), True) 

  

    # test that character_luck_list returns a list (3 different test cases required) 

    check.equal(isinstance(character_luck_list("characters-test.csv", 0.25), list), True) 

    check.equal(isinstance(character_luck_list("characters-test.csv", 0.67), list), True) 

    check.equal(isinstance(character_luck_list("characters-test.csv", 0.001), tuple), False) 

    

    # test that character_weapon_list returns a list (3 different test cases required) 

    check.equal(isinstance(character_weapon_list("characters-test.csv", 'Staff'), list), True) 

    check.equal(isinstance(character_weapon_list("characters-test.csv", 'Handaxe'), int), False) 

    check.equal(isinstance(character_weapon_list("characters-test.csv", 'Dagger'), list), True) 

   

    # test that load_data returns a list (6 different test cases required) 

    check.equal(isinstance(load_data("characters-test.csv", ('Agility', 10)), list), True) 

    check.equal(isinstance(load_data("characters-test.csv", ('Weapon', 'Staff')), float), False) 

    check.equal(isinstance(load_data("characters-test.csv", ('Armour', 10)), list), True) 

    check.equal(isinstance(load_data("characters-test.csv", ('Luck', 0.44)), list), True) 

    check.equal(isinstance(load_data("characters-test.csv", ('Strength', (17, 20))), dict), False) 

    check.equal(isinstance(load_data("characters-test.csv", ('Occupation', 'AT')), list), True) 

    

    # test that calculate_health returns a list (3 different test cases required) 

    check.equal(isinstance(calculate_health([{'Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7, 'Intelligence': 8, 'Armor': 0.7, 'Luck': 8, 'Weapon': 'Staff'}]), list), True) 

    check.equal(isinstance(calculate_health([{'Strength': 0, 'Agility': 0, 'Stamina': 0, 'Personality': 0, 'Intelligence': 0, 'Armor': 0.0, 'Luck': 0, 'Weapon': 'Staff'}]), bool), False) 

    check.equal(isinstance(calculate_health([{'Strength': 15, 'Agility': 4, 'Stamina': 6, 'Personality': 5, 'Intelligence': 2, 'Armor': 0.9, 'Luck': 2, 'Weapon': 'Staff'}]), list), True) 

    
    check.summary() 





# Place test_return_list_correct_length function here


def test_return_list_correct_length(): 

    test_file = 'characters-test.csv'

    # test that character_occupation_list returns a list with the correct length (3 different test cases required)

    check.equal(len(character_occupation_list(test_file, 'AT')), 3,"")

    check.equal(len(character_occupation_list(test_file, 'DB')), 2,"")

    check.equal(len(character_occupation_list(test_file, 'at')), 0,"")

   


    # test that character_strength_list returns a list with the correct length (3 different test cases required)

    check.equal(len(character_strength_list(test_file, (3, 10))), 4,"")

    check.equal(len(character_strength_list(test_file, (0, 13))), 11,"")

    check.equal(len(character_strength_list(test_file, (0, 5))), 0,"")

   


    # test that character_luck_list returns a list with the correct length (3 different test cases required)

    check.equal(len(character_luck_list(test_file, 0.1)), 0,"")

    check.equal(len(character_luck_list(test_file, 0.9)), 26,"")

    check.equal(len(character_luck_list(test_file, 0.5)), 5,"")

  


    # test that character_weapon_list returns a list with the correct length(3 different test cases required)

    check.equal(len(character_weapon_list(test_file, 'Staff')), 4,"")

    check.equal(len(character_weapon_list(test_file, 'Bat')), 0,"")

    check.equal(len(character_weapon_list(test_file, 'staff')), 0,"")

    


    # test that load_data returns a list with the correct length (6 different test cases required)

    check.equal(len(load_data(test_file, ('All', 'Staff'))), 26,"")

    check.equal(len(load_data(test_file, ('Weapon', 'Staff'))), 4,"")

    check.equal(len(load_data(test_file, ('Occupation', 'AT'))), 3,"")

    check.equal(len(load_data(test_file, ('All', 'AT'))), 26,"")

    check.equal(len(load_data(test_file, ('All', 'Batmobile'))), 26,"")

    check.equal(len(load_data(test_file, ('Weapon', 'Batmobile'))), 0,"")

   


    # test that calculate_health returns a list with the correct length (3 different test cases required)

    check.equal(len(calculate_health([])), 0,"")

    check.equal(len(calculate_health([{'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 10, 'Weapon':'Staff'}])), 1,"")

    check.equal(len(calculate_health([{'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 10, 'Weapon':'Staff'}, {'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 12, 'Weapon':'Club'}])), 2,"")

    check.summary()


#Place test_return_correct_dict_inside_list function here
def test_return_correct_dict_inside_list(): 

# Complete the function with your test cases 
    # Complete the function with your test cases 
    
     
    
        # test that character_occupation_list returns a correct dictionary inside the list (3 different test cases required) 
    
        check.equal([(character_occupation_list('characters-test.csv', 'DB'))[0], (character_occupation_list('characters-test.csv', 'DB'))[-1]], 
    
              [{'Strength': 15, 'Agility': 4, 'Stamina': 10, 'Personality': 11, 'Intelligence': 3, 'Luck': 0.61, 'Armor': 9, 'Weapon': 'Club'}, {'Strength': 10, 'Agility': 10, 'Stamina': 11, 'Personality': 11, 'Intelligence': 7, 'Luck': 0.44, 'Armor': 10, 'Weapon': 'Dagger'}], 'Not the right list of dicts') 
    
     
    
        check.equal([(character_occupation_list('characters-test.csv', 'EB'))[0], (character_occupation_list('characters-test.csv', 'EB'))[-1]], 
    
              [{'Strength': 13, 'Agility': 13, 'Stamina': 12, 'Personality': 8, 'Intelligence': 9, 'Luck': 0.67, 'Armor': 11, 'Weapon': 'Dart'}, {'Strength': 13, 'Agility': 8, 'Stamina': 8, 'Personality': 14, 'Intelligence': 15, 'Luck': 0.83, 'Armor': 10, 'Weapon': 'Sling'}], 'Not the right list of dicts') 
    
     
    
        check.equal([(character_occupation_list('characters-test.csv', 'M'))[0], (character_occupation_list('characters-test.csv', 'M'))[-1]], 
    
              [{'Strength': 17, 'Agility': 9, 'Stamina': 11, 'Personality': 5, 'Intelligence': 7, 'Luck': 0.61, 'Armor': 10, 'Weapon': 'Longsword'}, {'Strength': 12, 'Agility': 8, 'Stamina': 0, 'Personality': 13, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 10, 'Weapon': 'Club'}], 'Not the right list of dicts') 
    
     
    
        
    
     
    
        # test that character_strength_list returns a correct dictionary inside the list  (3 different test cases required) 
    
     
    
        check.equal([(character_strength_list('characters-test.csv', (4, 12)))[0], (character_strength_list('characters-test.csv', (4, 12)))[-1]], 
    
              [{'Occupation': 'DB', 'Agility': 10, 'Stamina': 11, 'Personality': 11, 'Intelligence': 7, 'Luck': 0.44, 'Armor': 10, 'Weapon': 'Dagger'}, {'Occupation': 'WA', 'Agility': 11, 'Stamina': 9, 'Personality': 10, 'Intelligence': 8, 'Luck': 0.61, 'Armor': 11, 'Weapon': 'Spear'}], 'Not the right list of dicts') 
    
     
    
        check.equal([(character_strength_list('characters-test.csv', (12, 14)))[0], (character_strength_list('characters-test.csv', (12, 14)))[-1]], 
    
              [{'Occupation': 'AT', 'Agility': 10, 'Stamina': 5, 'Personality': 11, 'Intelligence': 7, 'Luck': 0.44, 'Armor': 10, 'Weapon': 'Club'}, {'Occupation': 'WA', 'Agility': 7, 'Stamina': 8, 'Personality': 8, 'Intelligence': 7, 'Luck': 0.39, 'Armor': 10, 'Weapon': 'Staff'}], 'Not the right list of dicts') 
    
     
    
        check.equal([(character_strength_list('characters-test.csv', (2, 19)))[0], (character_strength_list('characters-test.csv', (2, 19)))[-1]], 
    
              [{'Occupation': 'AT', 'Agility': 10, 'Stamina': 5, 'Personality': 11, 'Intelligence': 7, 'Luck': 0.44, 'Armor': 10, 'Weapon': 'Club'}, {'Occupation': 'WA', 'Agility': 11, 'Stamina': 9, 'Personality': 10, 'Intelligence': 8, 'Luck': 0.61, 'Armor': 11, 'Weapon': 'Spear'}], 'Not the right list of dicts') 
    
     
    
       
    
     
    
        # test that character_luck_list returns a correct dictionary inside the list  (3 different test cases required) 
    
     
    
        check.equal([(character_luck_list('characters-test.csv', 0.40))[0], (character_luck_list('characters-test.csv', 0.40))[-1]], 
    
              [{'Occupation': 'AT', 'Strength': 19, 'Agility': 9, 'Stamina': 9, 'Personality': 10, 'Intelligence': 12, 'Armor': 10, 'Weapon': 'Dagger'}, {'Occupation': 'WA', 'Strength': 14, 'Agility': 7, 'Stamina': 8, 'Personality': 8, 'Intelligence': 7, 'Armor': 10, 'Weapon': 'Staff'}], 'Not the right list of dicts') 
    
     
    
        check.equal([(character_luck_list('characters-test.csv', 0.85))[0], (character_luck_list('characters-test.csv', 0.85))[-1]], 
    
              [{'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Armor': 10, 'Weapon': 'Staff'}, {'Occupation': 'WA', 'Strength': 8, 'Agility': 11, 'Stamina': 9, 'Personality': 10, 'Intelligence': 8, 'Armor': 11, 'Weapon': 'Spear'}], 'Not the right list of dicts') 
    
     
    
        check.equal([(character_luck_list('characters-test.csv', 0.62))[0], (character_luck_list('characters-test.csv', 0.62))[-1]], 
    
              [{'Occupation': 'AT', 'Strength': 13, 'Agility': 10, 'Stamina': 5, 'Personality': 11, 'Intelligence': 7, 'Armor': 10, 'Weapon': 'Club'}, {'Occupation': 'WA', 'Strength': 8, 'Agility': 11, 'Stamina': 9, 'Personality': 10, 'Intelligence': 8, 'Armor': 11, 'Weapon': 'Spear'}], 'Not the right list of dicts') 
    
     
    
        
    
     
    
        # test that character_weapon_list returns a correct dictionary inside the list (3 different test cases required) 
    
     
    
        check.equal([(character_weapon_list('characters-test.csv', 'Staff'))[0], (character_weapon_list('characters-test.csv', 'Staff'))[-1]], 
    
              [{'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 10}, {'Occupation': 'WA', 'Strength': 14, 'Agility': 7, 'Stamina': 8, 'Personality': 8, 'Intelligence': 7, 'Luck': 0.39, 'Armor': 10}], 'Not the right list of dicts') 
    
     
    
        check.equal([(character_weapon_list('characters-test.csv', 'Club'))[0], (character_weapon_list('characters-test.csv', 'Club'))[-1]], 
    
              [{'Occupation': 'AT', 'Strength': 13, 'Agility': 10, 'Stamina': 5, 'Personality': 11, 'Intelligence': 7, 'Luck': 0.44, 'Armor': 10}, {'Occupation': 'WA', 'Strength': 16, 'Agility': 10, 'Stamina': 6, 'Personality': 9, 'Intelligence': 9, 'Luck': 0.44, 'Armor': 10}], 'Not the right list of dicts') 
    
     
    
        check.equal([(character_weapon_list('characters-test.csv', 'Dart'))[0], (character_weapon_list('characters-test.csv', 'Dart'))[-1]], 
    
              [{'Occupation': 'EB', 'Strength': 13, 'Agility': 13, 'Stamina': 12, 'Personality': 8, 'Intelligence': 9, 'Luck': 0.67, 'Armor': 11}, {'Occupation': 'EB', 'Strength': 13, 'Agility': 13, 'Stamina': 12, 'Personality': 8, 'Intelligence': 9, 'Luck': 0.67, 'Armor': 11}], 'Not the right list of dicts') 
    
     
    
        
    
     
    
        # test that load_data returns a correct dictionary inside the list (6 different test cases required) 
    
     
    
        check.equal([(load_data('characters-test.csv', ('Occupation', 'WA')))[0], (load_data('characters-test.csv', ('Occupation', 'WA')))[-1]], 
    
              [{'Strength': 15, 'Agility': 6, 'Stamina': 12, 'Personality': 13, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 9, 'Weapon': 'Short sword'}, {'Strength': 8, 'Agility': 11, 'Stamina': 9, 'Personality': 10, 'Intelligence': 8, 'Luck': 0.61, 'Armor': 11, 'Weapon': 'Spear'}], 'Not the right list of dicts') 
    
     
    
        check.equal([(load_data('characters-test.csv', ('All', 'Handaxe')))[0], (load_data('characters-test.csv', ('All', 'Handaxe')))[-1]], 
    
              [{'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 10, 'Weapon': 'Staff'}, {'Occupation': 'WA', 'Strength': 8, 'Agility': 11, 'Stamina': 9, 'Personality': 10, 'Intelligence': 8, 'Luck': 0.61, 'Armor': 11, 'Weapon': 'Spear'}], 'Not the right list of dicts') 
    
     
    
        check.equal([(load_data('characters-test.csv', ('Weapon', 'Spear')))[0], (load_data('characters-test.csv', ('Weapon', 'Spear')))[-1]], 
    
              [{'Occupation': 'VF', 'Strength': 14, 'Agility': 6, 'Stamina': 4, 'Personality': 12, 'Intelligence': 14, 'Luck': 0.56, 'Armor': 9}, {'Occupation': 'WA', 'Strength': 8, 'Agility': 11, 'Stamina': 9, 'Personality': 10, 'Intelligence': 8, 'Luck': 0.61, 'Armor': 11}], 'Not the right list of dicts') 
    
     
    
        check.equal([(load_data('characters-test.csv', ('All', 'Club')))[0], (load_data('characters-test.csv', ('All', 'Club')))[-1]], 
    
              [{'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 10, 'Weapon': 'Staff'}, {'Occupation': 'WA', 'Strength': 8, 'Agility': 11, 'Stamina': 9, 'Personality': 10, 'Intelligence': 8, 'Luck': 0.61, 'Armor': 11, 'Weapon': 'Spear'}], 'Not the right list of dicts') 
    
     
    
        check.equal([(load_data('characters-test.csv', ('Luck', 0.68)))[0], (load_data('characters-test.csv', ('Luck', 0.68)))[-1]], 
    
              [{'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Armor': 10, 'Weapon': 'Staff'}, {'Occupation': 'WA', 'Strength': 8, 'Agility': 11, 'Stamina': 9, 'Personality': 10, 'Intelligence': 8, 'Armor': 11, 'Weapon': 'Spear'}], 'Not the right list of dicts') 
    
     
    
        check.equal([(load_data('characters-test.csv', ('Occupation', 'AT')))[0], (load_data('characters-test.csv', ('Occupation', 'AT')))[-1]], 
    
              [{'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 10, 'Weapon': 'Staff'}, {'Strength': 19, 'Agility': 9, 'Stamina': 9, 'Personality': 10, 'Intelligence': 12, 'Luck': 0.39, 'Armor': 10, 'Weapon': 'Dagger'}], 'Not the right list of dicts') 
    
     
    
        
    
     
    
        # test that calculate_health returns a correct dictionary inside the list  (3 different test cases required) 
    
     
    
        check.equal(calculate_health([{'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11, 
    
              'Intelligence': 8, 'Luck': 0.67, 'Armor': 10, 'Weapon': 'Staff'}]), [{'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 10, 'Weapon': 'Staff', 'Health': 115.0}], 'Not the right list of dicts') 
    
     
    
        check.equal(calculate_health([{'Occupation': 'AT', 'Strength': 13, 'Agility': 10, 'Stamina': 5, 'Personality': 11, 
    
              'Intelligence': 7, 'Luck': 0.44, 'Armor': 10, 'Weapon': 'Club'}]), [{'Occupation': 'AT', 'Strength': 13, 'Agility': 10, 'Stamina': 5, 'Personality': 11, 'Intelligence': 7, 'Luck': 0.44, 'Armor': 10, 'Weapon': 'Club', 'Health': 90.0}], 'Not the right list of dicts') 
    
     
    
        check.equal(calculate_health([{'Occupation': 'AT', 'Strength': 13, 'Agility': 10, 'Stamina': 5, 'Personality': 11, 'Intelligence': 7, 'Luck': 0.44, 'Armor': 10, 'Weapon': 'Club'}, { 
    
              'Occupation': 'EB', 'Strength': 17, 'Agility': 11, 'Stamina': 7, 'Personality': 12, 'Intelligence': 17, 'Luck': 0.83, 'Armor': 11, 'Weapon': 'Dagger'}]), [{'Occupation': 'AT', 'Strength': 13, 'Agility': 10, 'Stamina': 5, 'Personality': 11, 'Intelligence': 7, 'Luck': 0.44, 'Armor': 10, 'Weapon': 'Club', 'Health': 90.0}, {'Occupation': 'EB', 'Strength': 17, 'Agility': 11, 'Stamina': 7, 'Personality': 12, 'Intelligence': 17, 'Luck': 0.83, 'Armor': 11, 'Weapon': 'Dagger', 'Health': 164.43}], 'Not the right list of dicts') 
    
     
    
        check.summary()     

 




#Place test_calculate_health function here

def test_calculate_health(): 
    #Complete the function with your test cases 
    
    #test that the function does not change the length of the list provided as input parameter (5 different test cases required) 
    try:  
        check.equal(len(calculate_health(character_occupation_list('characters-test.csv', "AT"))), 3, "Wrong length") 
    except KeyError: 
        check.equal(1,1, 'Occupation Length Key Error') 
    
    try: 
        check.equal(len(calculate_health(character_luck_list('characters-test.csv', 0.5))), 2, "Wrong length") 
    except KeyError: 
        check.equal(1,1, 'Luck Length Key Error') 
    
    try: 
        check.equal(len(calculate_health(character_strength_list('characters-test.csv', (8, 8)))), 1, "Wrong length") 
    except KeyError: 
        check.equal(1,1, 'Strength Length Key Error') 
    
    try: 
        check.equal(len(calculate_health(character_weapon_list('characters-test.csv', 'Handaxe'))), 2, "Wrong length") 
    except KeyError: 
        check.equal(1,1, 'Weapon Length Key Error') 
    
    try: 
        check.equal(len(calculate_health(load_data('characters-test.csv', ('All', '')))), 26, "Wrong length") 
    except KeyError: 
        check.equal(1,1, 'Load Data Length Error') 
    
    #test that the function returns an empty list when it is called with an empty list 
    check.equal(len(calculate_health([])), 0, "List is not empty") 
    
    #test that the function increments the number of keys of the dictionary inside the list by one (5 different test cases required) 
    strength_list = character_strength_list('characters-test.csv', (8,8)) 
    strength = [strength_list[0]] 
    
    luck_list = character_luck_list('characters-test.csv', 0.5) 
    luck = [luck_list[0]] 
    
    try: 
        calculate_health(strength) 
    except KeyError: 
        check.equal(1,1, "Strength not in dictionary") 
    else: 
        check.equal(1,0, "Health executed when strength was not in dictionary") 
    
    try: 
        calculate_health(luck) 
    except KeyError: 
        check.equal(1,1, "Luck not in dictionary") 
    else: 
        check.equal(1,0, "Health executed when luck was not in dictionary") 
    
    try:  
        occupation_list = character_occupation_list('characters-test.csv', 'AT') 
        occupation = [occupation_list[0]] 
        check.equal(len((calculate_health(occupation)[0])), 9, "Wrong length of occupation dictionary") 
    except KeyError: 
        check.equal(1,1, 'Occupation Key Error') 
    
    try:  
        weapon_list = character_weapon_list('characters-test.csv', 'Staff') 
        weapon = [weapon_list[0]] 
        check.equal(len((calculate_health(weapon)[0])), 9, "Wrong length of weapon dictionary") 
    except KeyError: 
        check.equal(1,1) 
    
    try:  
        data = load_data('characters-test.csv', ('All', "")) 
        data1 = [data[0]] 
        check.equal(len((calculate_health(data1)[0])), 10, "Wrong length of load data dictionary") 
    except KeyError: 
        check.equal(1,1) 
    
    #test that the Health value is properly calculated (5 different test cases required) 
    test_list = [
        {"Occupation":"DB", 'Strength': 1, 'Agility': 1, 'Stamina': 1, 'Personality': 1, 'Intelligence': 1, 'Luck': 1.0, 'Armor': 1, 'Weapon': 'Staff'}, 
        {'Strength': 1, 'Agility': 1, 'Stamina': 1, 'Personality': 1, 'Intelligence': 1, 'Luck': 1, 'Armor': 1, 'Weapon': 'Staff'}, 
        {"Occupation":"DB", 'Agility': 1, 'Stamina': 1, 'Personality': 1, 'Intelligence': 1, 'Luck': 1, 'Armor': 1, 'Weapon': 'Staff'}, 
        {"Occupation":"DB", 'Strength': 1, 'Agility': 1, 'Stamina': 1, 'Personality': 1, 'Intelligence': 1, 'Luck': 1, 'Armor': 1, 'Weapon': 'Staff'}, 
        {"Occupation":"DB", 'Strength': 1, 'Agility': 1, 'Stamina': 1, 'Personality': 1, 'Intelligence': 1, 'Armor': 1, 'Weapon': 'Staff'}, 
        {"Occupation":"DB", 'Strength': 1, 'Agility': 1, 'Stamina': 1, 'Personality': 1, 'Intelligence': 1, 'Luck': 1, 'Armor': 1}
    ] 

    for number in range(0,5): 
        try:  
            health_test_var = calculate_health([test_list[number]]) 
            check.within(health_test_var[0]['Health'], 6.0, 0.000001, 'Health value not properly calculated') 
        except KeyError: 
            check.equal(1,1,'Key Error Successful') 

    check.summary() 




# Do NOT include a main script in your submission
