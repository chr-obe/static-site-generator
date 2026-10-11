import re
from enum import Enum


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
