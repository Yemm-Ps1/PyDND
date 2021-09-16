from ui.abstract_ui import AbstractUI
from res.resource_loader import get_resource, get_formatted_resource
from res.R import RegistryId
from controller.roll_handler import RollHandler


def get_all_commands():
    return [RollCommand("Roll", "!r")]


class Command:
    def __init__(self, name, shorthand):
        self.name = name
        self.shorthand = shorthand
        self.params = None
        self.acceptable_type_paths = None
        self.valid_param_count = -1

    def set_params(self, params: list):
        self.params = params

    def validate_params(self, ui: AbstractUI):
        if self.params is None:
            ui.submit_main_terminal_error_message(get_formatted_resource(RegistryId.ErrorNoArgumentTypeForCommand, self.name, self.valid_param_count))
            return False
        if len(self.params) is not self.valid_param_count:
            ui.submit_main_terminal_error_message(get_formatted_resource(RegistryId.ErrorIncorrectArgumentCount, self.name, self.valid_param_count, len(self.params)))
            return False
        # has_valid_types = self._validate_param_regex(ui)
        return True

    # Should be overridden
    def _validate_param_regex(self, ui: AbstractUI):
        ui.submit_main_terminal_error_message(get_formatted_resource(RegistryId.ErrorNoArgumentTypeForCommand, self.name))
        return False

    # Should be overridden
    def execute(self, ui: AbstractUI):
        ui.submit_main_terminal_error_message(get_formatted_resource(RegistryId.ErrorExecutionNotSpecifiedForCommand, self.name))
        return False


class RollCommand(Command):
    def __init__(self, name, shorthand):
        super().__init__(name, shorthand)
        self.valid_param_count = 1
        self.roll_handler: RollHandler = None

    def _validate_param_regex(self, ui: AbstractUI):
        if not self.roll_handler:
            self.roll_handler = RollHandler(ui)
        return False

    def execute(self, ui: AbstractUI):
        if not self.roll_handler:
            self.roll_handler = RollHandler(ui)
        self.roll_handler.roll(self.params[0])

if __name__ == '__main__':
    cmd = RollCommand("Roll", "!r")
    cmd.set_params(None)