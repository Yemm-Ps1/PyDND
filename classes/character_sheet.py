import dnd_classes as DndClass
import math

class Stats():
    def __init__(
        self,
        strength = 10,
        dexterity = 10,
        constitution = 10,
        intelligence = 10,
        wisdom = 10,
        charisma = 10,
    ):
        self._strength = strength
        self._dexterity = dexterity
        self._constitution = constitution
        self._intelligence = intelligence
        self._wisdom = wisdom
        self._charisma = charisma

    def _get_mod(self, stat):
        return math.floor(stat/2)-5
    def get_strength(self):
        return self._strength
    def set_strength(self, x):
        self._strength = x
    def get_dexterity(self):
        return self._dexterity
    def set_dexterity(self, x):
        self._dexterity = x
    def get_constitution(self):
        return self._constitution
    def set_constitution(self, x):
        self._constitution = x
    def get_intelligence(self):
        return self._intelligence
    def set_intelligence(self, x):
        self._intelligence = x
    def get_wisdom(self):
        return self._wisdom
    def set_wisdom(self, x):
        self._wisdom = x
    def get_charisma(self):
        return self._charisma
    def set__charisma(self, x):
        self._charisma = x
    def get_strength_modifier(self):
        return self._get_mod(self._strength)
    def get_dexterity_modifier(self):
        return self._get_mod(self._dexterity)
    def get_constitution_modifier(self):
        return self._get_mod(self._constitution)
    def get_intelligence_modifier(self):
        return self._get_mod(self._intelligence)
    def get_wisdom_modifier(self):
        return self._get_mod(self._wisdom)
    def get_charisma_modifier(self):
        return self._get_mod(self._charisma)

class Skills():
    def __init__(
        self,
        strength = 10,
        dexterity = 10,
        constitution = 10,
        intelligence = 10,
        wisdom = 10,
        charisma = 10,
    ):
        self._strength = strength
        self._dexterity = dexterity
        self._constitution = constitution
        self._intelligence = intelligence
        self._wisdom = wisdom
        self._charisma = charisma

class Proficiencies():
    def __init__(self):
        pass

class CharacterSheet():
    def __init__(self, sheet_data):
        self._proficiencies = Proficiencies(sheet_data)
        self._class = DndClass(sheet_data)
        self._stats = Stats()
        self._skills = Skills()

a = CharacterSheet()
print(a._stats.get_dexterity())