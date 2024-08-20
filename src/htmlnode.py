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
        out = ""
        if self.props == None:
            return out

        for k, v in self.props.items():
            out += f' {k}="{v}"'
        
        return out
    
    def __repr__(self):
        out = f"HTMLNode\nname: {self.tag}\nvalue: {self.value}\n"

        if self.children != None:
            out += "children: [\n"
            for child in self.children:
                out += f"{child.tag}\n"
            out += "]\n"

        if self.props != None:
            out += "properties: {\n"
            for k, v in self.props.items():
                out += k + ": " + v + "\n"
            out += '}'

        return out
    

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None or self.value == "":
            raise ValueError("All leaf nodes must have a value")
        
        if self.tag == None:
            return self.value
        
        if self.props != None:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
        return f"<{self.tag}>{self.value}</{self.tag}>"
    