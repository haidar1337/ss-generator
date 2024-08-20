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
        if self.props ==  None:
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
    