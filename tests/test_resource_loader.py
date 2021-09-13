import unittest
from res.resource_loader import get_dimensions, get_color_palette, VALID_NAME_REGEX, VALID_HEX_REGEX, \
    VALID_DIMENSION_REGEX

'''
 NOTE: These resource tests requires relative paths to at depth 1 from root folder. Check integrity via test_dnd instead.
'''


class TestResourceIntegrity(unittest.TestCase):
    def test_colorPalette_fromFile_shouldBeCapitalizedNameToHexCodes(self):
        found_color_palette = get_color_palette()
        for color_name, color_value in found_color_palette.items():
            self.assertRegex(color_name, VALID_NAME_REGEX)
            self.assertRegex(color_value, VALID_HEX_REGEX)

    def test_dimensions_fromFile_shouldBeNumberPixelValue(self):
        found_color_palette = get_dimensions()
        for dimen_name, dimen_value in found_color_palette.items():
            self.assertRegex(dimen_name, VALID_NAME_REGEX)
            self.assertRegex(dimen_value, VALID_DIMENSION_REGEX)
