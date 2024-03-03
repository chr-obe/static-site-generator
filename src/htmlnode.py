class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> None:
        raise NotImplementedError

    def props_to_html(self) -> str:
        html = ""
        for prop, val in self.props:
            html += f' {prop}="{val}"'
        return html

    def __repr__(self) -> str:
        pass
