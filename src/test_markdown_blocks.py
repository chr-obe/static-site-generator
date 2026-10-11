import unittest

from markdown_blocks import (
    BlockType,
    block_to_block_type,
    markdown_to_blocks,
    markdown_to_html_node,
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

def test_paragraphs(self):
    md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )


def test_codeblock(self):
    md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )

def test_lists(self):
        md = """
- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

def test_headings(self):
    md = """
# this is an h1

this is paragraph text

## this is an h2
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
    )

def test_blockquote(self):
    md = """
> This is a
> blockquote block

this is paragraph text

"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
    )

def test_code(self):
    md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )
