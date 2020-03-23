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
    print("Press a highlighted key.")

    while True:
        try:
            if keyboard.is_pressed('n'):
                NewGameStart()
                
            elif keyboard.is_pressed('l'):
                LoadGame()
                continue

            elif keyboard.is_pressed('o'):
                Options()
                continue
                
            elif keyboard.is_pressed('q'):
                return True
        except:
            continue

def NewGameStart():
    os.system("CLS")
    
    print("You wake up in a dimly lit room. Your equipment in tatters and no clear way out.")
    print('An iron door blocks your way, the key rests on a table, and beside it a note that reads: "Good luck."')
    print("You gaze around the room and see a few stations in various states of disrepair.")
    print("You get off the bed and decide to head out. Your adventure begins...")
    print("In the " + colorama.Style.BRIGHT + "Tomb of Smol" + colorama.Style.RESET_ALL + "!")
    print()
    print("(Press ENTER to continue)")
    keyboard.wait("enter")

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
    print("Knows:" + colorama.Fore.GREEN + "Parry," + colorama.Fore.RED + "Lockpick" + colorama.Style.RESET_ALL, end='\n')
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
    playerClass = ""
    while True:
        try:
            if keyboard.is_pressed('w'):
                playerClass = "w"
                break
            elif keyboard.is_pressed('f'):
                playerClass = "f"
                break
            elif keyboard.is_pressed('t'):
                playerClass = "t"
                break
            elif keyboard.is_pressed('c'):
                playerClass = "c"
                break
            elif keyboard.is_pressed('a'):
                playerClass = "a"
                break
        except:
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
    difficulty = ""
    while True:
        try:
            if keyboard.is_pressed('e'):
                difficulty = "easy"
                break
            elif keyboard.is_pressed('n'):
                difficulty = "normal"
                break
            elif keyboard.is_pressed('h'):
                difficulty = "hard"
                break
        except:
            continue

    newPlayer = player.Player(name, playerClass, difficulty)
    engine.StateController(newPlayer)

def LoadGame():
    pass

def Options():
    os.system("CLS")

