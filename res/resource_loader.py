import xml.etree.ElementTree as ET
import re

from typing.io import TextIO

COLORS_PATH = "../res/colors.xml"
STYLE_SHEET_PATH = "../res/style.qss"
DIMENSIONS_PATH = "../res/dimensions.xml"
STRINGS_PATH = "../res/strings.xml"
SETTINGS_PATH = "../res/settings.xml"
R_FILE_PATH = "../res/R.py"

VALID_NAME_REGEX = "[A-Za-z_]+"
VALID_HEX_REGEX = "#([0-9A-Fa-f]{3})([0-9A-Fa-f]{3})?"
VALID_DIMENSION_REGEX = "\\d+px"


def _get_dict_from_xml_path(xml_path: str):
    """
    :param xml_path: path to xml file (must contain root with child elements with name tag)
    :return: a dictionary from name attribute to value for children of root in xml file.
    """
    to_rtn = {}
    tree = ET.parse(xml_path)
    for child in tree.getroot():
        to_rtn[child.attrib["name"]] = child.text
    return to_rtn


def _inject_in_style_sheet(style_sheet: str, sub_dict: dict):
    """
    Substitutes special capitalized keywords which are stated in the relevant xml file e.g. color, dimension
    :param style_sheet: style sheet with missing keywords
    :param sub_dict: mapping from keyword to value e.g. WHITE -> #FFF or FONT_SMALL -> 8
    :return: stylesheet with defined values substituted in
    """
    to_rtn = style_sheet
    for name, value in sub_dict.items():
        # print(name, value)
        to_rtn = to_rtn.replace(f"@{name}", value)
    return to_rtn


def _validate_resource_integrity():
    valid_name_pattern = re.compile(VALID_NAME_REGEX)

    valid_color_pattern = re.compile(VALID_HEX_REGEX)
    valid_dimen_pattern = re.compile(VALID_DIMENSION_REGEX)

    for color_name, color_val in COLOR_PALETTE.items():
        if not valid_name_pattern.fullmatch(color_name):
            raise Exception(f"Invalid color name: {color_name}. Color names in res/colors.xml must have consist of "
                            f"letters and underscores only")
        if not valid_color_pattern.fullmatch(color_val):
            raise Exception(f"Invalid color value for: {color_name} -> {color_val}. Color values in res/colors.xml "
                            f"must be hex values e.g. #FFF or #FF113E")
    for dimen_name, dimen_val in DIMENSIONS.items():
        if not valid_name_pattern.fullmatch(dimen_name):
            raise Exception(f"Invalid dimension name: {dimen_name}. Dimension names in res/dimensions.xml must have "
                            f"consist of capital letters and underscores only")
        if not valid_dimen_pattern.fullmatch(dimen_val):
            raise Exception(
                f"Invalid dimension value for: {dimen_name} -> {dimen_val}. Dimension values in res/dimensions.xml must be in pixel format e.g. 10px or 32px")


def _write_enum_to_file(file: TextIO, name: str, num: int):
    file.write(f"    {name} = {num}\n")


with open(STYLE_SHEET_PATH) as f:
    STYLE_SHEET: str = f.read()

# Loads constants from resources
COLOR_PALETTE = _get_dict_from_xml_path(COLORS_PATH)
DIMENSIONS = _get_dict_from_xml_path(DIMENSIONS_PATH)
STRINGS = _get_dict_from_xml_path(STRINGS_PATH)
SETTINGS = _get_dict_from_xml_path(SETTINGS_PATH)
_validate_resource_integrity()

# Substitutes values into stylesheet
STYLE_SHEET = _inject_in_style_sheet(STYLE_SHEET, COLOR_PALETTE)
STYLE_SHEET = _inject_in_style_sheet(STYLE_SHEET, DIMENSIONS)

# Generates R.py so that resources can be found by id
RESOURCES = dict()
enum_prefix = '''# Automatically generated file. DO NOT MODIFY\n\nfrom enum import IntEnum\n\n\nclass RegistryId(IntEnum):\n'''
r_file = open(R_FILE_PATH, "w")
r_file.write(enum_prefix)
merged = {**COLOR_PALETTE, **DIMENSIONS, **STRINGS, **SETTINGS}
for i, k_v in enumerate(merged.items()):
    _write_enum_to_file(r_file, k_v[0], i)
    RESOURCES[i] = k_v[1]
r_file.close()

from res.R import RegistryId


def get_resource(reg_id: RegistryId) -> str:
    return RESOURCES[reg_id]


def get_color_palette() -> dict:
    return COLOR_PALETTE


def get_dimensions() -> dict:
    return DIMENSIONS


def get_settings() -> dict:
    return SETTINGS


def get_strings() -> dict:
    return STRINGS


def get_style_sheet() -> str:
    return STYLE_SHEET


if __name__ == '__main__':
    # palette = get_color_palette()
    # print(palette)
    # dimens = get_dimensions()
    # print(dimens)
    # strings = get_strings()
    # print(strings)
    # style_sheet = get_style_sheet()
    # print(style_sheet)
    print(RESOURCES)
    # print(get_resource(RegistryId.C))
