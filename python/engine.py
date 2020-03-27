import main, events, monsters, player, os, json, colorama

def StateController(playerObject):
    currentState = "StarterRoom"

    while True:
        if currentState == "StarterRoom":
            currentState, playerObject = StarterRoom(playerObject)
            continue

        elif currentState == "Map":
            currentState, playerObject = MapMovement(playerObject)
            continue

        elif currentState == "Upgrade":
            currentState, playerObject = UpgradeFacilities(playerObject)
            continue
            
        elif currentState == "Inventory":
            playerObject.DiplayInventory()
            currentState = "StarterRoom"
            continue

        elif currentState == "SaveQuit":
            break
        
        else:
            currentState = "StarterRoom"
            continue
    
    return playerObject


def StarterRoom(playerObject):
    os.system("CLS")
    print("You take a look around your room.")
    print()
    print("Your forge is currently level: " + colorama.Style.BRIGHT + str(playerObject.forgeLevel) + colorama.Style.RESET_ALL)
    print("Your wardrobe is currently level: " + colorama.Style.BRIGHT + str(playerObject.wardrobeLevel) + colorama.Style.RESET_ALL)
    print("Your jewelry box is currently level: " + colorama.Style.BRIGHT + str(playerObject.jewelryBoxLevel) + colorama.Style.RESET_ALL)
    print("Your bed is currently level: " + colorama.Style.BRIGHT + str(playerObject.bedLevel) + colorama.Style.RESET_ALL)
    print("Your altar is currently level: " + colorama.Style.BRIGHT + str(playerObject.altarLevel) + colorama.Style.RESET_ALL)
    print()
    print("What would you to do?")
    print()
    print("(" + colorama.Style.BRIGHT + "W" + colorama.Style.RESET_ALL + ") Brave the Tomb", end="   ")
    print("(" + colorama.Style.BRIGHT + "U" + colorama.Style.RESET_ALL + ")pgrade facilities", end="   ")
    print("Check your (" + colorama.Style.BRIGHT + "I" + colorama.Style.RESET_ALL + ")nventory", end="   ")
    print("Save and (" + colorama.Style.BRIGHT + "Q" + colorama.Style.RESET_ALL + ")uit", end="\n")


    while True:
        selection = str(input()).lower()

        if selection == "w":
            return "Map"
        elif selection == "u":
            return "Upgrade"
        elif selection == "i":
            return "Inventory"
        elif selection == "q":
            return "SaveQuit"
        else:
            continue

def GenerateEvent(playerObject):
    pass

def MapMovement(playerObject):
    return ("StarterRoom", playerObject)

def GetItemData(key, mode):
    jsonFile = open("python\\tables\\" + mode + ".json", "r")
    itemList = json.load(jsonFile)

    return itemList[key]

def BattleSystem(playerObject, monsterObject):
    pass

def UpgradeFacilities(playerObject):
    return ("StarterRoom", playerObject)