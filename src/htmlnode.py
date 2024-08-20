class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    # Convert properties from dictionary to HTML
    # E.g. representation of properties in HTML: href="https://example.com" target="_self"
    def props_to_html(self):
        if self.props is None:
            return ""
        
        out = ""
        for prop in self.props:
            out += f' {prop}="{self.props[prop]}"'
        
        return out
    
    def __repr__(self):
        out = f"HTMLNode\nname: {self.tag}\nvalue: {self.value}\n"

        if self.children is not None and self.children:
            out += "children: [\n"
            for child in self.children:
                out += f"{child.tag}\n"
            out += "]\n"

        if self.props is not None and self.props:
            out += "properties: {\n"
            for k, v in self.props.items():
                out += k + ": " + v + "\n"
            out += '}'

        return out
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        
        if self.tag is None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=[], props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("All parent nodes must have a tag")

        if not self.children:
            raise ValueError("All parent nodes must have children")
        
        out = f"<{self.tag}{self.props_to_html()}>"
        
        for child in self.children:
            out += child.to_html()
        out += f"</{self.tag}>"

        return out
