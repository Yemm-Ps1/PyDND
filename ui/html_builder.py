TAG_OPEN_PARAGRAPH = '<p>'
TAG_OPEN_INDENTED_PARAGRAPH = '<p style="margin-left:{}px">'
TAG_CLOSE_PARAGRAPH = '</p>'
TAG_COLOR_TEXT_FORMAT = '<span style="color:{}">{}</span>'
TAG_OPEN_COLOR_TEXT = '<span style="color:{}">'
TAG_CLOSE_COLOR_TEXT = '</span>'
TAG_LINE_BREAK = "<br>"


class HTMLLineBuilder:
    def __init__(self, tab_depth=0, tab_size: int = None):
        if tab_depth > 0:
            if tab_size is None:
                # avoids importing resources in unit testing
                from res.R import RegistryId
                from res.resource_loader import get_resource
                tab_size = get_resource(RegistryId.TerminalIndent)
            else:
                self.to_build = TAG_OPEN_INDENTED_PARAGRAPH.format(tab_size * tab_depth)
        else:
            self.to_build = TAG_OPEN_PARAGRAPH

    def write_normal(self, to_write):
        self.to_build += to_write
        return self

    def write_color(self, to_write, color_hex):
        self.to_build += TAG_COLOR_TEXT_FORMAT.format(color_hex, to_write)
        return self

    def build(self):
        return self.to_build + TAG_CLOSE_PARAGRAPH

