import unittest

from htmlnode import LeafNode
from textnode import TextNode
from textnode import text_node_to_html_node
from text_types import *
from util import split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")

        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is an example of a text node", "italic")

        node_actual = node.__repr__()
        node_expected = "TextNode(This is an example of a text node, italic, None)"

        self.assertEqual(node_actual, node_expected)

    def test_ineq(self):
        node = TextNode("Testing textnodes...", "bold")
        node2 = TextNode("Testing textnodes...", "italic")

        self.assertNotEqual(node, node2)

    def test_nourl(self):
        node = TextNode("Testing textnode with no url", "bold")
        node2 = TextNode("Testing textnode with url", "bold", "https://google.com")

        self.assertNotEqual(node, node2)
    
    def test_text_node_to_html_node(self):
        node = TextNode("This is bold text", "bold")

        actual = text_node_to_html_node(node)
        expected = LeafNode("b", "This is bold text")

        self.assertEqual(actual.tag, expected.tag)

    def test_text_node_to_html_node_props(self):
        node = TextNode("This is an image of a cat", "image",
                        "https://images.rawpixel.com/image_800/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvbHIvcHUyMzMxNjM2LWltYWdlLWt3dnk3dzV3LmpwZw.jpg")
        
        actual = text_node_to_html_node(node)
        expected = LeafNode("img", "", {
            "src": "https://images.rawpixel.com/image_800/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvbHIvcHUyMzMxNjM2LWltYWdlLWt3dnk3dzV3LmpwZw.jpg",
            "alt": "This is an image of a cat"
        })

        self.assertEqual(actual.props, expected.props)
        self.assertEqual(actual.value, expected.value)

    def test_split_nodes_delimeter(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        split_nodes = split_nodes_delimiter([node], "`", text_type_code)

        expected = [
            TextNode("This is text with a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" word", text_type_text),
        ]

        self.assertListEqual(split_nodes, expected)       

    def test_split_nodes_delimeter_multiple(self):
        nodes = [
                TextNode("This is some *italic* text. **bold** is nice. Here is some python code to print: `print(\"Hello\")`", text_type_text),
            ]
        split_nodes = split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter(nodes, "**", text_type_bold), "*", text_type_italic), "`", text_type_code) 

        expected = [
            TextNode("This is some ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" text. ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" is nice. Here is some python code to print: ", text_type_text),
            TextNode("print(\"Hello\")", text_type_code),
        ]

        self.assertListEqual(split_nodes, expected)

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded word", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()