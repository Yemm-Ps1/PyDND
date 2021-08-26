from enum import Enum, auto


class Ability(Enum):
    STR = auto()
    DEX = auto()
    CON = auto()
    INT = auto()
    WIS = auto()
    CHA = auto()


class Skill(Enum):
    ACROBATICS      = auto()
    ANIMAL_HANDLING = auto()
    ARCANA          = auto()
    ATHLETICS       = auto()
    DECEPTION       = auto()
    HISTORY         = auto()
    INSIGHT         = auto()
    INTIMIDATION    = auto()
    INVESTIGATION   = auto()
    MEDICINE        = auto()
    NATURE          = auto()
    PERCEPTION      = auto()
    PERFORMANCE     = auto()
    PERSUASION      = auto()
    RELIGION        = auto()
    SLEIGHT_OF_HAND = auto()
    STEALTH         = auto()
    SURVIVAL        = auto()

    def is_str(self):
        return self is Skill.ATHLETICS

    def is_dex(self):
        return self in [Skill.ACROBATICS, Skill.SLEIGHT_OF_HAND, Skill.STEALTH]


class Proficient(Enum):
    NOT = auto()
    HALF = auto()
    PROFICIENT = auto()
    EXPERT = auto()
