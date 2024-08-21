
from textnode import TextNode
from text_types import *
import re as re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    # Match '!', then [] with any number of characters inside, then () with any number of characters inside
    regex = r"!\[(.*?)\]\((.*?)\)"
    out = re.findall(regex, text)

    return out

def extract_markdown_links(text):
    # Negative lookbehind, match brackets with any text inside, and match parentheses with any text inside 
    regex = r"(?<!!)\[(.*?)\]\((.*?)\)"
    out  = re.findall(regex, text)

    return out

def split_nodes_image(old_nodes):
    out = []
    
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if not images:
            return old_nodes
        
        split_nodes = []
        sections = []
        stop = node.text
        
        for i in range(len(images)):
            image_alt, image_link = images[i][0], images[i][1]
            sections += stop.split(f"![{image_alt}]({image_link})", 1)
            stop = stop.replace(f"{sections[0]}![{image_alt}]({image_link})", "")

            for i in range(len(sections)):
                if "!" in sections[i]:
                    continue
                if sections[i] == "":
                    continue
                if TextNode(sections[i], text_type_text) in split_nodes:
                    continue 
                split_nodes.append(TextNode(sections[i], text_type_text))

            split_nodes.append(TextNode(image_alt, text_type_image, image_link))
        
        out.extend(split_nodes)
    return out

def split_nodes_link(old_nodes):
    out = []
    
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if not links:
            return old_nodes
        
        split_nodes = []
        sections = []
        stop = node.text
        
        for i in range(len(links)):
            text, link = links[i][0], links[i][1]
            sections += stop.split(f"[{text}]({link})", 1)
            stop = stop.replace(f"{sections[0]}[{text}]({link})", "")

            for i in range(len(sections)):
                if "[" in sections[i]:
                    continue
                if sections[i] == "":
                    continue
                if TextNode(sections[i], text_type_text) in split_nodes:
                    continue 
                split_nodes.append(TextNode(sections[i], text_type_text))

            split_nodes.append(TextNode(text, text_type_link, link))
        
        out.extend(split_nodes)
    return out