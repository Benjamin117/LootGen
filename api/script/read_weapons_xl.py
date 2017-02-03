import pandas as pd
import json


xl = pd.ExcelFile("Loot generator table version 2.xlsx")

weaponlist= {}

weapon_sheet_list = [0,1]
sheet_names = xl.sheet_names
weapon_attribute_index = [3,4,5]


for weapons_sheet in weapon_sheet_list:
    weapon_class = sheet_names[weapons_sheet]
    print(weapon_class)
    weaponlist[weapon_class] = {}
    weapons = xl.parse(weapons_sheet)
    page_headings = weapons.keys()

    row_iterator = weapons.iterrows()
    index = 0
    for i, row in row_iterator:

        row_obj = { "Weapon Class":row[0],
                    "Weapon Family":row[1],
                    "Weapon Name":row[2],
                    "Base Damage":row[3],
                    "Base Properties":row[4],
                    "Special Properties":row[5],
                    "Base Value":row[6],
                    "Weight":row[7]}
        weaponlist[weapon_class][str(index)]=row_obj
        index+=1
    print(weaponlist)


with open('weapons.json', 'w') as outfile:
    json.dump(weaponlist, outfile)





















