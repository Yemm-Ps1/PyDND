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

# ([+-]*\d+(:?d\d+)?)+

def roll(roll_command, roll_type=RollType.STANDARD):
    pass