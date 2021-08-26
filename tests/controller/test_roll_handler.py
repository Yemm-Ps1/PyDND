import unittest
from controller.roll_handler import RollHandler, RollType

SAMPLE_SIZE = 50


class TestRollHandler(unittest.TestCase):

    def setUp(self):
        self.handler = RollHandler()
        self.handler.ui.set_active(False)  # suppresses messages to make test terminal manageable

    def test_isValidExpress_d20_shouldReturnTrue(self):
        in_expression = "d20 "
        result = self.handler._is_valid_expression(in_expression)
        self.assertTrue(result)

    def test_isValidExpress_d12plus5_shouldReturnTrue(self):
        in_expression = "d12 + 5 "
        result = self.handler._is_valid_expression(in_expression)
        self.assertTrue(result)

    def test_isValidExpression_1d20_shouldReturnTrue(self):
        in_expression = "1d20 "
        result = self.handler._is_valid_expression(in_expression)
        self.assertTrue(result)

    def test_isValidExpression_1d20plus5_shouldReturnTrue(self):
        in_expression = " 1d20+5"
        result = self.handler._is_valid_expression(in_expression)
        self.assertTrue(result)

    def test_isValidExpression_1d20minus7_shouldReturnTrue(self):
        in_expression = "1d20 - 7"
        result = self.handler._is_valid_expression(in_expression)
        self.assertTrue(result)

    def test_isValidExpression_1d20minus3withAdvantage_shouldReturnTrue(self):
        in_expression = "1d20- 3"
        result = self.handler._is_valid_expression(in_expression, roll_type=RollType.ADVANTAGE)
        self.assertTrue(result)

    def test_isValidExpression_1d20plus1d4plus5_shouldReturnFalse(self):
        in_expression = "1d20+1d4+5"
        result = self.handler._is_valid_expression(in_expression)
        self.assertFalse(result)

    def test_isValidExpression_1d12minus7withAdvantage_shouldReturnFalse(self):
        in_expression = "1d12-7"
        result = self.handler._is_valid_expression(in_expression, roll_type=RollType.ADVANTAGE)
        self.assertFalse(result)

    def test_isValidExpression_2d20minus2withAdvantage_shouldReturnFalse(self):
        in_expression = "2d20-2"
        result = self.handler._is_valid_expression(in_expression, roll_type=RollType.ADVANTAGE)
        self.assertFalse(result)

    def test_isValidExpression_1d12minus7WithSuperDisadvantage_shouldReturnFalse(self):
        in_expression = "1d12-7"
        result = self.handler._is_valid_expression(in_expression, roll_type=RollType.SUPER_DISADVANTAGE)
        self.assertFalse(result)

    def test_isValidExpression_invalidMath_shouldReturnFalse(self):
        in_expression = "1d12-*-7"
        result = self.handler._is_valid_expression(in_expression)
        self.assertFalse(result)

    def test_roll_1d8plus3_shouldHaveSamplesInRange(self):
        in_expression = "1d8+3"
        for _ in range(SAMPLE_SIZE):
            result = self.handler.roll(in_expression)
            self.assertGreaterEqual(result, 4)
            self.assertLessEqual(result, 11)

    def test_roll_1d20_shouldHaveSamplesInRange(self):
        in_expression = "1d20"
        for _ in range(SAMPLE_SIZE):
            result = self.handler.roll(in_expression)
            self.assertGreaterEqual(result, 1)
            self.assertLessEqual(result, 20)

    def test_roll_1d20withSuperAdvantage_shouldHaveSamplesInRange(self):
        in_expression = "1d20"
        for _ in range(SAMPLE_SIZE):
            result = self.handler.roll(in_expression, RollType.SUPER_ADVANTAGE)
            self.assertGreaterEqual(result, 1)
            self.assertLessEqual(result, 20)

    def test_roll_1d20plus2_shouldHaveSamplesInRange(self):
        in_expression = "1d20+2"
        for _ in range(SAMPLE_SIZE):
            result = self.handler.roll(in_expression)
            self.assertGreaterEqual(result, 3)
            self.assertLessEqual(result, 22)

    def test_roll_1d20minus5_shouldHaveSamplesInRange(self):
        in_expression = "1d20-5"
        for _ in range(SAMPLE_SIZE):
            result = self.handler.roll(in_expression)
            self.assertGreaterEqual(result, -4)
            self.assertLessEqual(result, 15)

    def test_roll_2d12minus1_shouldHaveSamplesInRange(self):
        in_expression = "2d12-1"
        for _ in range(SAMPLE_SIZE):
            result = self.handler.roll(in_expression)
            self.assertGreaterEqual(result, 1)
            self.assertLessEqual(result, 23)

    def test_roll_10d6minus5_shouldHaveSamplesInRange(self):
        in_expression = "10d6+5"
        for _ in range(SAMPLE_SIZE):
            result = self.handler.roll(in_expression)
            self.assertGreaterEqual(result, 11)
            self.assertLessEqual(result, 65)


if __name__ == '__main__':
    unittest.main()
