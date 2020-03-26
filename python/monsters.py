import colorama, player, random

class Monster():
    name: str = ""
    strength: int = 0
    dexterity: int = 0
    intelligence: int = 0
    currentHP: int = 0
    currentMP: int = 0
    weapon: str = ""
    armor: str = ""
    accessory: str = ""
    
    def __init__(self, strength: int, dexterity: int, intelligence: int):
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence

    def BehaviourTree(self):
        pass

    def Attack(self):
        pass

    def Death(self):
        print("Die monster, you do not belong in this world.")
        pass


class Goblin(Monster):
    
    def __init__(self, playerLevel):
        self.name = "Goblin"
        super().__init__(2 + playerLevel, 2 + playerLevel, 1 + playerLevel)
        self.currentHP = random.randrange(4, 7) * playerLevel
        self.currentMP = random.randrange(2, 4) * playerLevel

    def BehaviourTree(self):
        pass

    def Attack(self):
        pass

    def Death(self):
        pass

