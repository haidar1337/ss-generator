import unittest

from textnode import TextNode
from text_types import *
from util import text_to_textnodes

class TestText(unittest.TestCase):
    def test_text_to_textnode(self):
        text = "This is raw text"

        self.assertListEqual([TextNode(text, text_type_text)], text_to_textnodes(text))

    def test_text_to_textnode_bold(self):
        text = "This is **bolded** text"

        expected = [
            TextNode("This is ", text_type_text),
            TextNode("bolded", text_type_bold),
            TextNode(" text", text_type_text)
        ]

        self.assertListEqual(expected, text_to_textnodes(text))

    def test_text_to_textnode_combination(self):
        text = "This is *italic*, this is **bolded** and here is some python code: `print('Hello')`"

        expected = [
            TextNode("This is ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(", this is ", text_type_text),
            TextNode("bolded", text_type_bold),
            TextNode(" and here is some python code: ", text_type_text),
            TextNode("print('Hello')", text_type_code)
        ]

        self.assertListEqual(expected, text_to_textnodes(text))

    def test_text_to_textnode_all(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![cat image](https://images.rawpixel.com/image_800/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvbHIvcHUyMzMxNjM2LWltYWdlLWt3dnk3dzV3LmpwZw.jpg) and a link [to google](https://google.com)"

        expected = [
            TextNode("This is ", text_type_text),
            TextNode("text", text_type_bold),
            TextNode(" with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word and a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" and an ", text_type_text),
            TextNode("cat image", text_type_image, "https://images.rawpixel.com/image_800/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvbHIvcHUyMzMxNjM2LWltYWdlLWt3dnk3dzV3LmpwZw.jpg"),
            TextNode(" and a link ", text_type_text),
            TextNode("to google", text_type_link, "https://google.com"),
        ]

        self.assertListEqual(expected, text_to_textnodes(text))


if __name__ == "__main__":
    unittest.main()