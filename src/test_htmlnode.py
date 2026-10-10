import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    # test props to html with props
    def test_props_to_html(self):
        tag = "a"
        value = "test"
        props = {
            "href": "website.com",
            "target": "_blank"
        }
        node = HTMLNode(tag, value, props=props)
        expected = ' href="website.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)


    # test props to html with no props
    def test_props_to_html_no_props(self):
        node = HTMLNode("p", "test")
        self.assertIsNone(node.props)
        self.assertEqual(node.props_to_html(), "")


    # test repr
    def test_repr(self):
        child = HTMLNode("a", "click here", props={"href": "website.com"})
        parent = HTMLNode("div", "lorem ipsum", [child])
        expected = "HTMLNode(div, lorem ipsum, [HTMLNode(a, click here, None, {'href': 'website.com'})], None)"
        self.assertEqual(repr(parent), expected)

    # test values with optional args
    def test_values_optional_args(self):
        node = HTMLNode("p", "lorem ipsum")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "lorem ipsum")
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)


class TestLeafNode(unittest.TestCase):
    # test leaf node with no props
    def test_leaf_to_html_no_props(self):
        node = LeafNode("p", "lorem ipsum")
        self.assertEqual("<p>lorem ipsum</p>", node.to_html())

    # test leaf node with props
    def test_leaf_to_html_props(self):
        node = LeafNode("a", "website", {"href": "website.com"})
        self.assertEqual('<a href="website.com">website</a>', node.to_html())

    # test leaf node with no tag
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "lorem ipsum")
        self.assertEqual("lorem ipsum", node.to_html())

    # test repr
    def test_leaf_repr(self):
        node = LeafNode("p", "lorem ipsum")
        self.assertEqual("LeafNode(p, lorem ipsum, None)", repr(node))


if __name__ == "__main__":
    unittest.main()
