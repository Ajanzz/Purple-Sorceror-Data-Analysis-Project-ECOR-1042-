
# ECOR 1042 Lab 3 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Ajan Balaganesh, Thomas Birnie-Wortley, Anusha Shah, Arianne Beauchesne"

# Update "" with your team (e.g. T102)
__team__ = "T110"


#==========================================#
# Place your character_occupation_list function after this line
def character_occupation_list(file_name: str, occupation: str) -> list[dict]: 
   """Returns a list containing dictionaries of attributes of characters given the file where the data is stored and the wanted occupation. 
   Preconditions: File must exist and have the following columns in the following order ['Occupation', 'Strength', 'Agility', 'Stamina', 'Personality', 'Intelligence', 'Luck', 'Armor', 'Weapon']. 
   >>>character_occupation_list('characters-mat.csv', 'AT') 
   [{'Strength': 13, 'Agility': 2, 'Stamina': 6,  'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': Staff},  
   {another element},...] 
   >>>character_occupation_list('characters-mat.csv', 'a') 
   [] 
   >>>character_occupation_list('characters-mat.csv', 'at') 
   [] 
   """ 
   file = open(file_name, 'r') 
   stats_list = []   
   first_line = True 
   for line in file: 
      line = line.strip() 
      line = line.split(",") 
      if first_line: 
         first_line = False 
         table_header = line 
      else: 
         if occupation == line[0]: 
            stats = {} 
            stats[table_header[1]] = int(line[1]) 
            stats[table_header[2]] = int(line[2]) 
            stats[table_header[3]] = int(line[3]) 
            stats[table_header[4]] = int(line[4]) 
            stats[table_header[5]] = int(line[5]) 
            stats[table_header[6]] = float(line[6])
            stats[table_header[7]] = int(line[7]) 
            stats[table_header[8]] = line[8] 
            stats_list.append(stats)            
   file.close() 
   return stats_list 

 



#==========================================#
# Place your character_strength_list function after this line
def character_strength_list(file_name: str, strength: tuple[int, int]) -> list[dict]: 

   """Return a list of dictionaries of characters with strength between a minimum and maximum value from a file while given the file name and the strength range. 

   Preconditions: len(strength) == 2, file_name has columns labeled ['Occupation', 'Strength', 'Agility', 'Stamina', 'Personality', 'Intelligence', 'Luck', 'Armor', 'Weapon'] 

   >>> character_strength_list('characters-mat.csv', (2,10)) 
   [{'Occupation': 'AT', 'Strength': 5, 'Agility': 8, 'Stamina': 7, 'Personality': 6, 'Intelligence': 1, 'Luck': 3, 'Armor': 10, 'Weapon': 'Staff'}] 
   
   >>> character_strength_list('characters-mat.csv', (20,30)) 

   [] 

   >>> character_strength_list('characters-mat.csv', (50,70)) 

   [] 

   """ 

   list1 = [] 

   in_file = open(file_name) 



   first_line = True 

   count = 0 

   for line in in_file: 

      count += 1 

      line = line.strip() 

      line = line.split(',')  

         

      if first_line: 

            first_line = False 

            table_header = line 

      else: 

            character = {}    

            character[table_header[0]] = str(line[0]) 

            character[table_header[1]] = float(line[1]) 

            character[table_header[2]] = float(line[2]) 

            character[table_header[3]] = float(line[3]) 

            character[table_header[4]] = float(line[4]) 

            character[table_header[5]] = float(line[5]) 

            character[table_header[6]] = float(line[6]) 

            character[table_header[7]] = float(line[7]) 

            character[table_header[8]] = str(line[8]) 



            if min(strength) <= character['Strength'] <= max(strength): 

               del character['Strength'] 

               list1.append(character) 

   in_file.close() 

   return list1 


