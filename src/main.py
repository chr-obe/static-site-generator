from textnode import TextNode, TextType


def main() -> None:
    # create a dummy textnode just to make sure it works
    textnode: TextNode = TextNode(
        "This is some anchor text",
        TextType.LINK,
        "https://www.boot.dev")

    print(textnode)


if __name__ == "__main__":
    main()
