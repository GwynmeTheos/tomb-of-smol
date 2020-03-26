import colorama, engine, random

class Player():
    name: str = ""
    playerClass: str = ""
    difficulty: str = ""
    
    level: int = 0
    experience: int = 0
    strength: int = 0
    dexterity: int = 0
    intelligence = 0
    
    maxHP: int = 0
    currentHP: int = 0
    maxMP: int = 0
    currentMP: int = 0
    
    skills = {}

    weapon: str = ''
    armor: str = ''
    accessory: str = ''
    inventory = []
    gold: int = 0
    
    forgeLevel: int = 0
    wardrobeLevel: int = 0
    jewelryBoxLevel: int = 0
    bedLevel: int = 0
    altarLevel: int = 0

    damageDie = 0
    resistance = 0

    def __init__(self, playerDataDict):
        self.name = playerDataDict["name"]
        self.playerClass = playerDataDict["playerClass"]
        self.difficulty = playerDataDict["difficulty"]

        self.level = playerDataDict["level"]
        self.experience = playerDataDict["experience"]
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
        self.inventory = playerDataDict["inventory"]
        self.gold = playerDataDict["gold"]

        self.forgeLevel = playerDataDict["forgeLevel"]
        self.wardrobeLevel = playerDataDict["wardrobeLevel"]
        self.jewelryBoxLevel = playerDataDict["jewelryBoxLevel"]
        self.bedLevel = playerDataDict["bedLevel"]
        self.altarLevel = playerDataDict["alterLevel"]

        if self.weapon != "":
            self.damageDie = engine.GetItemData(self.weapon, "weapon")
        else:
            self.damageDie = 2
        if self.armor != "":
            self.resistance += engine.GetItemData(self.armor, "armor")
        else:
            self.resistance += 0
        if self.accessory != "":
            self.resistance += engine.GetItemData(self.accessory, "accessory")
        else:
            self.resistance += 2
    
    def Attack(self):
        pass

    def TakeDamage(self, damage):
        damageTaken = (damage - self.resistance)
        
        if damageTaken > 0:
            self.currentHP -= damageTaken
        else:
            self.currentHP -= 0

        return damageTaken

    def UseSkill(self):
        pass
