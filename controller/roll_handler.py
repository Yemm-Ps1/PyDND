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
