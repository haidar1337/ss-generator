import unittest

from textnode import TextNode
from util import split_nodes_delimiter, split_nodes_image, split_nodes_link
from text_types import *

class TestSplitNodes(unittest.TestCase):
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

    def test_split_nodes_image(self):
        node = TextNode('This is an image of a cat ![Grey cat](https://images.rawpixel.com/image_800/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvbHIvcHUyMzMxNjM2LWltYWdlLWt3dnk3dzV3LmpwZw.jpg)', text_type_text)

        excepted = [
            TextNode("This is an image of a cat ", text_type_text),
            TextNode("Grey cat", text_type_image, "https://images.rawpixel.com/image_800/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvbHIvcHUyMzMxNjM2LWltYWdlLWt3dnk3dzV3LmpwZw.jpg")
        ]
        actual = split_nodes_image([node])

        self.assertListEqual(actual, excepted)
    
    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a link [to google](https://www.google.com)",
            text_type_text,
        )

        actual = split_nodes_link([node])
        expected = [
            TextNode("This is text with a link ", text_type_text),
            TextNode("to google", text_type_link, "https://www.google.com")
        ]

        self.assertListEqual(actual, expected)

    def test_split_nodes_images(self):
        node = TextNode('This is an image of a cat ![Grey cat](https://images.rawpixel.com/image_800/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvbHIvcHUyMzMxNjM2LWltYWdlLWt3dnk3dzV3LmpwZw.jpg) and this is an image of a dog ![Dog](https://cdn.britannica.com/79/232779-050-6B0411D7/German-Shepherd-dog-Alsatian.jpg)', text_type_text)

        actual = split_nodes_image([node])
        expected = [
            TextNode("This is an image of a cat ", text_type_text),
            TextNode("Grey cat", text_type_image, "https://images.rawpixel.com/image_800/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvbHIvcHUyMzMxNjM2LWltYWdlLWt3dnk3dzV3LmpwZw.jpg"),
            TextNode(" and this is an image of a dog ", text_type_text),
            TextNode("Dog", text_type_image, "https://cdn.britannica.com/79/232779-050-6B0411D7/German-Shepherd-dog-Alsatian.jpg")
        ]

        self.assertListEqual(actual, expected)

    def test_split_nodes_image_empty(self):
        node = TextNode("This is a node without an image or a link", text_type_text)

        expected = [node]
        actual = split_nodes_image([node])

        self.assertListEqual(actual, expected)

    def test_split_nodes_link_empty(self):
        node = TextNode("This is a node without an image or a link", text_type_text)

        expected = [node]
        actual = split_nodes_link([node])

        self.assertListEqual(actual, expected)

    def test_split_nodes_image_first(self):
        node = TextNode("![Grey cat](https://images.rawpixel.com/image_800/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvbHIvcHUyMzMxNjM2LWltYWdlLWt3dnk3dzV3LmpwZw.jpg), that is an image of a cat", text_type_text)

        expected = [
            TextNode(", that is an image of a cat", text_type_text),
            TextNode("Grey cat", text_type_image, "https://images.rawpixel.com/image_800/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvbHIvcHUyMzMxNjM2LWltYWdlLWt3dnk3dzV3LmpwZw.jpg"),
        ]
        actual = split_nodes_image([node])

        self.assertListEqual(actual, expected)

    def test_split_nodes_link_first(self):
        node = TextNode("[to google](https://www.google.com), that is a link to google", text_type_text)

        expected = [
            TextNode(", that is a link to google", text_type_text),
            TextNode("to google",  text_type_link, "https://www.google.com")
        ]
        actual = split_nodes_link([node])

        self.assertListEqual(actual, expected)