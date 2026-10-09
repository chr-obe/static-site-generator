import unittest

from leafnode import LeafNode


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
