import time

from res.R import RegistryId
from res.resource_loader import get_formatted_resource
from ui.abstract_ui import AbstractUI
from controller.roll_handler import RollHandler
from model.model_facade import ModelFacade
import re
from controller.commands import Command, get_all_commands
from ui.basic_ui import BasicUI


INPUT_DELIMITER_REGEX = re.compile('\s+')
ACTUAL_DELIMITER_STR = ' '

NON_MATH_COMMAND_REGEX = re.compile('[\w\-_#]+(?:\d+)?')

CONNECTING_TOKEN_REGEX = r'[+\-*/]'




class CommandMediator:
    """
    The central controller which takes in commands from the ui and runs commands which may interleave with signals
    of messages to the UI. It also loads a Model and updates it when required. Delegation to to other controller
    sub-components occurs whenever required.
    """

    # TODO change so that ai passed through methods instead of controller having a pointer. Maybe?
    def __init__(self, ui: AbstractUI = BasicUI()):
        self.ui = ui
        self.roll_handler = RollHandler(ui)
        self.model: ModelFacade = None
        self.command_from_name = dict()
        self.command_from_shorthand = dict()
        self._load_commands_to_dicts()

    def _load_commands_to_dicts(self):
        """

        :return:
        """
        all_commands = get_all_commands()
        for command in all_commands:
            self.command_from_name[command.name] = command
            self.command_from_shorthand[command.shorthand] = command

    def load_model(self):
        return ModelFacade()  # TODO replace with model from file

    def process_command(self, input_str: str):
        # TODO check for empty commands
        time.sleep(.05)
        print("Before preprocess:", input_str)
        input_str = self._preprocess_input(input_str)
        print("After preprocess:", input_str)

        split = re.split("\s", input_str)
        cmd_str = split[0]
        params = list(filter(lambda a: a != '', split[1:]))
        # print("Command:", cmd_str, "\tParams:", params)


        cmd: Command = self._get_command_from_dicts(cmd_str)
        if not cmd:
            self.ui.submit_main_terminal_error_message(get_formatted_resource(RegistryId.ErrorUnrecognizedCommandOrShorthand, cmd_str))
            return False

        cmd.set_params(params)
        if cmd.validate_params(self.ui):
            cmd.execute(self.ui)

    @staticmethod
    def _preprocess_input(processing: str) -> str:
        processing = processing.strip()
        to_replace = r'\s*({})\s*'.format(CONNECTING_TOKEN_REGEX)
        return re.sub(to_replace, r'\1', processing)

    def _get_command_from_dicts(self, cmd_str):
        if cmd_str in self.command_from_name:
            return self.command_from_name[cmd_str]
        if cmd_str in self.command_from_shorthand:
            return self.command_from_shorthand[cmd_str]
        return None


if __name__ == '__main__':
    center = CommandMediator(BasicUI())
    in_str = '16 + 18 + 12'
    print(in_str)
    processed = center._preprocess_input(in_str)
    print(processed)