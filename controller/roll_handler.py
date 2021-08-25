from enum import Enum
import random
import re


ONE_DIE_ROLL_MATCHER = re.compile("((\\d*)d(\\d+))")
ONE_D_TWENTY_MATCHER = re.compile("([+-]*\\d*)*1d20([+-]*\\d+)*")


class RollType(Enum):
    SUPER_DISADVANTAGE = -2
    DISADVANTAGE = -1
    STANDARD = 0
    ADVANTAGE = 1
    SUPER_ADVANTAGE = 2

    def get_postfix(self):
        if self is RollType.SUPER_DISADVANTAGE:
            return "with super-disadvantage"
        elif self is RollType.DISADVANTAGE:
            return "with disadvantage"
        elif self is RollType.STANDARD:
            return ""
        elif self is RollType.ADVANTAGE:
            return "with advantage"
        elif self is RollType.SUPER_ADVANTAGE:
            return "with super-advantage"


class RollHandler:
    def __init__(self):
        pass

    def roll(self, expression, roll_type=RollType.STANDARD):
        expression = self._preformat_expression(expression)
        if self._is_valid_expression(expression, roll_type):
            roll_match = re.search(ONE_DIE_ROLL_MATCHER, expression)
            if roll_match:
                full_match, dice_count, face_count = roll_match.groups()
                total = 0
                adv_roll_count = abs(roll_type.value) + 1
                print(f"Rolling {full_match} {roll_type.get_postfix()}:")
                for d in range(int(dice_count)):
                    rolls = [random.randint(1, int(face_count)) for _ in range(adv_roll_count)]
                    print("\n".join([str(s) for s in rolls]))
                    total += max(rolls) if roll_type.value >= 0 else min(rolls)
                expression = expression.replace(full_match, str(total), 1)
            to_rtn = eval(expression)
            print(expression, "=", to_rtn)
            return to_rtn

    def roll_advantage(self, roll_expression):
        return self.roll(roll_expression, roll_type=RollType.ADVANTAGE)

    def roll_disadvantage(self, roll_expression):
        return self.roll(roll_expression, roll_type=RollType.DISADVANTAGE)

    def roll_super_advantage(self, roll_expression):
        return self.roll(roll_expression, roll_type=RollType.SUPER_ADVANTAGE)

    def roll_super_disadvantage(self, roll_expression):
        return self.roll(roll_expression, roll_type=RollType.SUPER_DISADVANTAGE)

    @staticmethod
    def _is_valid_expression(expression, roll_type=RollType.STANDARD):
        preformatted_expression = RollHandler._preformat_expression(expression)
        expression_without_dice = re.sub(ONE_DIE_ROLL_MATCHER, "0", preformatted_expression)
        if len(list(re.finditer(ONE_DIE_ROLL_MATCHER, preformatted_expression))) > 1:
            print("Multiple dice rolls found in expression e.g 1d20 + 1d4")
            return False
        elif not re.fullmatch(ONE_D_TWENTY_MATCHER, preformatted_expression) and roll_type is not RollType.STANDARD:
            print("Non-1d20 expression found for roll which has advantage or disadvantage")
            return False
        try:
            eval(expression_without_dice)
        except SyntaxError:
            print("Invalid math syntax in expression.")
            return False
        return True

    @staticmethod
    def _preformat_expression(roll_expression):
        if roll_expression[0] is "d":
            roll_expression = "1" + roll_expression
        return re.sub("\\s", "", roll_expression)


if __name__ == '__main__':
    in_str = "d12+5"
    handler = RollHandler()
    print("Input:", in_str)
    v = handler.roll(in_str, roll_type=RollType.DISADVANTAGE)
    # print("Result:", v)