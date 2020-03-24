import main, inventory, maps, monsters, player, shop, os

def StateController(player):
    os.system("CLS")
    for x in player:
        print(x)