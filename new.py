import pandas as pd
import re

fct_entries = pd.read_csv("fct_entries_2020-09-21 22:18:54.766014.csv")
dim_tags = pd.read_csv("dim_tags2020-09-21 22:18:54.766014.csv")

regex = r"<{{\|t\|\d\d\d\d\d\d\|}}>"
tag_codes = []

for i in range(len(fct_entries['note'])):

    matches = re.finditer(regex, str(fct_entries['note'][i]), re.MULTILINE)

    for matchNum, match in enumerate(matches):
        tag_codes.append(match.group()[6:12])
    
    print(tag_codes)
    
    print(tag_codes.distinct())
    
    unique(tag_codes)
    
# function to get unique values 

  
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in tag_codes: 
        print(x)
        # check if exists in unique_list or not 
        if x not in tag_codes: 
            unique_list.append(x) 
    # print list 
    for x in unique_list: 
        print (x)
        
    return (x)



string_text = fct_entries['note'][50]
   
# Prints the string by replacing geeks by Geeks  
print(string.replace('<{{|t|255982|}}>', 'Tag'))

dim_tags

[re.search('<{{|t|255982|}}>', string) for string in string_text]
  