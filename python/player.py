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

    def __init__(self, _name, _playerClass, _difficulty, _level, _maxHP, _currentHP, _maxMP, _currentMP, _strength, _dexterity, _intelligence, _skills, _weapon, _armor, _accessory):
        self.name = _name
        self.playerClass = _playerClass
        self.difficulty = _difficulty
        self.level = _level
        self.maxHP = _maxHP
        self.currentHP = _currentHP
        self.maxMP = _maxMP
        self.currentMP = _currentMP
        self.strength = _strength
        self.dexterity = _dexterity
        self.intelligence = _intelligence
        self.skills = _skills
        self.weapon = _weapon
        self.armor = _armor
        self.accessory = _accessory

