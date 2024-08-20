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

        node_actual = node.__repr__()
        node2_actual = node2.__repr__()
        node_expected = "TextNode(This is an example of a text node, italic, None)"
        node2_expected = "TextNode(This is another example of a text node, bold, None)"

        self.assertEqual(node_actual, node_expected)
        self.assertEqual(node2_actual, node2_expected)

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