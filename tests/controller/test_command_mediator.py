import unittest
from controller.command_mediator import CommandMediator

class TestCommandMediator(unittest.TestCase):

    def setUp(self):
        self.test_mediator = CommandMediator()

    def test_preprocessCommand_noConnectors_shouldRemainTheSame(self):
        test = '16 18 12'
        found = self.test_mediator._preprocess_input(test)
        self.assertEqual(test, found)

    def test_preprocessCommand_chainedPlus_shouldRemoveAdjacentSpace(self):
        test = '16 + 18 + 12'
        expected = "16+18+12"
        found = self.test_mediator._preprocess_input(test)
        self.assertEqual(expected, found)

    def test_preprocessCommand_chainedMinus_shouldRemoveAdjacentSpace(self):
        test = '16 - 18 - 12'
        expected = "16-18-12"
        found = self.test_mediator._preprocess_input(test)
        self.assertEqual(expected, found)

    def test_preprocessCommand_chainedDivide_shouldRemoveAdjacentSpace(self):
        test = '16 / 18 / 12'
        expected = "16/18/12"
        found = self.test_mediator._preprocess_input(test)
        self.assertEqual(expected, found)

    def test_preprocessCommand_chainedTimes_shouldRemoveAdjacentSpace(self):
        test = '16 * 18 * 12'
        expected = "16*18*12"
        found = self.test_mediator._preprocess_input(test)
        self.assertEqual(expected, found)

    def test_preprocessCommand_mixedSpaceWithPlus_shouldRemoveAdjacentSpace(self):
        test = '16+ 18 +12'
        expected = "16+18+12"
        found = self.test_mediator._preprocess_input(test)
        self.assertEqual(expected, found)

if __name__ == '__main__':
    unittest.main()