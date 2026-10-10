from multiprocessing import Value
import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    # two equal text nodes
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    # two nodes equal in all but text type
    def test_almost_eq(self):
        node = TextNode("lorem ipsum", TextType.TEXT)
        node2 = TextNode("lorem ipsum", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    # ensure a node with no url has the url as None
    def test_no_url(self):
        node = TextNode("lorem ipsum", TextType.TEXT)
        self.assertIsNone(node.url)

    # the same text except for capitals
    def test_capitals(self):
        node = TextNode("Lorem Ipsum", TextType.TEXT)
        node2 = TextNode("lorem ipsum", TextType.TEXT)
        self.assertNotEqual(node, node2)

    # everything is different
    def test_not_eq(self):
        node = TextNode("lorem ipsum", TextType.TEXT)
        node2 = TextNode("website", TextType.LINK, "website.com")
        self.assertNotEqual(node, node2)

    # test the repr override
    def test_repr(self):
        node = TextNode("lorem ipsum", TextType.TEXT)
        expected = "TextNode(lorem ipsum, text, None)"
        self.assertEqual(repr(node), expected)

    # test plain text node to HTML node
    def test_text(self):
        node = TextNode("lorem ipsum", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertIsNone(html_node.tag)
        self.assertEqual(html_node.value, "lorem ipsum")

    # test bold text node to HTML node
    def test_bold(self):
        node = TextNode("lorem ipsum", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "lorem ipsum")

    # test italic text node to HTML node
    def test_italic(self):
        node = TextNode("lorem ipsum", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "lorem ipsum")

    # test code text node to HTML node
    def test_code(self):
        node = TextNode("lorem ipsum", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "lorem ipsum")

    # test link text node to HTML node
    def test_link(self):
        node = TextNode("lorem ipsum", TextType.LINK, "website.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "lorem ipsum")
        self.assertEqual(html_node.props, {"href": "website.com"})

    # test image text node to HTML node
    def test_image(self):
        node = TextNode("lorem ipsum", TextType.IMAGE, "image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "image.png", "alt": "lorem ipsum"})

    # test link text node with no url
    def test_link_no_url(self):
        node = TextNode("lorem ipsum", TextType.LINK)
        self.assertRaises(ValueError, text_node_to_html_node, node)

    # test image text node with no url
    def test_image_no_url(self):
        node = TextNode("lorem ipsum", TextType.IMAGE)
        self.assertRaises(ValueError, text_node_to_html_node, node)


if __name__ == "__main__":
    unittest.main()
