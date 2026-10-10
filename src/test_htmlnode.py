import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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


class TestParentNode(unittest.TestCase):
    # test with no nested ParentNodes
    def test_parent_node_with_children_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
                LeafNode(None, "Normal text")
            ],
        )

        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>")

    # test nested parents
    def test_parent_node_with_grandchildren_to_html(self):
        great_grandchild = LeafNode("b", "great-grandchild")
        grandchild = ParentNode("p", [great_grandchild])
        child = ParentNode("span", [grandchild])
        parent = ParentNode("div", [child])

        self.assertEqual(
            parent.to_html(),
            "<div><span><p><b>great-grandchild</b></p></span></div>"
        )

    # test no children
    def test_parent_node_with_no_children(self):
        node = ParentNode("b", [])
        self.assertRaises(ValueError, node.to_html)


    # test nested parents, with props
    def test_parent_with_nested_and_props(self):
        grandchild = LeafNode("b", "text", {"test": "test"})
        child = ParentNode("p", [grandchild], {"test2": "test2"})
        node = ParentNode("div", [child], {"test3": "test3"})
        self.assertEqual(
            node.to_html(),
            '<div test3="test3"><p test2="test2"><b test="test">text</b></p></div>'
        )

if __name__ == "__main__":
    unittest.main()
