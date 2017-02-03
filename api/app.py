from flask import *
import flask
import random
import json
import os
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:8000"}})
@app.route("/roll",methods=['GET'])
def get_loot():


    #sampleMassDist = [0.8, 0.11, 0.05, 0.03, 0.01, 0.0]
    # assume sum of bias is 1
    def roll(massDist):
        randRoll = random.random()  # in [0,1)
        sum = 0
        result = 0

        for mass in massDist:
            sum += mass
            if randRoll < sum:
                return result
            result += 1
    def sec_perk(star_count,labels):
        print("sec roll")
        if star_count ==0:
            print(0)
            return 'none'
        if star_count==1:
            print(1)
            return labels[roll([0.98,0.02])]
        if star_count==2:
            print(2)
            return labels[roll([0.99,0.001])]
        if star_count==3:
            print(3)
            return labels[roll([0.999,0.0001])]
        if star_count==4:
            print(4)
            return labels[roll([0.9999,0.0001])]



    weapons = {}

    loot_item_schema = {"primaryperk": {},
                        "secondary_perk":{},
                        "weaponname":"",
                        "weapon class":"",
                        "weaponfamily":"",
                        "baseproperties":"",
                        "basedamage":"",
                        "specialproperties":"",
                        "basevalue":"",
                        "weight":""}

    difficulty = request.args.get('difficulty')
    item_count = request.args.get('item_count')
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    # melee or ranged?
    typeprobs = [0.5,0.5]

    typelabels = ["Melee weapons","Ranged weapons"]
    typeresult = typelabels[roll(typeprobs)]
    #print(typeresult)

    #load up the difficulty table for perks
    diff_tables = os.path.join(SITE_ROOT, "static", "difficultytables.json")
    difficulty_table = json.load(open(diff_tables))
    # load up perk table
    perk_json = os.path.join(SITE_ROOT, "static", "perks.json")
    perks = json.load(open(perk_json))
    #pprint(str(perks).replace(u"\u2018", "'").replace(u"\u2019", "'"))
    #load up the weapons list
    weapon_json = os.path.join(SITE_ROOT, "static", "weapons.json")
    weapons = json.load(open(weapon_json))


    diff = difficulty_table[0][difficulty]
    dist = []
    labels = []

    for value in diff:
        dist.append(diff[value])
        labels.append(value)
    pperk_rarity_result = labels[roll(dist)]

    #draw a weapon
    base_weapon_set = weapons[typeresult]
    draw = random.choice(list(base_weapon_set.keys()))
    base_weapon = base_weapon_set[draw]
    #print(base_weapon)
    weapon_class = base_weapon['Weapon Class']


    secondary_perk = 'none'
    sec_perk_result = 'none'
    primary_perk_set = {}
    sec_perk_set = {}
    base_weapon['secondaryperk']='none'
    base_weapon['primaryperk'] = 'none'
    base_weapon['pperkrarity'] = 'none'
    base_weapon['sperkrarity'] = 'none'
    base_weapon['pperkvalue'] = '0 GP'
    base_weapon['sperkvalue'] = '0 GP'
    if pperk_rarity_result != 'none':
        primary_perk_set = perks[pperk_rarity_result]
        primary_perk = random.choice(list(primary_perk_set[weapon_class].keys()))
        base_weapon['primaryperk'] = primary_perk
        base_weapon['pperkrarity'] = pperk_rarity_result
        base_weapon['pperkeffect'] = primary_perk_set[weapon_class][primary_perk]['Effect']
        base_weapon['pperkvalue'] = primary_perk_set[weapon_class][primary_perk]['Value']

        # Check for second perk roll

        mp_stars = primary_perk.count('*')
        sec_perk_result = sec_perk(mp_stars,labels)

        if sec_perk_result!='none':
            #print("second perk")
            sec_perk_set = perks[sec_perk_result]
            secondary_perk = random.choice(list(sec_perk_set[weapon_class].keys()))
            base_weapon['secondaryperk'] = secondary_perk
            base_weapon['sperkrarity'] = sec_perk_result
            base_weapon['sperkeffect'] = sec_perk_set[weapon_class][secondary_perk]['Effect']
            base_weapon['sperkvalue'] = sec_perk_set[weapon_class][secondary_perk]['Value']
            #print(secondary_perk)


    else:
        primary_perk = 'none'
    #print(perk_rarity_result)
    #print("ALL G")





    if base_weapon['primaryperk'] != 'none':
        b = base_weapon['primaryperk']
    else:
        b = ''
    if base_weapon['secondaryperk'] != 'none':
        m = base_weapon['secondaryperk']
    else:
        m = ''
    draw_weapon_name = b+' '+m+' '+base_weapon['Weapon Name']
    draw_weapon_name = draw_weapon_name.replace("*", "")
    base_weapon['drawname'] = draw_weapon_name
    #need to fix here -- perkvalues may not exist
    if 'SP' in base_weapon['Base Value']:
        if int( base_weapon['pperkvalue'].split()[0])+ int( base_weapon['sperkvalue'].split()[0])==0:
            base_weapon['totalvalue'] = base_weapon['Base Value']
        else:
            base_weapon['totalvalue'] = str(int( base_weapon['pperkvalue'].split()[0])+ int( base_weapon['sperkvalue'].split()[0]))+" GP, "+base_weapon['Base Value']
    else:
        base_weapon['totalvalue'] = str(int(base_weapon['Base Value'].split()[0])+int( base_weapon['pperkvalue'].split()[0])+ int( base_weapon['sperkvalue'].split()[0]))+" GP"

    weapon_json = json.dumps(base_weapon)
    #print(weapon_json)
    resp = Response(response=weapon_json,
                    status=200,
                    mimetype="application/json")
    return (resp)

@app.route("/weapons")
def get_weapon_stats():
    return "501 Not Implemented"
@app.route("/perks")
def get_perk_stats():
    return "501 Not Implemented"

@app.route("/")
def home():
    return render_template('hello.html')


if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=8080, debug=False)
