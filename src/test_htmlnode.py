import unittest

from htmlnode import HTMLNode


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