#==========================================#
# Place your character_luck_list function after this line
def character_luck_list(name_of_file: str, luck: float) -> list[dict]: 

   """Return a list of dictionnaries for characters whose luck is lower than the luck value that was input by the user. 
   Precondition : luck >= 0, name_of_file has the following columns ['Occupation', 'Strength', 'Agility', 'Stamina', 'Personality', 'Intelligence', 'Luck', 'Armor', 'Weapon'] 
   >>> character_luck_list ('characters-mat.csv', 0.2) 
   [{'Occupation': 'VF', 'Strength': 12, 'Agility': 4, 'Stamina': 2, 'Personality': 14, 'Intelligence': 14, 'Armor': 9, 'Weapon': 'Dagger'}] 
   >>> character_luck_list ('characters-mat.csv', 0.1) 
   [] 

   >>> character_luck_list ('characters-mat.csv', 0.25) 
   [{'Occupation': 'AT', 'Strength': 14, 'Agility': 5, 'Stamina': 6, 'Personality': 13, 'Intelligence': 9, 'Armor': 9, 'Weapon': 'Staff'}, {'Occupation': 'DB', 'Strength': 15, 'Agility': 7, 'Stamina': 6, 'Personality': 7, 'Intelligence': 13, 'Armor': 10, 'Weapon': 'Club'}, {'Occupation': 'DB', 'Strength': 16, 'Agility': 10, 'Stamina': 9, 'Personality': 13, 'Intelligence': 6, 'Armor': 10, 'Weapon': 'Club'}, {'Occupation': 'DB', 'Strength': 12, 'Agility': 9, 'Stamina': 5, 'Personality': 7, 'Intelligence': 7, 'Armor': 10, 'Weapon': 'Club'}, {'Occupation': 'H', 'Strength': 16, 'Agility': 12, 'Stamina': 3, 'Personality': 6, 'Intelligence': 15, 'Armor': 11, 'Weapon': 'Dagger'}, {'Occupation': 'HG', 'Strength': 17, 'Agility': 10, 'Stamina': 9, 'Personality': 14, 'Intelligence': 12, 'Armor': 10, 'Weapon': 'Dagger'}, {'Occupation': 'VF', 'Strength': 16, 'Agility': 6, 'Stamina': 3, 'Personality': 8, 'Intelligence': 8, 'Armor': 9, 'Weapon': 'Sling'}, {'Occupation': 'VF', 'Strength': 18, 'Agility': 10, 'Stamina': 9, 'Personality': 13, 'Intelligence': 6, 'Armor': 10, 'Weapon': 'Club'}, {'Occupation': 'VF', 'Strength': 14, 'Agility': 8, 'Stamina': 8, 'Personality': 10, 'Intelligence': 8, 'Armor': 10, 'Weapon': 'Dagger'}] 
   """ 

  

   full_file = open(name_of_file, "r") 

   luck_character_list = [] 

   first_line = True 

  

   for line in full_file: 

      line = line.strip().split(",") 

      luck_dict = {} 

      if first_line: 

         first_line = False 

         headers = line 

      elif luck > float(line[6]): 

               luck_dict[headers[0]] = str(line[0]) 

               luck_dict[headers[1]] = int(line[1]) 

               luck_dict[headers[2]] = int(line[2]) 

               luck_dict[headers[3]] = int(line[3]) 

               luck_dict[headers[4]] = int(line[4]) 

               luck_dict[headers[5]] = int(line[5]) 

               luck_dict[headers[7]] = int(line[7]) 

               luck_dict[headers[8]] = str(line[8]) 

               luck_character_list.append(luck_dict) 

  

   full_file.close() 

  

   return luck_character_list 

#==========================================#
# Place your character_weapon_list function after this line
def character_weapon_list(filename: str, weapon: str) -> list[dict]: 

   """Return a list holding dictionary's of each character that has a certain weapon type given the file name and weapon type. 



   Precondition: filename has these columns: ['Occupation', 'Strength', 'Agility', 'Stamina', 'Personality', 'Intelligence', 'Luck', 'Armor', 'Weapon'] 

  

   >>>character_weapon_list('characters-mat.csv', 'Club') 

   [{'Occupation': 'AT', 'Strength': '14', 'Agility': '2', 'Stamina': '8', 'Personality': '11', 'Intelligence': '5', 'Luck': '0.78', 'Armor': '8'}, 

   {next item}, ....}] 

  

   >>>character_weapon_list('characters-mat.csv', 'Hellp') 

   [] 

  

   >>>character_weapon_list('characters-mat.csv', 'Handaxe') 

   [{'Occupation': 'HG', 'Strength': 16, 'Agility': 4, 'Stamina': 7, 'Personality': 12, 'Intelligence': 9, 'Luck': 0.61, 'Armor': 9}, 

   {next item}, ... }] 

  

   """ 

  

   weapon_file = open(filename, 'r') 

  

   character_list = [] 

  

   i = True 

  

   for line in weapon_file: 

      if i: 

         line = line.strip().split(',') 

         first_line = line 

         i = False 

      else: 

         if weapon in line: 

               line = line.strip().split(',') 

               character_dict = {} 

               character_dict[first_line[0]] = line[0] 

               character_dict[first_line[1]] = int(line[1]) 

               character_dict[first_line[2]] = int(line[2]) 

               character_dict[first_line[3]] = int(line[3]) 

               character_dict[first_line[4]] = int(line[4]) 

               character_dict[first_line[5]] = int(line[5]) 

               character_dict[first_line[6]] = float(line[6]) 

               character_dict[first_line[7]] = int(line[7]) 

               character_list.append(character_dict) 

  

   weapon_file.close() 

  

   return character_list 


