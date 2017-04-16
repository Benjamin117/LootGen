from flask import *
import flask
import random
import json
from LootGenutils import *
import os
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
# load up the difficulty table for perks
diff_tables = os.path.join(SITE_ROOT, "static", "difficultytables.json")
difficulty_table = json.load(open(diff_tables))
# load up perk table
perk_json = os.path.join(SITE_ROOT, "static", "perks.json")
perks = json.load(open(perk_json))

# load up the weapons list
items_json = os.path.join(SITE_ROOT, "static", "weapons.json")
items = json.load(open(items_json))


def roll(massDist):
    randRoll = random.random()  # in [0,1)
    sum = 0
    result = 0

    for mass in massDist:
        sum += mass
        if randRoll < sum:
            return result
        result += 1

def draw_base(type):
    base_item_set = items[type]
    draw = random.choice(list(base_item_set.keys()))
    base_item = base_item_set[draw]
    return base_item

def initialise_item(base_item,itemtype):
    base_item['secondaryperk'] = 'none'
    base_item['primaryperk'] = 'none'
    base_item['pperkrarity'] = 'none'
    base_item['sperkrarity'] = 'none'
    base_item['pperkvalue'] = '0 GP'
    base_item['sperkvalue'] = '0 GP'
    base_item['itemtype'] = itemtype
    if 'Special Properties' in base_item:
        if type(base_item['Special Properties']) is not str:
            base_item['Special Properties'] = 'none'
    return base_item

def roll_primary_perk(difficulty,labels):
    diff = difficulty_table[0][difficulty]
    dist = []

    for value in diff:
        dist.append(diff[value])
        labels.append(value)

    return labels[roll(dist)]

def roll_secondary_perk(star_count, labels):

    if star_count == 0:
        #print(0)
        return 'none'
    if star_count == 1:
        #print(1)
        return labels[roll([0.98, 0.02])]
    if star_count == 2:
        #print(2)
        return labels[roll([0.99, 0.001])]
    if star_count == 3:
        #print(3)
        return labels[roll([0.999, 0.0001])]
    if star_count == 4:
        #print(4)
        return labels[roll([0.9999, 0.0001])]

def assign_perks(pperk_rarity_result,base_item,labels):
    print(base_item)
    print(labels)
    if pperk_rarity_result != 'none':
        primary_perk_set = perks[pperk_rarity_result]
        weapon_class = base_item[base_item['itemtype']+' Class']
        primary_perk = random.choice(list(primary_perk_set[weapon_class].keys()))
        base_item['primaryperk'] = primary_perk
        base_item['pperkrarity'] = pperk_rarity_result
        base_item['pperkeffect'] = primary_perk_set[weapon_class][primary_perk]['Effect']
        base_item['pperkvalue'] = primary_perk_set[weapon_class][primary_perk]['Value']

        # Check for second perk roll

        mp_stars = primary_perk.count('*')
        sec_perk_result = roll_secondary_perk(mp_stars, labels)

        if sec_perk_result != 'none':
            # print("second perk")
            sec_perk_set = perks[sec_perk_result]
            secondary_perk = random.choice(list(sec_perk_set[weapon_class].keys()))
            base_item['secondaryperk'] = secondary_perk
            base_item['sperkrarity'] = sec_perk_result
            base_item['sperkeffect'] = sec_perk_set[weapon_class][secondary_perk]['Effect']
            base_item['sperkvalue'] = sec_perk_set[weapon_class][secondary_perk]['Value']
            # print(secondary_perk)


    else:
        primary_perk = 'none'

    return base_item

def format_item(base_item):
    print('base:')
    print(base_item)
    if base_item['primaryperk'] != 'none':
        b = base_item['primaryperk']
    else:
        b = ''
    if base_item['secondaryperk'] != 'none':
        m = base_item['secondaryperk']
    else:
        m = ''
    draw_weapon_name = b + ' ' + m + ' ' + base_item[base_item['itemtype']+' Name']
    draw_weapon_name = draw_weapon_name.replace("*", "")
    base_item['drawname'] = draw_weapon_name
    print(base_item)
    if 'SP' in base_item['Base Value']:
        if int(base_item['pperkvalue'].split()[0]) + int(base_item['sperkvalue'].split()[0]) == 0:
            base_item['totalvalue'] = base_item['Base Value']
        else:
            base_item['totalvalue'] = str(
                int(base_item['pperkvalue'].split()[0]) + int(base_item['sperkvalue'].split()[0])) + " GP, " + \
                                      base_item['Base Value']
    else:
        base_item['totalvalue'] = str(
            int(base_item['Base Value'].split()[0]) + int(base_item['pperkvalue'].split()[0]) + int(
                base_item['sperkvalue'].split()[0])) + " GP"

    return json.dumps(base_item)




@app.route("/rollweapon")
def roll_for_weapon():

    difficulty = request.args.get('difficulty')
    itemtype = 'Weapon'

    # melee or ranged?
    typeprobs = [0.5, 0.5]
    typelabels = ["Melee weapons", "Ranged weapons"]
    typeresult = typelabels[roll(typeprobs)]

    # draw a weapon
    base_item = draw_base(typeresult)

    # intialise the fields
    base_item= initialise_item(base_item,itemtype)

    #roll for primary perk
    labels = []
    pperk_rarity_result = roll_primary_perk(difficulty,labels)

    # assign primary perk, check for second
    base_item = assign_perks(pperk_rarity_result, base_item,labels)

    #assign other attributes, format the object
    item_json =format_item(base_item)

    resp = Response(response=item_json,
                    status=200,
                    mimetype="application/json")
    return (resp)


@app.route("/rollarmour")
def roll_for_armour():

    difficulty = request.args.get('difficulty')
    itemtype = 'Armour'

    # draw a weapon
    base_item = draw_base(itemtype)
    print(base_item)
    # intialise the fields
    base_item = initialise_item(base_item, itemtype)

    # roll for primary perk
    labels = []
    pperk_rarity_result = roll_primary_perk(difficulty, labels)

    # assign primary perk, check for second
    base_item = assign_perks(pperk_rarity_result, base_item, labels)

    # assign other attributes, format the object
    item_json = format_item(base_item)

    resp = Response(response=item_json,
                    status=200,
                    mimetype="application/json")
    return (resp)


@app.route("/")
def home():
    return render_template('hello.html')


if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=81, debug=False)
    #roll_for_armour('hard',2)