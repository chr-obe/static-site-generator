import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "a", "boot.dev", props={"href": "https://www.boot.dev", "target": "_blank"}
        )
        expected = ' href="https://www.boot.dev" target="_blank"'
        actual = node.props_to_html()
        self.assertEqual(expected, actual)

    def test_no_value(self):
        node = LeafNode(None, "hr")
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_props_to_html(self):
        node = LeafNode("boot.dev website", "a", {"href": "https://www.boot.dev/"})
        expected = ' href="https://www.boot.dev/"'
        actual = node.props_to_html()
        self.assertEqual(expected, actual)

    def test_to_html_has_value(self):
        node = LeafNode("boot.dev website", "a", {"href": "https://www.boot.dev/"})
        expected = '<a href="https://www.boot.dev/">boot.dev website</a>'
        self.assertEqual(node.to_html(), expected)

    def test_to_html_empty_value(self):
        node = LeafNode("lorem ipsum")
        expected = "lorem ipsum"
        self.assertEqual(node.to_html(), expected)


if __name__ == "__main__":
    unittest.main()
