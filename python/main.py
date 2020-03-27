import os, colorama, engine, player, json

def Start():
    os.system("CLS")

    file = open("python\\screens\\start-screen.txt", "r+", encoding="UTF-8")

    for line in file.readlines():
        print(line, end="")
    print()
    print("(" + colorama.Style.BRIGHT +"N" + colorama.Style.RESET_ALL + ")ew Game")
    print("(" + colorama.Style.BRIGHT +"L" + colorama.Style.RESET_ALL + ")oad Game")
    print("(" + colorama.Style.BRIGHT +"Q" + colorama.Style.RESET_ALL + ")uit")
    print()
    print("Input a highlighted key.")
    print()

    selection = str(input()).lower()
    while True:
        if selection == 'n':
            user = NewGameStart()
            user = engine.StateController(user)
            SaveGame(user)

        elif selection == 'l':
            user = LoadGame()
            user = engine.StateController(user)
            SaveGame(user)
                
        elif selection == 'q':
            exit()
        
        else: 
            continue

def NewGameStart():
    os.system("CLS")
    
    print("You wake up in a dimly lit room. Your equipment in tatters and an iron door blocks your way.")
    print("You try to remember anything as you lay down in the bed.")
    print("It eventually comes back to you...")
    print("You died. But instead, you woke up in this bed.")
    print("You gaze around the room and see a few stations in various states of disrepair.")
    print("You get off the bed and decide to head out.")
    print("You might be small, but you're brave.")
    print("But will it be enough to defeat...")
    print("The dreadful " + colorama.Style.BRIGHT + "Tomb of Smol" + colorama.Style.RESET_ALL + "!")
    print()
    print("(Press ENTER to continue)")
    input()

    os.system("CLS")
    newPlayerDict = {}
    print("What's your name: ", end="")
    newPlayerDict["name"] = input()

    
    os.system("CLS")
    print("Choose your class:")
    print()
    print("("+ colorama.Style.BRIGHT + "W" + colorama.Style.RESET_ALL +")izard", end='\n')
    print("Starts with: Staff, Robes", end='\n')
    print("Knows: " + colorama.Fore.RED + "Fireball" + colorama.Style.RESET_ALL, end='\n')
    print("High damage, but low survivability.", end='\n')
    print()
    print("("+ colorama.Style.BRIGHT + "F" + colorama.Style.RESET_ALL +")ighter", end='\n')
    print("Starts with: Short Sword, Shield", end='\n')
    print("Knows: " + colorama.Fore.RED + "Cleave" + colorama.Style.RESET_ALL, end='\n')
    print("All rounder, melee fighter.", end='\n')
    print()
    print("("+ colorama.Style.BRIGHT + "T" + colorama.Style.RESET_ALL +")hief", end='\n')
    print("Starts with: Dagger, Buckler", end='\n')
    print("Knows:" + colorama.Fore.GREEN + "Parry" + colorama.Style.RESET_ALL + ", " + colorama.Fore.RED + "Lockpick" + colorama.Style.RESET_ALL, end='\n')
    print("Highly technical playstyle.", end='\n')
    print()
    print("("+ colorama.Style.BRIGHT + "C" + colorama.Style.RESET_ALL +")leric", end='\n')
    print("Starts with: Mace, Holy Symbol", end='\n')
    print("Knows: " + colorama.Fore.RED + "Cure Wounds" + colorama.Style.RESET_ALL, end='\n')
    print("Healer capable of dealing damage.", end='\n')
    print()
    print("("+ colorama.Style.BRIGHT + "A" + colorama.Style.RESET_ALL +")rcher", end='\n')
    print("Starts with: Short Bow, Arrows", end='\n')
    print("Knows:" + colorama.Fore.GREEN + "Scout" + colorama.Style.RESET_ALL, end='\n')
    print("Versatile class, can see enemy information.", end='\n')
    print()

    while True:
        selection = str(input()).lower()
        if selection == 'w':
            newPlayerDict["playerClass"] = "Wizard"
            newPlayerDict["weapon"] = "Staff"
            newPlayerDict["armor"] = "Robes"
            newPlayerDict["accessory"] = ""
            newPlayerDict["skills"] = {"Fireball"}
            newPlayerDict["strength"] = 1
            newPlayerDict["dexterity"] = 1
            newPlayerDict["intelligence"] = 3
            newPlayerDict["baseHP"] = 6
            newPlayerDict["baseMP"] = 12
            newPlayerDict["currentHP"] = newPlayerDict["baseHP"]
            newPlayerDict["currentMP"] = newPlayerDict["baseMP"]
            break

        elif selection == 'f':
            newPlayerDict["playerClass"] = "Fighter"
            newPlayerDict["weapon"] = "Short Sword"
            newPlayerDict["armor"] = ""
            newPlayerDict["accessory"] = "Shield"
            newPlayerDict["skills"] = {"Cleave"}
            newPlayerDict["strength"] = 2
            newPlayerDict["dexterity"] = 2
            newPlayerDict["intelligence"] = 1
            newPlayerDict["baseHP"] = 12
            newPlayerDict["baseMP"] = 6
            newPlayerDict["currentHP"] = newPlayerDict["baseHP"]
            newPlayerDict["currentMP"] = newPlayerDict["baseMP"]
            break
        
        elif selection == 't':
            newPlayerDict["playerClass"] = "Thief"
            newPlayerDict["weapon"] = "Dagger"
            newPlayerDict["armor"] = ""
            newPlayerDict["accessory"] = "Buckler"
            newPlayerDict["skills"] = {"Parry", "Lockpick"}
            newPlayerDict["strength"] = 1
            newPlayerDict["dexterity"] = 2
            newPlayerDict["intelligence"] = 2
            newPlayerDict["baseHP"] = 8
            newPlayerDict["baseMP"] = 8
            newPlayerDict["currentHP"] = newPlayerDict["baseHP"]
            newPlayerDict["currentMP"] = newPlayerDict["baseMP"]
            break

        elif selection == 'c':
            newPlayerDict["playerClass"] = "Cleric"
            newPlayerDict["weapon"] = "Mace"
            newPlayerDict["armor"] = ""
            newPlayerDict["accessory"] = "Holy Symbol"
            newPlayerDict["skills"] = {"Cure Wounds"}
            newPlayerDict["strength"] = 2
            newPlayerDict["dexterity"] = 1
            newPlayerDict["intelligence"] = 2
            newPlayerDict["baseHP"] = 8
            newPlayerDict["baseMP"] = 10
            newPlayerDict["currentHP"] = newPlayerDict["baseHP"]
            newPlayerDict["currentMP"] = newPlayerDict["baseMP"]
            break
        
        elif selection == 'a':
            newPlayerDict["playerClass"] = "Archer"
            newPlayerDict["weapon"] = "Short Bow"
            newPlayerDict["armor"] = ""
            newPlayerDict["accessory"] = "Arrows"
            newPlayerDict["skills"] = {"Scout"}
            newPlayerDict["strength"] = 1
            newPlayerDict["dexterity"] = 3
            newPlayerDict["intelligence"] = 1
            newPlayerDict["baseHP"] = 10
            newPlayerDict["baseMP"] = 8
            newPlayerDict["currentHP"] = newPlayerDict["baseHP"]
            newPlayerDict["currentMP"] = newPlayerDict["baseMP"]
            break

        else: 
            continue

    os.system("CLS")
    print("Choose the game difficulty:")
    print()
    print("("+ colorama.Style.BRIGHT + "E" + colorama.Style.RESET_ALL +")asy", end='\n')
    print("0.8x enemy scaling. Less rewards.", end='\n')
    print()
    print("("+ colorama.Style.BRIGHT + "N" + colorama.Style.RESET_ALL +")normal", end='\n')
    print("Normal enemy scaling. Normal rewards.", end='\n')
    print()
    print("("+ colorama.Style.BRIGHT + "H" + colorama.Style.RESET_ALL +")ard", end='\n')
    print("1.2x enemy scaling. More rewards.", end='\n')
    print()

    while True:
        selection = str(input()).lower()
        if selection == 'e':
            newPlayerDict["difficulty"] = "easy"
            break
        
        elif selection == 'n':
            newPlayerDict["difficulty"] = "normal"
            break
        
        elif selection == 'h':
            newPlayerDict["difficulty"] = "hard"
            break
        
        else: 
            continue
    
    newPlayerDict["level"] = 1
    newPlayerDict["experience"], newPlayerDict["gold"] = 0, 0
    newPlayerDict["inventory"] = []
    newPlayerDict["forgeLevel"], newPlayerDict["wardrobeLevel"], newPlayerDict["jewelryBoxLevel"] = 0, 0, 0
    newPlayerDict["bedLevel"], newPlayerDict["altarLevel"] = 0, 0

    newPlayer = player.Player(newPlayerDict)
    return newPlayer

