import pandas as pd
import json

xl = pd.ExcelFile("Loot generator table version 2.xlsx")
meleeweapons = {}
bows = {}
firearms = {}




perklist= {}

perks_sheet_list = [4,5,6,7,8]
sheet_names = xl.sheet_names
weapon_type_index = [3,4,5,6,7,8,9]


for perk_sheet in perks_sheet_list:
    perk_class = sheet_names[perk_sheet]
    print(perk_class)
    perklist[perk_class]={}
    perks = xl.parse(perk_sheet)
    page_headings = perks.keys()
    print(page_headings)


    for weapon_type in weapon_type_index:
        weapon_type_name = page_headings[weapon_type]
        perklist[perk_class][weapon_type_name] = {}
        if(weapon_type==1):
            print(weapon_type_name)
        row_iterator = perks.iterrows()
        for i, row in row_iterator:
            print(row[weapon_type])
            print(weapon_type_name)
            if row[weapon_type] == 1:
                perklist[perk_class][weapon_type_name][row[0]] = {page_headings[1]: row[1], page_headings[2]: row[2]}
#print(perklist)

with open('perks.json', 'w') as outfile:
    json.dump(perklist, outfile)





















