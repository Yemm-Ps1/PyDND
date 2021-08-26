from ui.abstract_ui import AbstractUI
from colorama import Fore, Style
import re

ONE_DIE_ROLL_MATCHER = re.compile("((\\d*)d(\\d+))")

'''
UI used as a placeholder to connect to back-end and check functionality before front-end is developed.
Just prints the native python console.
'''


class BasicUI(AbstractUI):
    def __init__(self):
        pass

    def submit_main_terminal_message(self, message):
        """ Submits a message to the main terminal where user inputs commands. """
        print(message)

    def submit_main_terminal_error_message(self, message: str):
        """ Submits an error message to the main terminal and colors it red. """
        print(f"{Fore.RED}{message}{Style.RESET_ALL}")

    def invalidate_health_display(self):
        """ Indicates that health display would be invalidated if it existed. """
        print(f"{Fore.BLUE}Healths Invalidated!{Style.RESET_ALL}")

    @staticmethod
    def _preformat_colors(message: str):
        """ Inserts colors to specific character sequences such as dice rolls, numbers and character names """
        for m in re.finditer(ONE_DIE_ROLL_MATCHER, message):
            pass
        # TODO replace die rolls with color
        # TODO numbers with color
        # TODO replace character names with color


if __name__ == '__main__':
    # print(re.sub("\\d+", "->\g<0><-", "a b c 5 e f"))
    ui = BasicUI()
    ui.submit_main_terminal_message("Hello there")
    ui.submit_main_terminal_error_message("General Kenobi")
    ui.invalidate_health_display()
