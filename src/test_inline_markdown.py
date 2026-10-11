import unittest

from inline_markdown import (
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
)
from textnode import TextNode, TextType


class TestGenerator(unittest.TestCase):
    # test with bold
    def test_split_bold(self):
        old = TextNode("foo **bar** baz", TextType.TEXT)
        expected = [
            TextNode("foo ", TextType.TEXT),
            TextNode("bar", TextType.BOLD),
            TextNode(" baz", TextType.TEXT)
        ]
        self.assertEqual(
            split_nodes_delimiter([old], "**", TextType.BOLD),
            expected
        )

    # test with italic
    def test_split_italic(self):
        old = TextNode("foo _bar_ baz", TextType.TEXT)
        expected = [
            TextNode("foo ", TextType.TEXT),
            TextNode("bar", TextType.ITALIC),
            TextNode(" baz", TextType.TEXT)
        ]
        self.assertEqual(
            split_nodes_delimiter([old], "_", TextType.ITALIC),
            expected
        )

    # test with code
    def test_split_code(self):
        old = TextNode("foo `bar` baz", TextType.TEXT)
        expected = [
            TextNode("foo ", TextType.TEXT),
            TextNode("bar", TextType.CODE),
            TextNode(" baz", TextType.TEXT)
        ]
        self.assertEqual(
            split_nodes_delimiter([old], "`", TextType.CODE),
            expected
        )

    # test with multiple bolded words
    def test_split_multiple(self):
        old = TextNode("word **bold** word **bold**", TextType.TEXT)
        expected = [
            TextNode("word ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word ", TextType.TEXT),
            TextNode("bold", TextType.BOLD)
        ]
        self.assertEqual(
            split_nodes_delimiter([old], "**", TextType.BOLD),
            expected
        )

    # test with a multi-word bold word
    def test_split_multi_word(self):
        old = TextNode("one **two three** four", TextType.TEXT)
        expected = [
            TextNode("one ", TextType.TEXT),
            TextNode("two three", TextType.BOLD),
            TextNode(" four", TextType.TEXT)
        ]
        self.assertEqual(
            split_nodes_delimiter([old], "**", TextType.BOLD),
            expected
        )

    # test with invalid markdown
    def test_raises_error(self):
        node = TextNode("word **word", TextType.TEXT)
        self.assertRaises(ValueError, split_nodes_delimiter, [node], "**", TextType.BOLD)

    # test with no delimiter
    def test_no_delimiter(self):
        node = TextNode("lorem ipsum", TextType.TEXT)
        self.assertEqual(
            split_nodes_delimiter([node], "**", TextType.BOLD),
            [node]
        )

    # test with single image
    def test_one_image(self):
        matches = extract_markdown_images(
            "This is text with an ![image](url)"
        )
        self.assertListEqual([("image", "url")], matches)

    # test with multiple images
    def test_multiple_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](url) and another ![image2](url2)"
        )
        self.assertListEqual([("image", "url"), ("image2", "url2")], matches)

    # test with single link
    def test_one_link(self):
        matches = extract_markdown_links(
            "This is text with a [link](url)"
        )
        self.assertListEqual([("link", "url")], matches)

    # test with multiple links
    def test_multiple_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](url) and another [link2](url2)"
        )
        self.assertListEqual([("link", "url"), ("link2", "url2")], matches)

    # test with image and link in the same text
    def test_with_image_and_link(self):
        text = "This is text with both an ![image](url) and a [link](url)"
        image_matches = extract_markdown_images(text)
        link_matches = extract_markdown_links(text)
        self.assertListEqual([("image", "url")], image_matches)
        self.assertListEqual([("link", "url")], link_matches)

    # test separating a single image in the middle
    def test_one_image_in_middle(self):
        node = TextNode("This is text with an ![image](url) in the middle!", TextType.TEXT)
        expected = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "url"),
            TextNode(" in the middle!", TextType.TEXT)
        ]
        self.assertListEqual(split_nodes_image([node]), expected)

    # test separating a single image at the start
    def test_one_image_at_start(self):
        node = TextNode("![This](url) is text with an image at the start!", TextType.TEXT)
        expected = [
            TextNode("This", TextType.IMAGE, "url"),
            TextNode(" is text with an image at the start!", TextType.TEXT)
        ]
        self.assertListEqual(split_nodes_image([node]), expected)

    # test two images
    def test_multiple_images_nodes(self):
        node = TextNode("This ![text](url) has multiple ![images](url2) in it!", TextType.TEXT)
        expected = [
            TextNode("This ", TextType.TEXT),
            TextNode("text", TextType.IMAGE, "url"),
            TextNode(" has multiple ", TextType.TEXT),
            TextNode("images", TextType.IMAGE, "url2"),
            TextNode(" in it!", TextType.TEXT)
        ]
        self.assertListEqual(split_nodes_image([node]), expected)

    # test separating a single link in the middle
    def test_one_link_in_middle(self):
        node = TextNode("This is text with a [link](url) in the middle!", TextType.TEXT)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "url"),
            TextNode(" in the middle!", TextType.TEXT)
        ]
        self.assertListEqual(split_nodes_link([node]), expected)

    # test separating a single link at the start
    def test_one_link_at_start(self):
        node = TextNode("[This](url) is text with a link at the start!", TextType.TEXT)
        expected = [
            TextNode("This", TextType.LINK, "url"),
            TextNode(" is text with a link at the start!", TextType.TEXT)
        ]
        self.assertListEqual(split_nodes_link([node]), expected)

    # test two links
    def test_multiple_links_nodes(self):
        node = TextNode("This [text](url) has multiple [links](url2) in it!", TextType.TEXT)
        expected = [
            TextNode("This ", TextType.TEXT),
            TextNode("text", TextType.LINK, "url"),
            TextNode(" has multiple ", TextType.TEXT),
            TextNode("links", TextType.LINK, "url2"),
            TextNode(" in it!", TextType.TEXT)
        ]
        self.assertListEqual(split_nodes_link([node]), expected)

    # test the whole generator
    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertListEqual(text_to_textnodes(text), expected)
