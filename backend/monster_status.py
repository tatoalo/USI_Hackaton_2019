import numpy as np
import json
import random

json_file ='backend/monster_status.json' #Path configuration file
range_value = 6 #Margin randon value
minimun_damage = 1 #Minimun damage
max_damage = 50 #Maximun damage
critical = 0.2 #Probability of a critical damage
desviation = 1 #Parameter mu for the gaussian distribution

def compile():
    """
    Compile the configuration file.
    """
    try:
        with open(json_file, 'r') as myfile:
            data=myfile.read()
        data = json.loads(data)
        correct = True
        for i in data.keys():
            aux =0
            for j in data[i].keys():
                aux += data[i][j]
            if aux != 100:
                correct = False
                print("Error, values are not correct")
    except:
         correct = False
         print("Format error")
    return  (data, correct)

def damage(id,pollution):
    """
    Give a damage value between minimun_damage and max_damage.
    """
    NO2 = 0.01
    NO = 0.01
    O3 = 0.01
    PM10 = 0.01
    data, correct = compile()
    id= str(id)
    #if compile fail the program take values near to zero
    if correct:
        NO2 = float(data[id]["NO2"])/100
        NO = float(data[id]["NO"])/100
        O3 = float(data[id]["O3"])/100
        PM10 = float(data[id]["PM10"])/100
    value = int(NO2*pollution["NO2"] + NO*pollution["NO"]  + O3*pollution["O3"]  + PM10*pollution["PM10"])
    value = random.randint(value - range_value, value + range_value)
    if value < minimun_damage:
        value = minimun_damage
    elif value > max_damage:
        valye = max_damage
    value = random.choices([value,max_damage], [1 -critical,critical])[0]
    return value


#damage(1,{"NO2":10.0, "NO":2.0,"O3":20.0,"PM10":10.0})
#damage(1,{"NO2":100.0, "NO":100.0,"O3":100.0,"PM10":100.0})

def gaussian(x, mu, sig):
    """
    Gaussian distribution
    url: https://stackoverflow.com/questions/14873203/plotting-of-1-dimensional-gaussian-distribution-function
    """
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

#monster1 = {"id":1,"icon":"ja","name":"pollutionGuy","lvl":3}
#monster2 = {"id":2,"icon":"ja","name":"pollutionGuy","lvl":5}
#monster3 = {"id":3,"icon":"ja","name":"pollutionGuy","lvl":6}
#monster4 = {"id":4,"icon":"ja","name":"pollutionGuy","lvl":3}
#monster5 = {"id":5,"icon":"ja","name":"pollutionGuy","lvl":1}
#list_monsters = [monster1,monster2,monster3,monster4,monster5]

def choose_monster(list_monsters,level):
    """
    Choose a monster depending the levels of the monsters and the level of the player.
    """
    level_list = []
    for i in list_monsters:
        level_list.append(i["lvl"])
    level_list = gaussian(np.array(level_list),level,desviation)
    return random.choices(list_monsters,level_list)