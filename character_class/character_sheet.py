import dnd_classes as DndClass
from sheet_enums import *
import math



class SheetData():
    def __init__(self, dnd_class: list = [DndClass.Rogue(1)]):
        self.classes = dnd_class
        self.ability_scores = {
            Ability.STR : {"Value" : 10, "Proficient" : self._get_class_proficiency(Ability.STR)},
            Ability.DEX : {"Value" : 10, "Proficient" : self._get_class_proficiency(Ability.DEX)},
            Ability.CON : {"Value" : 10, "Proficient" : self._get_class_proficiency(Ability.CON)},
            Ability.INT : {"Value" : 10, "Proficient" : self._get_class_proficiency(Ability.INT)},
            Ability.WIS : {"Value" : 10, "Proficient" : self._get_class_proficiency(Ability.WIS)},
            Ability.CHA : {"Value" : 10, "Proficient" : self._get_class_proficiency(Ability.CHA)}
        }
        self.skills = {
            Skill.ACROBATICS        : { "Value" : 0, "Proficient" : Proficient.NOT},
            Skill.ANIMAL_HANDLING   : { "Value" : 0, "Proficient" : Proficient.NOT},
            Skill.ARCANA            : { "Value" : 0, "Proficient" : Proficient.NOT},
            Skill.ATHLETICS         : { "Value" : 0, "Proficient" : Proficient.NOT},
            Skill.DECEPTION         : { "Value" : 0, "Proficient" : Proficient.NOT},
            Skill.HISTORY           : { "Value" : 0, "Proficient" : Proficient.NOT},
            Skill.INSIGHT           : { "Value" : 0, "Proficient" : Proficient.NOT},
            Skill.INTIMIDATION      : { "Value" : 0, "Proficient" : Proficient.NOT},
            Skill.INVESTIGATION     : { "Value" : 0, "Proficient" : Proficient.NOT},
            Skill.MEDICINE          : { "Value" : 0, "Proficient" : Proficient.NOT},
            Skill.NATURE            : { "Value" : 0, "Proficient" : Proficient.NOT},
            Skill.PERCEPTION        : { "Value" : 0, "Proficient" : Proficient.NOT},
            Skill.PERFORMANCE       : { "Value" : 0, "Proficient" : Proficient.NOT},
            Skill.PERSUASION        : { "Value" : 0, "Proficient" : Proficient.NOT},
            Skill.RELIGION          : { "Value" : 0, "Proficient" : Proficient.NOT},
            Skill.SLEIGHT_OF_HAND   : { "Value" : 0, "Proficient" : Proficient.NOT},
            Skill.STEALTH           : { "Value" : 0, "Proficient" : Proficient.NOT},
            Skill.SURVIVAL          : { "Value" : 0, "Proficient" : Proficient.NOT},
        }

    def _get_class_proficiency(self, ability: Ability):
        for dnd_class in self.classes:
            if ability in dnd_class.saving_throws: return True
        return False

    def _get_level(self):
        level = 0
        for dnd_class in self.classes:
            level += dnd_class.level
        return level

    def _get_proficiency(self): 
        # random health code I accidentally wrote when I forgot what I was doing.
        # for dnd_class in self.classes:
        #     to_rtn += (dnd_class.hit_die * dnd_class.level)
        return math.ceil(self._get_level() / 4) + 1

    def _get_saving_throw(self, ability: Ability):
        profBonus = self._get_proficiency() if ability["Proficient"] else 0
        return self._get_mod(ability) + profBonus

    def _get_mod(self, ability: Ability):
        return math.floor(ability["Value"]/2) - 5

    def _set_ability(self, ability: Ability, score, is_proficient):
        self.ability_scores[ability]["Value"] = self.ability_scores[ability]["Value"] if score is None else score
        self.ability_scores[ability]["Proficient"] = self.ability_scores[ability]["Proficient"] if is_proficient is None else is_proficient


    def set_strength(self, score: int = None, is_proficient: bool = None):
        self._set_ability(Ability.STR, score, is_proficient)

    def get_strength(self):
        return self.ability_scores[Ability.STR]["Value"]
        
    def get_strength_modifier(self):
        return self._get_mod(self.ability_scores[Ability.STR])

    def get_strength_saving_throw(self):
        return self._get_saving_throw(self.ability_scores[Ability.STR])


    def set_dexterity(self, score: int = None, is_proficient: bool = None):
        self._set_ability(Ability.DEX, score, is_proficient)

    def get_dexterity(self):
        return self.ability_scores[Ability.DEX]["Value"]
        
    def get_dexterity_modifier(self):
        return self._get_mod(self.ability_scores[Ability.DEX])

    def get_dexterity_saving_throw(self):
        return self._get_saving_throw(self.ability_scores[Ability.DEX])


    def set_constitution(self, score: int = None, is_proficient: bool = None):
        self._set_ability(Ability.CON, score, is_proficient)

    def get_constitution(self):
        return self.ability_scores[Ability.CON]["Value"]
        
    def get_constitution_modifier(self):
        return self._get_mod(self.ability_scores[Ability.CON])


    def set_intelligence(self, score: int = None, is_proficient: bool = None):
        self._set_ability(Ability.INT, score, is_proficient)

    def get_intelligence(self):
        return self.ability_scores[Ability.INT]["Value"]
        
    def get_intelligence_modifier(self):
        return self._get_mod(self.ability_scores[Ability.INT])


    def set_wisdom(self, score: int = None, is_proficient: bool = None):
        self._set_ability(Ability.WIS, score, is_proficient)

    def get_wisdom(self):
        return self.ability_scores[Ability.WIS]["Value"]
        
    def get_wisdom_modifier(self):
        return self._get_mod(self.ability_scores[Ability.WIS])

    def set_charisma(self, score: int = None, is_proficient: bool = None):
        self._set_ability(Ability.CHA, score, is_proficient)

    def get_charisma(self):
        return self.ability_scores[Ability.CHA]["Value"]
        
    def get_charisma_modifier(self):
        return self._get_mod(self.ability_scores[Ability.CHA])






class CharacterSheet:
    def __init__(self, dnd_class: list):
        self.sheet_data = SheetData(dnd_class)



