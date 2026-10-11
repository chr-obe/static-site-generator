import re
from enum import Enum

from htmlnode import HTMLNode, ParentNode
from inline_markdown import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown: str) -> list[str]:
    raw_blocks = markdown.split("\n\n")
    blocks = []
    for block in raw_blocks:
        stripped = block.strip()
        if len(stripped) != 0:
            blocks.append(stripped)
    return blocks

def block_to_block_type(block: str) -> BlockType:
    # simple patterns at beginning and end
    if re.match(r"^#{1,6}", block) is not None:
        return BlockType.HEADING
    if re.match(r"^`{3}\n[\s\S]*`{3}$", block) is not None:
        return BlockType.CODE

    # otherwise, check for quote, list
    lines = block.split("\n")

    if all(line.startswith((">", "> ")) for line in lines):
        return BlockType.QUOTE

    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    ordered_list = True
    for i in range(len(lines)):
        if not lines[i].startswith(f"{i + 1}. "):
            ordered_list = False

    return BlockType.ORDERED_LIST if ordered_list else BlockType.PARAGRAPH


def markdown_to_html_node(markdown: str) -> ParentNode:
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children)


def block_to_html_node(block: str) -> ParentNode:
    block_type = block_to_block_type(block)
    match block_type:
        case BlockType.PARAGRAPH:
            return paragraph_to_html_node(block)
        case BlockType.HEADING:
            return heading_to_html_node(block)
        case BlockType.CODE:
            return code_to_html_node(block)
        case BlockType.UNORDERED_LIST:
            return unordered_list_to_html_node(block)
        case BlockType.ORDERED_LIST:
            return ordered_list_to_html_node(block)
        case BlockType.QUOTE:
            return quote_to_html_node(block)
    raise ValueError("invalid block type")

def text_to_children(text: str) -> list[HTMLNode]:
    text_nodes = text_to_textnodes(text)
    children = []
    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        children.append(html_node)
    return children

def paragraph_to_html_node(block: str) -> ParentNode:
    text = block.replace("\n", " ")
    return ParentNode("p", text_to_children(text))

def heading_to_html_node(block: str) -> ParentNode:
    number = block.split()[0].count("#")
    if number > 6:
       raise ValueError("invalid heading level")
    stripped = block.lstrip("# ")
    return ParentNode(f"h{number}", text_to_children(stripped))

def code_to_html_node(block: str) -> ParentNode:
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    text = block[4:-3]
    text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])

def ordered_list_to_html_node(block: str) -> ParentNode:
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item.split(". ", 1)[1]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def unordered_list_to_html_node(block: str) -> ParentNode:
    items = block.split("\n")
    html_items = []
    for item in items:
        children = text_to_children(item[2:])
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def quote_to_html_node(block: str) -> ParentNode:
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line.lstrip(">").strip())
    children = text_to_children(" ".join(new_lines))
    return ParentNode("blockquote", children)
