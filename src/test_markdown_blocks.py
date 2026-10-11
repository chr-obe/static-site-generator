import unittest

from markdown_blocks import (
    BlockType,
    block_to_block_type,
    markdown_to_blocks,
)


class TestMarkdownBlocks(unittest.TestCase):
    # test markdown to blocks
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    # test block to block type: paragraph
    def test_block_to_block_type_paragraph(self):
        md = "This is a paragraph"
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)

    # test block to block type: heading (all six)
    def test_block_to_block_type_headings(self):
        md = [
            "# This is a heading",
            "## This is a heading",
            "### This is a heading",
            "#### This is a heading",
            "##### This is a heading",
            "###### This is a heading",
        ]

        block_types = []
        for block in md:
            block_types.append(block_to_block_type(block))

        self.assertListEqual(block_types, [BlockType.HEADING] * 6)

    # test block to block type: code
    def test_block_to_block_type_code(self):
        md = """```
print("This is some code")
```"""
        self.assertEqual(block_to_block_type(md), BlockType.CODE)


    # test block to block type: quote
    def test_block_to_block_type_quote(self):
        md = """>line 1
> line 2
> line 3
>line 4"""
        self.assertEqual(block_to_block_type(md), BlockType.QUOTE)

    # test block to block type: unordered list
    def test_block_to_block_type_unordered_list(self):
        md = """- item 1
- item 2
- item 3"""
        self.assertEqual(block_to_block_type(md), BlockType.UNORDERED_LIST)

    # test block to block type: ordered list
    def test_block_to_block_type_ordered_list(self):
        md = """1. item 1
2. item 2
3. item 3"""
        self.assertEqual(block_to_block_type(md), BlockType.ORDERED_LIST)
