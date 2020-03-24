import os, colorama, keyboard, engine, player

def Start():
    os.system("CLS")

    file = open("python\\screens\\start-screen.txt", "r+", encoding="UTF-8")

    for line in file.readlines():
        print(line, end="")
    print()
    print("(" + colorama.Style.BRIGHT +"N" + colorama.Style.RESET_ALL + ")ew Game")
    print("(" + colorama.Style.BRIGHT +"L" + colorama.Style.RESET_ALL + ")oad Game")
    print("(" + colorama.Style.BRIGHT +"O" + colorama.Style.RESET_ALL + ")ptions")
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
            # user = LoadGame()
            # engine.StateController(user)
            continue

        elif selection == 'o':
            Options()
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
    pass

def Options():
    os.system("CLS")