#==========================================#
# Place your load_data function after this line
def load_data(file_name: str, trim: tuple[str, any]) -> list[dict]: 

   """Return a list of dictionaries of characters with a specified attribute and value from a file. 

   Preconditions: len(trim) == 2, file_name has columns labeled ['Occupation', 'Strength', 'Agility', 'Stamina', 'Personality', 'Intelligence', 'Luck', 'Armor', 'Weapon'] 

   >>>load_data('characters-mat.csv', ('Occupation','AT')) 

   [{'Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': 'Staff'}, {another element}] 

   >>>load_data('characters-mat.csv', ('Weapon', 'Hero')) 

   [] 

   >>>load_data('characters-mat.csv', ('All', 6)) 

   [{'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': 'Staff'}, {another element}] 

   """ 
   if trim[0] == 'All':
      file = open(file_name, 'r')
      dictionary_lst = []
      first_line = True
      for line in file:
         line = line.strip().split(',')
         if first_line:
            table_header = line
            first_line = False
         else:
            characters= {}
            characters[table_header[0]] = line[0]
            characters[table_header[1]] = int(line[1]) 
            characters[table_header[2]] = int(line[2]) 
            characters[table_header[3]] = int(line[3]) 
            characters[table_header[4]] = int(line[4]) 
            characters[table_header[5]] = int(line[5]) 
            characters[table_header[6]] = float(line[6])
            characters[table_header[7]] = int(line[7]) 
            characters[table_header[8]] = line[8]
            dictionary_lst.append(characters)
      file.close()
   elif trim[0] == 'Occupation':
      dictionary_lst = character_occupation_list(file_name, trim[1])
   elif trim[0] == 'Strength':
      dictionary_lst = character_strength_list(file_name, (trim[1], trim[1]))
   elif trim[0] == 'Luck':
      dictionary_lst = character_luck_list(file_name, trim[1])
   elif trim[0] == 'Weapon':
      dictionary_lst = character_weapon_list(file_name, trim[1])
   else:
      dictionary_lst = []
   return dictionary_lst
   
         
         



        


#==========================================#
# Place your calculate_health function after this line
def calculate_health(dictionary_lst: list[dict]) -> list[dict] : 

   """Returns a list of dictionaries that is identical to the list of dictionaries given as a parameter but adds a health section and returns the new list of dictionaries. 
   File name where the data is stored must also be given. 
   Precondition: File must exist and have the following columns in the following order: ['Occupation', 'Strength', 'Agility', 'Stamina', 'Personality', 'Intelligence', 'Luck', 'Armor', 'Weapon'].
   >>>calculate_health([{'Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7, 'Intelligence': 8, 'Armor': 0.7, 'Luck': 8, 'Weapon':'Staff'}, {another element}])
   [{'Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7, 'Intelligence': 8, 'Armor': 0.7, 'Luck': 8, 'Weapon':'Staff', 'Health': 80.8}, {another element}]
   >>>calculate_health([{'Strength': 0, 'Agility': 0, 'Stamina': 0, 'Personality': 0, 'Intelligence': 0, 'Armor': 0.0, 'Luck': 0, 'Weapon':'Staff'}, {another element}])
   [{'Strength': 0, 'Agility': 0, 'Stamina': 0, 'Personality': 0, 'Intelligence': 0, 'Armor': 0.0, 'Luck': 0, 'Weapon':'Staff', 'Health': 0.0}, {another element}]
   >>>calculate_health([{'Strength': 15, 'Agility': 4, 'Stamina': 6, 'Personality': 5, 'Intelligence': 2, 'Armor': 0.9, 'Luck': 2, 'Weapon':'Staff'}, {another element}])
   [{'Strength': 15, 'Agility': 4, 'Stamina': 6, 'Personality': 5, 'Intelligence': 2, 'Armor': 0.9, 'Luck': 2, 'Weapon':'Staff', 'Health': 34.81}, {another element}]
   """ 

   for i in range (len(dictionary_lst)): 
      health= dictionary_lst[i]['Strength'] + dictionary_lst[i]["Agility"] + dictionary_lst[i]["Stamina"] + dictionary_lst[i]["Personality"] + dictionary_lst[i]["Intelligence"] + dictionary_lst[i]["Armor"] ** 2 * dictionary_lst[i]["Luck"] 
      dictionary_lst[i].update({"Health": health}) 
   return dictionary_lst 

# Do NOT include a main script in your submission
