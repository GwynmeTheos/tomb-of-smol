import colorama, player, random, engine

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
    
    damageDie: int = 0
    resistance: int = 0
    
    def __init__(self, strength: int, dexterity: int, intelligence: int):
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence

    def BehaviourTree(self):
        pass

    def Attack(self):
        pass

    def TakeDamage(self):
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
        
        self.weapon = random.choice(["Club", "Crude Bow"])
        self.armor = random.choice(["Loincloth", ""])
        self.accessory = random.choice(["", "", "", "Tribal Ornament"])

        self.damageDie = engine.GetItemData(self.weapon, "weapon")
        if self.armor != "":
            self.resistance = engine.GetItemData(self.armor, "armor")
        if self.accessory == "Tribal Ornament":
            self.resistance += engine.GetItemData(self.accessory, "accessory")

    def BehaviourTree(self):
        return self.Attack()

    def Attack(self):
        if self.weapon == "Club":
            attackDamage = random.randrange(1, self.damageDie + 1) + self.strength
        elif self.weapon == "Crude Bow":
            attackDamage = random.randrange(1, self.damageDie + 1) + self.dexterity
        
        return attackDamage

    def TakeDamage(self, damage):
        damageTaken = (damage - self.resistance)
        
        if damageTaken > 0:
            self.currentHP -= damageTaken
        else:
            self.currentHP -= 0

        return damageTaken

    def Death(self):
        gold = random.randrange(0, 11)
        item = random.choice(["", "", "", self.weapon, self.armor, self.accessory])
        experience = 5
        
        return (gold, item, experience)
