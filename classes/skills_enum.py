from enum import Enum, auto
import math

class Ability(Enum):
    Str = auto()
    Dex = auto()
    Con = auto()
    Int = auto()
    Wis = auto()
    Cha = auto()


class Stats():
    def __init__(self):
        self.ability_scores = {
            Ability.Str : [10, False],
            Ability.Dex : [10, False],
            Ability.Con : [10, False],
            Ability.Int : [10, False],
            Ability.Wis : [10, False],
            Ability.Cha : [10, False]
        }

    def _get_mod(self, ability_type: Ability):
        return math.floor(ability_type[0]/2)-5

    def _set_ability(self, ability_type: Ability, score, is_proficient):
        self.ability_scores[ability_type][0] = self.ability_scores[ability_type][0] if score is None else score
        self.ability_scores[ability_type][1] = self.ability_scores[ability_type][1] if is_proficient is None else is_proficient

    def set_strength(self, score: int = None, is_proficient: bool = None):
        self._set_ability(Ability.Str, score, is_proficient)

    def get_strength(self):
        return self.ability_scores[Ability.Str]

    def get_strength_modifier(self):
        return self._get_mod(self.ability_scores[Ability.Str])

    def set_dexterity(self, x):
        self._dexterity = x
    def get_dexterity(self):
        return self._dexterity
    def get_dexterity_modifier(self):
        return self._get_mod(self._dexterity)

    def set_constitution(self, x):
        self._constitution = x
    def get_constitution(self):
        return self._constitution
    def get_constitution_modifier(self):
        return self._get_mod(self._constitution)

    def set_intelligence(self, x):
        self._intelligence = x
    def get_intelligence(self):
        return self._intelligence
    def get_intelligence_modifier(self):
        return self._get_mod(self._intelligence)

    def set_wisdom(self, x):
        self._wisdom = x
    def get_wisdom(self):
        return self._wisdom
    def get_wisdom_modifier(self):
        return self._get_mod(self._wisdom)

    def set__charisma(self, x):
        self._charisma = x
    def get_charisma(self):
        return self._charisma
    def get_charisma_modifier(self):
        return self._get_mod(self._charisma)



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
        pass


stats = Stats
stats.set_strength(5, True)
