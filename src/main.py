from htmlnode import LeafNode
from textnode import TextNode
from util import split_nodes_delimiter
from text_types import *

def main():
     nodes = [TextNode("This is some *italic* text. **bold** is nice. Here is some python code to print: `print(\"Hello\")`", text_type_text)]
     split_nodes = split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter(nodes, "*", text_type_italic), "**", text_type_bold), "`", text_type_code) 

     print(split_nodes)



def text_node_to_html_node(text_node):
    text_node_type = text_node.text_type
    text_node_text = text_node.text
    text_node_url = text_node.url

    if text_node_type == text_type_text:
        return LeafNode(None, text_node_text)
    elif text_node_type == text_type_bold:
        return LeafNode("b", text_node_text)
    elif text_node_type == text_type_italic:
        return LeafNode("i", text_node_text)
    elif text_node_type == text_type_code:
        return LeafNode("code", text_node_text)
    elif text_node_type == text_type_link:
        return LeafNode("a", text_node_type, {
            "href": text_node_url
        })
    elif text_node_type == text_type_image:
        return LeafNode("img", "", {
            "alt": text_node_text,
            "src": text_node_url
        })
    raise Exception("Invalid type")

main()