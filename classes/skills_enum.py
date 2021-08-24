from enum import Enum

class Skills(Enum):
    ACROBATICS = 0
    ANIMAL_HANDLING = 1
    ARCANA = 2
    ATHLETICS = 3
    DECEPTION = 4
    HISTORY = 5
    INSIGHT = 6
    INTIMIDATION = 7
    INVESTIGATION = 9
    MEDICINE = 9
    NATURE = 10
    PERCEPTION = 11
    PERFORMANCE = 12
    PERSUASION = 13
    RELIGION = 14
    SLEIGHT_OF_HAND = 15
    STEALTH = 17
    SURVIVAL = 18

    def is_str(self):
        return self is Skills.ATHLETICS

    def is_dex(self):
        return self in [Skills.ACROBATICS, Skills.SLEIGHT_OF_HAND, Skills.STEALTH]


class CharacterSheet:
    def __init__(self):
        prof_mod = {Skills.ATHLETICS: 1 }
        for s in filter(lambda s: s.is_dex(), Skills):
            print(s)
