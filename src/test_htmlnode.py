import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "a", "boot.dev", props={"href": "https://www.boot.dev", "target": "_blank"}
        )
        expected = ' href="https://www.boot.dev" target="_blank"'
        actual = node.props_to_html()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
