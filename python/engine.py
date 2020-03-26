import main, events, monsters, player, os, json

def StateController(player):
    os.system("CLS")
    print("Under construction.")

def GenerateEvent():
    pass

def MapMovement():
    pass

def GetItemData(key, mode):
    jsonFile = open("\\python\\tables\\" + mode + ".json", "r")
    itemList = json.load(jsonFile)

    return itemList[key]

def BattleSystem(playerObject, monsterObject):
    pass