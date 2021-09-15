import unittest

from ui.html_builder import HTMLLineBuilder

TEST_HELLO = 'Hello'
TEST_THERE = 'There'
TEST_WORLD = 'World'

TEST_TO_ESCAPE_CHARACTERS = 'Three escape characters & < >'




class TestIsValidExpressionHandler(unittest.TestCase):
    def test_builder_normalText_shouldBeHtmlFormatted(self):
        builder = HTMLLineBuilder()
        expected = '<p>HelloThereWorld</p>'
        found = builder.write_normal(TEST_HELLO).write_normal(TEST_THERE).write_normal(TEST_WORLD).build()
        self.assertEqual(expected, found)

    def test_builder_indentedText_shouldBeHtmlFormatted(self):
        builder = HTMLLineBuilder(tab_size=1, tab_depth=30)
        expected = '<p style="margin-left:30px">HelloThereWorld</p>'
        found = builder.write_normal(TEST_HELLO).write_normal(TEST_THERE).write_normal(TEST_WORLD).build()
        self.assertEqual(expected, found)

    def test_builder_doubleIndentedText_shouldBeHtmlFormatted(self):
        builder = HTMLLineBuilder(tab_size=2, tab_depth=30)
        expected = '<p style="margin-left:60px">HelloThereWorld</p>'
        found = builder.write_normal(TEST_HELLO).write_normal(TEST_THERE).write_normal(TEST_WORLD).build()
        self.assertEqual(expected, found)

    def test_builder_redThere_shouldBeHtmlFormatted(self):
        builder = HTMLLineBuilder()
        expected = '<p>Hello<span style="color:#FF0000">There</span>World</p>'
        found = builder.write_normal(TEST_HELLO).write_color(TEST_THERE, "#FF0000").write_normal(TEST_WORLD).build()
        self.assertEqual(expected, found)

    def test_builder_redThereBlueWorld_shouldBeHtmlFormatted(self):
        builder = HTMLLineBuilder()
        expected = '<p>Hello<span style="color:#FF0000">There</span><span style="color:#0000FF">World</span></p>'
        found = builder.write_normal(TEST_HELLO).write_color(TEST_THERE, "#FF0000").write_color(TEST_WORLD, "#0000FF").build()
        self.assertEqual(expected, found)

    def test_builder_tripleIndentedRedThereBlueWorld_shouldBeHtmlFormatted(self):
        builder = HTMLLineBuilder(tab_size=3, tab_depth=30)
        expected = '<p style="margin-left:90px">Hello<span style="color:#FF0000">There</span><span style="color:#0000FF">World</span></p>'
        found = builder.write_normal(TEST_HELLO).write_color(TEST_THERE, "#FF0000").write_color(TEST_WORLD, "#0000FF").build()
        self.assertEqual(expected, found)
        
    def test_builder_charactersToEscape_shouldBeHtmlFormatted(self):
        builder = HTMLLineBuilder()
        expected = '<p>Three escape characters &amp; &lt; &gt;</p>'
        found = builder.write_normal(TEST_TO_ESCAPE_CHARACTERS).build()
        self.assertEqual(expected, found)

    def test_builder_invalidHexOne_shouldRaiseException(self):
        builder = HTMLLineBuilder()
        SHOULD_FAIL_HEX = "#44"
        self.assertRaises(Exception, builder.write_color, "", SHOULD_FAIL_HEX)

    def test_builder_invalidHexTwo_shouldRaiseException(self):
        builder = HTMLLineBuilder()
        SHOULD_FAIL_HEX = "blue"
        self.assertRaises(Exception, builder.write_color, "", SHOULD_FAIL_HEX)


if __name__ == '__main__':
    unittest.main()
