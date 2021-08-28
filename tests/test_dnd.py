import unittest
from tests.controller import test_roll_handler
from tests.model import test_character_sheet

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(test_roll_handler))
suite.addTests(loader.loadTestsFromModule(test_character_sheet))

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
