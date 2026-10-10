from enum import Enum

from htmlnode import LeafNode


class TextType(Enum):
    TEXT = "text"   # written as: text
    BOLD = "bold"     # written as: **text**
    ITALIC = "italic" # written as: _text_
    CODE = "code"     # written as: `text`
    LINK = "link"     # written as: [link text](url)
    IMAGE = "image"   # written as: ![alt text](url)


class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str | None = None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other) -> bool:
        if not isinstance(other, TextNode):
            return False

        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            if text_node.url:
                return LeafNode("a", text_node.text, {"href": text_node.url})
            else:
                raise ValueError("link must have a url")
        case TextType.IMAGE:
            if text_node.url:
                return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
            else:
                raise ValueError("image must have a source")
        case _:
            raise ValueError("unknown text type")
