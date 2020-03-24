import colorama

class Player():
    name = ""
    playerClass = ""
    difficulty = ""
    level = 1
    maxHP = 10
    currentHP = 10
    maxMP = 10
    currentMP = 10
    strength = 2
    dexterity = 2
    intelligence = 2
    skills = {}
    weapon = ''
    armor = ''
    accessory = ''

    def __init__(self, _name, _playerClass, _difficulty, _level, _strength, _dexterity, _intelligence, _baseHP, _currentHP, _baseMP, _currentMP, _skills, _weapon, _armor, _accessory):
        self.name = _name
        self.playerClass = _playerClass
        self.difficulty = _difficulty
        self.level = _level
        self.strength = _strength
        self.dexterity = _dexterity
        self.intelligence = _intelligence
        self.maxHP = _baseHP * self.level
        self.currentHP = _currentHP
        self.maxMP = _baseMP * self.level
        self.currentMP = _currentMP
        self.skills = _skills
        self.weapon = _weapon
        self.armor = _armor
        self.accessory = _accessory

