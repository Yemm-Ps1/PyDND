import abc

'''
Defines the interface for concrete UIs
'''


class AbstractUI(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def submit_main_terminal_message(self, message):
        """ Submits a message to the main terminal where user inputs commands. """
        pass

    @abc.abstractmethod
    def submit_main_terminal_error_message(self, message):
        """ Submits an error message to the main terminal where user inputs commands likely due to invalid user-input. """
        pass

    @abc.abstractmethod
    def invalidate_health_display(self):
        """ Invalidates the console which shows character health so that the new healths can be displayed. """
        pass


if __name__ == '__main__':
    AbstractUI.s
