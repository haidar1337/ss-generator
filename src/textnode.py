from htmlnode import LeafNode


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node):
    text_node_type = text_node.text_type
    text_node_text = text_node.text
    text_node_url = text_node.url

    if text_node_type == "text":
        return LeafNode(None, text_node_text)
    elif text_node_type == "bold":
        return LeafNode("b", text_node_text)
    elif text_node_type == "italic":
        return LeafNode("i", text_node_text)
    elif text_node_type == "code":
        return LeafNode("code", text_node_text)
    elif text_node_type == "link":
        return LeafNode("a", text_node_text, {
            "href": text_node_url
        })
    elif text_node_type == "image":
        return LeafNode("img", "", {
            "alt": text_node_text,
            "src": text_node_url
        })
    raise Exception("Invalid type")

