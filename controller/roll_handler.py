import random
import re
from enum import Enum

from ui.abstract_ui import AbstractUI
from ui.basic_ui import BasicUI

ONE_DIE_ROLL_MATCHER = re.compile("((\\d*)d(\\d+))")
ONE_D_TWENTY_MATCHER = re.compile("([+-]*\\d*)*1d20([+-]*\\d+)*")


class RollType(Enum):
    """
    An enumeration indicating a type of dice roll, for example "Advantage".
    """
    SUPER_DISADVANTAGE = -2
    DISADVANTAGE = -1
    STANDARD = 0
    ADVANTAGE = 1
    SUPER_ADVANTAGE = 2

    def get_postfix(self):
        """
        A gets a custom string post-fix for a dice-roll ending in a full-stop e.g. "with disadvantage.".
        :return:
        """
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
    def __init__(self, ui: AbstractUI = None):
        self.ui = ui if ui else BasicUI()

    def roll(self, roll_expression: str, roll_type: RollType = RollType.STANDARD) -> int:
        """
        Calculates the outcome of dice rolls for an inputted expression written in dice notation.

        :param roll_expression: An expression in dice notation indicating rolls to be made
        :param roll_type: An enumeration indicating whether the roll is standard or has advantage, disadvantage.
        :return: the evaluation of the mathematical expression when diced rolls have been evaluated.
        """
        roll_expression = self._preformat_expression(roll_expression)
        if self._is_valid_expression(roll_expression, roll_type):
            roll_match = re.search(ONE_DIE_ROLL_MATCHER, roll_expression)
            if roll_match:
                full_match, dice_count, face_count = roll_match.groups()
                total = 0
                adv_roll_count = abs(roll_type.value) + 1
                self.ui.submit_main_terminal_message(f"Rolling {full_match} {roll_type.get_postfix()}:")
                for d in range(int(dice_count)):
                    rolls = [random.randint(1, int(face_count)) for _ in range(adv_roll_count)]
                    self.ui.submit_main_terminal_message("\n".join([str(s) for s in rolls]))
                    total += max(rolls) if roll_type.value >= 0 else min(rolls)
                roll_expression = roll_expression.replace(full_match, str(total), 1)
            to_rtn = eval(roll_expression)
            self.ui.submit_main_terminal_message(roll_expression + " = " + str(to_rtn))
            return int(to_rtn)

    def roll_advantage(self, roll_expression) -> int:
        """
        Calculates the outcome of dice rolls for an inputted expression written in dice notation with advantage.

        :param roll_expression: An expression in dice notation indicating rolls to be made
        :return: the evaluation of the mathematical expression when diced rolls have been evaluated.
        """
        return self.roll(roll_expression, roll_type=RollType.ADVANTAGE)

    def roll_disadvantage(self, roll_expression) -> int:
        """
        Calculates the outcome of dice rolls for an inputted expression written in dice notation with disadvantage.

        :param roll_expression: An expression in dice notation indicating rolls to be made
        :return: the evaluation of the mathematical expression when diced rolls have been evaluated.
        """
        return self.roll(roll_expression, roll_type=RollType.DISADVANTAGE)

    def roll_super_advantage(self, roll_expression) -> int:
        """
        Calculates the outcome of dice rolls for an inputted expression written in dice notation with super-advantage.

        :param roll_expression: An expression in dice notation indicating rolls to be made
        :return: the evaluation of the mathematical expression when diced rolls have been evaluated.
        """
        return self.roll(roll_expression, roll_type=RollType.SUPER_ADVANTAGE)

    def roll_super_disadvantage(self, roll_expression) -> int:
        """
        Calculates the outcome of dice rolls for an inputted expression written in dice notation with super-disadvantage.

        :param roll_expression: An expression in dice notation indicating rolls to be made.
        :return: the evaluation of the mathematical expression when diced rolls have been evaluated.
        """
        return self.roll(roll_expression, roll_type=RollType.SUPER_DISADVANTAGE)

    def _is_valid_expression(self, roll_expression, roll_type=RollType.STANDARD) -> bool:
        """
        Checks the validity an inputted expression written in dice notation and submits a custom error message to the
        ui if the expression is in an unexpected form.

        :param roll_expression: An expression in dice notation indicating rolls to be made
        :param roll_type: An enumeration indicating whether the roll is standard or has advantage, disadvantage.
        :return: the evaluation of the mathematical expression when diced rolls have been evaluated.
        """
        preformatted_expression = RollHandler._preformat_expression(roll_expression)
        expression_without_dice = re.sub(ONE_DIE_ROLL_MATCHER, "0", preformatted_expression)
        if len(list(re.finditer(ONE_DIE_ROLL_MATCHER, preformatted_expression))) > 1:
            self.ui.submit_main_terminal_error_message("Multiple dice rolls found in expression e.g 1d20 + 1d4.")
            return False
        elif not re.fullmatch(ONE_D_TWENTY_MATCHER, preformatted_expression) and roll_type is not RollType.STANDARD:
            self.ui.submit_main_terminal_error_message("Non-1d20 expression not permitted with Advantage/Disadvantage")
            return False
        try:
            eval(expression_without_dice)
        except SyntaxError:
            self.ui.submit_main_terminal_error_message("Invalid math syntax in expression.")
            return False
        return True

    @staticmethod
    def _preformat_expression(roll_expression) -> str:
        """
        Prepends a 1 to the expression if it begins with d, for example d20+5 becomes 1d20+5.

        :return: the string prepended with a 1
        """
        if roll_expression[0] is "d":
            roll_expression = "1" + roll_expression
        return re.sub("\\s", "", roll_expression)


if __name__ == '__main__':
    in_str = "1d20+5"
    handler = RollHandler()
    print("Input:", in_str)
    v = handler.roll(in_str, roll_type=RollType.DISADVANTAGE)
    print("Result:", v)
