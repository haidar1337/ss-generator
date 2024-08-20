import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")

        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is an example of a text node", "italic")
        node2 = TextNode("This is another example of a text node", "bold")

        self.assertEqual(node.__repr__(), f"TextNode({node.text}, {node.text_type}, {node.url})")
        self.assertEqual(node2.__repr__(), f"TextNode({node2.text}, {node2.text_type}, {node2.url})")

    def test_ineq(self):
        node = TextNode("Testing textnodes...", "bold")
        node2 = TextNode("Testing textnodes...", "italic")

        self.assertNotEqual(node, node2)

    def test_nourl(self):
        node = TextNode("Testing textnode with no url", "bold")
        node2 = TextNode("Testing textnode with url", "bold", "https://google.com")

        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()