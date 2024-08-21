from htmlnode import LeafNode
from textnode import TextNode
from util import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, text_to_textnodes
from text_types import *

def main():
    text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

    print(text_to_textnodes(text))

main()