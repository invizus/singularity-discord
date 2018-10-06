#!/usr/bin/python3
import json
import math

LANG = 'EN'
jsonFile = 'prof.json'

labelLevelEN = " level: "
labelExpEN = " Exp: "

dataFormatlevel = 'level'
dataFormatexp = 'exp'

def loadProfs():
    profFile = open(jsonFile)
    global jsonData
    jsonData = json.loads(profFile.read())
    profFile.close()

def writeProfs():
    with open(jsonFile, 'w') as f:
        f.write(json.dumps(jsonData))

def getProf(user):
    loadProfs()
    lama = []
    for key, value in jsonData[user].items():
        nextLevel = 2**(int(value[dataFormatlevel])+1)
        lama.append(key + labelLevelEN + str(value[dataFormatlevel]) + labelExpEN + str(value[dataFormatexp]) + "/" + str(nextLevel) + '\n')
    lamb = ''.join(lama)
    return lamb

def addExp(user, prof, inc):
    loadProfs()
    results = ""
    currentLevel = jsonData[user][prof][dataFormatlevel]
    jsonData[user][prof][dataFormatexp] += int(inc)
#    jsonData[user][prof][dataFormatexp] = jsonData[user][prof][dataFormatexp] + int(inc)
    currentExp = jsonData[user][prof][dataFormatexp]
    newLevel = int(math.log(currentExp,2))
    jsonData[user][prof][dataFormatlevel] = newLevel
    if newLevel > currentLevel:
      results = "YAY Level up! Now level: " + str(newLevel) + " "
    writeProfs()
    return results

def addProf(user, newprof):
    loadProfs()
    results = "OK"
    if newprof in jsonData[user]:
        results = "already has skill"
    else:
        jsonData[user].update({newprof: {'Title': '', dataFormatexp : 0, dataFormatlevel: 0}})
        writeProfs()
    return results

def initiate(user):
    loadProfs()
    results = ""
    if user in jsonData:
        results = "Exists"
    else:
        jsonData.update({user: {}})
        results = "OK"
    writeProfs()
    return results
