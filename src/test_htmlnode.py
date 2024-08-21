import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        htmlnode = HTMLNode("a", "This is an anchor", None, {
            "href": "https://www.google.com",
            "target": "_blank",
        })

        actual = htmlnode.props_to_html()
        expected = ' href="https://www.google.com" target="_blank"'

        self.assertEqual(actual, expected)

    def test_repr(self):
        htmlnode = HTMLNode("div", None,
        [
            HTMLNode("h1", "Heading 1"),
            HTMLNode("p", "This is a paragraph"),
        ],
        {
            "draggable": "true",
            "id": "top-div",
        })

        actual = htmlnode.__repr__()
        expected = "HTMLNode\nname: div\nvalue: None\nchildren: [\nh1\np\n]\nproperties: {\ndraggable: true\nid: top-div\n}"

        self.assertEqual(actual, expected)

    def test_no_props(self):
        htmlnode = HTMLNode("a", "This is an anchor")

        actual = htmlnode.props_to_html()
        expected = ""

        self.assertEqual(actual, expected)

    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        actual = node.to_html()
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        
        self.assertEqual(actual, expected)

    def test_to_html_nested(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text")
                    ],
                ),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                ParentNode(
                    "div",
                    [
                        ParentNode("p",
                        [
                            LeafNode("i", "italic text"),
                        ],
                        {
                            "id": "ita"
                        }),
                        LeafNode(None, "Raw text")   
                    ],
                )
            ],
        )

        actual = node.to_html()
        expected = "<div><p><b>Bold text</b></p>Normal text<i>italic text</i><div><p id=\"ita\"><i>italic text</i></p>Raw text</div></div>"

        self.assertEqual(actual, expected)

    def test_to_html_nochildren(self):
        node = ParentNode("div")

        # A ValueError should be raised when a parent node does not have children
        self.assertRaises(ValueError, lambda: node.to_html())

    def test_to_html_notag(self):
        node = ParentNode()
        
        # A ValueError should be raised when a parent node does not have a tag
        self.assertRaises(ValueError, lambda: node.to_html())

    def test_to_html_leaf(self):
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


if __name__ == "__main__":
    unittest.main()