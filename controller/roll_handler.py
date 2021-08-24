from enum import Enum
import random
import re

ROLL_FULL_MATCHER = re.compile("([+-]*\d+(:?d\d+)?)+")


class RollType(Enum):
    SUPER_DISADVANTAGE = -2
    DISADVANTAGE = -1
    STANDARD = 0
    ADVANTAGE = 1
    SUPER_ADVANTAGE = 2

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


# ([+-]*\d+(:?d\d+)?)


def roll(roll_command, roll_type=RollType.STANDARD):
    pass


if __name__ == '__main__':
    print(Skills.SLEIGHT_OF_HAND.is_dex())
    for v in filter(lambda s: s.is_dex(), Skills):
        print(v)
    my_list = [0, 1, 2, 3, 4]
    for val in filter(lambda x: x % 2 == 0, my_list):
        print(val)
