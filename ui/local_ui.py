from ui.abstract_ui import AbstractUI

'''
UI which can be used locally.
'''
class LocalUI(AbstractUI):
    def __init__(self):
        pass

    def submit_main_terminal_message(self, message):
        pass

    def submit_main_terminal_error_message(self, message):
        pass

    def invalidate_health_display(self):
        pass

if __name__ == '__main__':
    ui = LocalUI()