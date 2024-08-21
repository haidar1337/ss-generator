from htmlnode import LeafNode
from textnode import TextNode
from util import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image
from text_types import *

def main():
    pass

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