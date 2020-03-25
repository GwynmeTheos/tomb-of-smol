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
            engine.StateController(user)
                
        elif selection == 'l':
            user = LoadGame()
            engine.StateController(user)
            continue
                
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
    print("What's your name: ", end="")
    name = input()
    
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

    selection = str(input()).lower()
    while True:
        if selection == 'w':
            playerClass = "Wizard"
            weapon = "Staff"
            armor = "Robes"
            accessory = ""
            skills = {"Skills"}
            strength = 1
            dexterity = 1
            intelligence = 3
            baseHP = 6
            baseMP = 12
            break

        elif selection == 'f':
            playerClass = "Fighter"
            weapon = "Short Sword"
            armor = ""
            accessory = "Shield"
            skills = {"Cleave"}
            strength = 2
            dexterity = 2
            intelligence = 1
            baseHP = 12
            baseMP = 6
            break
        
        elif selection == 't':
            playerClass = "Thief"
            weapon = "Dagger"
            armor = ""
            accessory = "Buckler"
            skills = {"Parry", "Lockpick"}
            strength = 1
            dexterity = 2
            intelligence = 2
            baseHP = 8
            baseMP = 8
            break

        elif selection == 'c':
            playerClass = "Cleric"
            weapon = "Mace"
            armor = ""
            accessory = "Holy Symbol"
            skills = {"Cure Wounds"}
            strength = 2
            dexterity = 1
            intelligence = 2
            baseHP = 8
            baseMP = 10
            break
        
        elif selection == 'a':
            playerClass = "Archer"
            weapon = "Short Bow"
            armor = ""
            accessory = "Arrows"
            skills = {"Scout"}
            strength = 1
            dexterity = 3
            intelligence = 1
            baseHP = 10
            baseMP = 8
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

    selection = str(input()).lower()
    while True:
        if selection == 'e':
            difficulty = "easy"
            break
        
        elif selection == 'n':
            difficulty = "normal"
            break
        
        elif selection == 'h':
            difficulty = "hard"
            break
        
        else: 
            continue

    newPlayer = player.Player(name, playerClass, difficulty, 1, strength, dexterity, intelligence, baseHP, baseHP, baseMP, baseMP, skills, weapon, armor, accessory)
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

    selection = str(input())
    while True:
        if selection == "0":
            user = player.Player(savedata0['name'], savedata0['playerClass'], savedata0['difficulty'], savedata0['level'], savedata0['maxHP'], savedata0['currentHP'], savedata0['maxMP'], savedata0['currentMP'], savedata0['strength'], savedata0['dexterity'], savedata0['intelligence'], set(savedata0['skills']), savedata0['weapon'], savedata0['armor'], savedata0['accessory'])
            return user
        elif selection == "1":
            user = player.Player(savedata1['name'], savedata1['playerClass'], savedata1['difficulty'], savedata1['level'], savedata1['maxHP'], savedata1['currentHP'], savedata1['maxMP'], savedata1['currentMP'], savedata1['strength'], savedata1['dexterity'], savedata1['intelligence'], set(savedata1['skills']), savedata1['weapon'], savedata1['armor'], savedata1['accessory'])
            return user        
        elif selection == "2":
            user = player.Player(savedata2['name'], savedata2['playerClass'], savedata2['difficulty'], savedata2['level'], savedata2['maxHP'], savedata2['currentHP'], savedata2['maxMP'], savedata2['currentMP'], savedata2['strength'], savedata2['dexterity'], savedata2['intelligence'], set(savedata2['skills']), savedata2['weapon'], savedata2['armor'], savedata2['accessory'])
            return user
        elif selection == "3":
            user = player.Player(savedata3['name'], savedata3['playerClass'], savedata3['difficulty'], savedata3['level'], savedata3['maxHP'], savedata3['currentHP'], savedata3['maxMP'], savedata3['currentMP'], savedata3['strength'], savedata3['dexterity'], savedata3['intelligence'], set(savedata3['skills']), savedata3['weapon'], savedata3['armor'], savedata3['accessory'])
            return user
        elif selection == "4":
            user = player.Player(savedata4['name'], savedata4['playerClass'], savedata4['difficulty'], savedata4['level'], savedata4['maxHP'], savedata4['currentHP'], savedata4['maxMP'], savedata4['currentMP'], savedata4['strength'], savedata4['dexterity'], savedata4['intelligence'], set(savedata4['skills']), savedata4['weapon'], savedata4['armor'], savedata4['accessory'])
            return user
        elif selection == "5":
            user = player.Player(savedata5['name'], savedata5['playerClass'], savedata5['difficulty'], savedata5['level'], savedata5['maxHP'], savedata5['currentHP'], savedata5['maxMP'], savedata5['currentMP'], savedata5['strength'], savedata5['dexterity'], savedata5['intelligence'], set(savedata5['skills']), savedata5['weapon'], savedata5['armor'], savedata5['accessory'])
            return user
        else:
            continue

def DataLookup(jsonDict):
    if jsonDict["written"] == False:
        return "No save data."
    else:
        return str(jsonDict["name"]) + " - Level " + str(jsonDict["level"])
