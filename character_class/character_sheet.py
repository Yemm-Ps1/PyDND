import dnd_classes as DndClass




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