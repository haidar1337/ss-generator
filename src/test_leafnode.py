import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        leafnode = LeafNode("p", "Keep calm and keep going")

        actual = leafnode.to_html()
        expected = "<p>Keep calm and keep going</p>"

        self.assertEqual(actual, expected)

    def test_to_html_props(self):
        leafnode = LeafNode("a", "This is an anchor", {
            "href": "https://www.google.com"
        })

        actual = leafnode.to_html()
        expected = "<a href=\"https://www.google.com\">This is an anchor</a>"

        self.assertEqual(actual, expected)

    def test_to_html_tag(self):
        leafnode = LeafNode(None, "This is raw text")

        actual = leafnode.to_html()
        excepted = "This is raw text"

        self.assertEqual(actual, excepted)