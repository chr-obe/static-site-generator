import unittest

from textnode import TextNode, TextType


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
