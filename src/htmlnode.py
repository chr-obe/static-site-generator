class HTMLNode:
    def __init__(self,
        tag: str | None = None,
        value: str | None = None,
        children: list["HTMLNode"] | None = None,
        props: dict[str, str] | None = None) -> None:

        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    # gets the HTML that the HTMLNode represents
    def to_html(self) -> str:
        raise NotImplementedError

    # converts the props to formatted HTML
    def props_to_html(self) -> str:
        props_html = ""

        # return the empty string if there are no properties
        if self.props is None or len(self.props) == 0:
            return props_html

        # otherwise, add the properties
        for prop, val in self.props.items():
            props_html += f' {prop}="{val}"'

        return props_html

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
