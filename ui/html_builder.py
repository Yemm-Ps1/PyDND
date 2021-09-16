import re

ESCAPE_CHARACTERS_MAP = {'&': '&amp;', '<': '&lt;', '>': '&gt;'}
ATTRIBUTE_ONLY_ESCAPE_CHARACTERS_MAP = {'"': '&quot;', '\'': "&#39;"}

TAG_OPEN_PARAGRAPH = '<p>'
TAG_OPEN_INDENTED_PARAGRAPH = '<p style="margin-left:{}px">'
TAG_CLOSE_PARAGRAPH = '</p>'
TAG_COLOR_TEXT_FORMAT = '<span style="color:{}">{}</span>'
TAG_OPEN_COLOR_TEXT = '<span style="color:{}">'
TAG_CLOSE_COLOR_TEXT = '</span>'
TAG_LINE_BREAK = "<br>"

VALID_HEX_REGEX = "#([0-9A-Fa-f]{3})([0-9A-Fa-f]{3})?"


class HTMLLineBuilder:
    def __init__(self, tab_depth=0, tab_size: int = None):
        if tab_depth > 0:
            self.to_build = TAG_OPEN_INDENTED_PARAGRAPH.format(tab_size * tab_depth)
        else:
            self.to_build = TAG_OPEN_PARAGRAPH

    def write_normal(self, to_write):
        self.to_build += self._sub_escape_chars(to_write)
        return self

    def write_color(self, to_write, color_hex: str):
        self._raise_exception_if_not_hex(color_hex)
        subbed = self._sub_escape_chars(to_write)
        self.to_build += TAG_COLOR_TEXT_FORMAT.format(color_hex, subbed)
        return self

    @staticmethod
    def _raise_exception_if_not_hex(should_be_hex):
        if type(should_be_hex) is not str:
            raise Exception(f'Hexes should be string-typed, type found{type(should_be_hex)}')
        if not re.fullmatch(VALID_HEX_REGEX, should_be_hex):
            raise Exception(f'String {should_be_hex} does not match expected hex format e.g. #FFF or #010AB1')

    @staticmethod
    def _sub_escape_chars(txt: str):
        to_rtn = txt
        for k, v in ESCAPE_CHARACTERS_MAP.items():
            to_rtn = to_rtn.replace(k, v)
        return to_rtn

    @staticmethod
    def _sub_attribute_escape_values(self, txt: str):
        to_rtn = self._sub_escape_chars(txt)
        for k, v in ATTRIBUTE_ONLY_ESCAPE_CHARACTERS_MAP.items():
            to_rtn = to_rtn.replace(k, v)
        return to_rtn

    def build(self):
        return self.to_build + TAG_CLOSE_PARAGRAPH

