import colorama

class Player():
    name: str = ""
    playerClass: str = ""
    difficulty: str = ""
    level: int = 0
    maxHP: int = 0
    currentHP: int = 0
    maxMP: int = 0
    currentMP: int = 0
    strength: int = 0
    dexterity: int = 0
    intelligence = 0
    skills = {}
    weapon: str = ''
    armor: str = ''
    accessory: str = ''
    experience: int = 0
    inventory = []

    def __init__(self, playerDataDict):
        self.name = playerDataDict["name"]
        self.playerClass = playerDataDict["playerClass"]
        self.difficulty = playerDataDict["difficulty"]
        self.level = playerDataDict["level"]
        self.strength = playerDataDict["strength"]
        self.dexterity = playerDataDict["dexterity"]
        self.intelligence = playerDataDict["intelligence"]
        self.maxHP = playerDataDict["baseHP"] * self.level
        self.currentHP = playerDataDict["currentHP"]
        self.maxMP = playerDataDict["baseMP"] * self.level
        self.currentMP = playerDataDict["currentMP"]
        self.skills = playerDataDict["skills"]
        self.weapon = playerDataDict["weapon"]
        self.armor = playerDataDict["armor"]
        self.accessory = playerDataDict["accessory"]
        self.experience = playerDataDict["experience"]
        self.inventory = playerDataDict["inventory"]

    