def LoadGame():
    os.system("CLS")

    savefile0 = open("python\\saves\\save0", "r")
    savedata0 = json.load(savefile0)
    savefile1 = open("python\\saves\\save1", "r")
    savedata1 = json.load(savefile1)
    savefile2 = open("python\\saves\\save2", "r")
    savedata2 = json.load(savefile2)
    savefile3 = open("python\\saves\\save3", "r")
    savedata3 = json.load(savefile3)
    savefile4 = open("python\\saves\\save4", "r")    
    savedata4 = json.load(savefile4)
    savefile5 = open("python\\saves\\save5", "r")
    savedata5 = json.load(savefile5)

    print("Select a save: ")
    print()
    print("File ("+ colorama.Style.BRIGHT + "0" + colorama.Style.RESET_ALL +")")
    print(DataLookup(savedata0))
    print()
    print("File ("+ colorama.Style.BRIGHT + "1" + colorama.Style.RESET_ALL +")")
    print(DataLookup(savedata1))
    print()
    print("File ("+ colorama.Style.BRIGHT + "2" + colorama.Style.RESET_ALL +")")
    print(DataLookup(savedata2))
    print()
    print("File ("+ colorama.Style.BRIGHT + "3" + colorama.Style.RESET_ALL +")")
    print(DataLookup(savedata3))
    print()
    print("File ("+ colorama.Style.BRIGHT + "4" + colorama.Style.RESET_ALL +")")
    print(DataLookup(savedata4))
    print()
    print("File ("+ colorama.Style.BRIGHT + "5" + colorama.Style.RESET_ALL +")")
    print(DataLookup(savedata5))
    print()

    while True:
        selection = str(input())
        if selection == "0":
            user = player.Player(savedata0)
            return user
        elif selection == "1":
            user = player.Player(savedata1)
            return user
        elif selection == "2":
            user = player.Player(savedata2)
            return user
        elif selection == "3":
            user = player.Player(savedata3)
            return user
        elif selection == "4":
            user = player.Player(savedata4)
            return user
        elif selection == "5":
            user = player.Player(savedata5)
            return user
        else:
            continue

def DataLookup(jsonDict):
    if jsonDict["written"] == False:
        return "No save data."
    else:
        return str(jsonDict["name"]) + " - Level " + str(jsonDict["level"])

def SaveGame(playerObject):
    pass