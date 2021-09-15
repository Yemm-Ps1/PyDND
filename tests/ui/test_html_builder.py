import unittest

from ui.html_builder import HTMLLineBuilder

TEST_HELLO = 'Hello'
TEST_THERE = 'There'
TEST_WORLD = 'World'


class TestIsValidExpressionHandler(unittest.TestCase):
    def test_justBuild_normalText_shouldWrappedInParaTags(self):
        builder = HTMLLineBuilder()
        expected = '<p>HelloThereWorld</p>'
        found = builder.write_normal(TEST_HELLO).write_normal(TEST_THERE).write_normal(TEST_WORLD).build()
        self.assertEqual(expected, found)
        # R #FF0000
        # B #0000FF

    def test_justBuild_indentedText_shouldWrappedInParaTags(self):
        builder = HTMLLineBuilder(tab_size=1, tab_depth=30)
        expected = '<p style="margin-left:30px">HelloThereWorld</p>'
        found = builder.write_normal(TEST_HELLO).write_normal(TEST_THERE).write_normal(TEST_WORLD).build()
        self.assertEqual(expected, found)

    def test_justBuild_doubleIndentedText_shouldWrappedInParaTags(self):
        builder = HTMLLineBuilder(tab_size=2, tab_depth=30)
        expected = '<p style="margin-left:60px">HelloThereWorld</p>'
        found = builder.write_normal(TEST_HELLO).write_normal(TEST_THERE).write_normal(TEST_WORLD).build()
        self.assertEqual(expected, found)

    def test_justBuild_redThere_shouldWrappedInParaTags(self):
        builder = HTMLLineBuilder()
        expected = '<p>Hello<span style="color:#FF0000">There</span>World</p>'
        found = builder.write_normal(TEST_HELLO).write_color(TEST_THERE, "#FF0000").write_normal(TEST_WORLD).build()
        self.assertEqual(expected, found)

    def test_justBuild_redThereBlueWorld_shouldWrappedInParaTags(self):
        builder = HTMLLineBuilder()
        expected = '<p>Hello<span style="color:#FF0000">There</span><span style="color:#0000FF">World</span></p>'
        found = builder.write_normal(TEST_HELLO).write_color(TEST_THERE, "#FF0000").write_color(TEST_WORLD, "#0000FF").build()
        self.assertEqual(expected, found)

    def test_justBuild_tripleIndentedRedThereBlueWorld_shouldWrappedInParaTags(self):
        # TODO
        builder = HTMLLineBuilder(tab_size=3, tab_depth=30)
        expected = '<p style="margin-left:90px">Hello<span style="color:#FF0000">There</span><span style="color:#0000FF">World</span></p>'
        found = builder.write_normal(TEST_HELLO).write_color(TEST_THERE, "#FF0000").write_color(TEST_WORLD, "#0000FF").build()
        self.assertEqual(expected, found)


if __name__ == '__main__':
    unittest.main()