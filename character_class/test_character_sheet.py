import unittest
import character_sheet as CharacterSheet
import dnd_classes as DndClass

class SheetTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_levelOneRogue(self):
        sheet = CharacterSheet.SheetData([DndClass.Rogue(1)])
        self.assertEqual(sheet.get_dexterity(), 10)
        self.assertEqual(sheet.get_dexterity_saving_throw(), 2)
        self.assertEqual(sheet.get_strength_saving_throw(), 0)
        self.assertEqual(sheet.get_max_hp(), 8)

    def test_levelOneBarbarian(self):
        sheet = CharacterSheet.SheetData([DndClass.Barbarian(1)])
        self.assertEqual(sheet.get_strength(), 10)
        self.assertEqual(sheet.get_strength_saving_throw(), 2)
        self.assertEqual(sheet.get_dexterity_saving_throw(), 0)
        self.assertEqual(sheet.get_max_hp(), 12)

    def test_levelTwoRogueBarbarian(self):
        sheet = CharacterSheet.SheetData([DndClass.Rogue(1), DndClass.Barbarian(1)])
        self.assertEqual(sheet.get_strength(), 10)
        self.assertEqual(sheet.get_strength_saving_throw(), 2)
        self.assertEqual(sheet.get_dexterity_saving_throw(), 2)
        self.assertEqual(sheet.get_max_hp(), 20)

    # def test_draw_lowerBound(self):
    #     print("\nTesting lower bound Tie.")
    #     for choices in self.choiceArray:
    #         self.assertEqual(CalculateWinner(0, 0, choices), 0)

if __name__ == '__main__':
    unittest.main()


# stats = SheetData([DndClass.Rogue(1), DndClass.Barbarian(1)])
# stats.set_strength(18)
# stats.set_dexterity(20, True)
# print("Strength %s" % stats.get_strength()["Value"])
# print("Strength Mod: %s" % stats.get_strength_modifier())
# print("Strength Saving Throw: %s" % stats.get_strength_saving_throw())
# print(stats.get_dexterity()["Value"])
# print(stats.get_dexterity_modifier())
# print(stats.get_dexterity_saving_throw())