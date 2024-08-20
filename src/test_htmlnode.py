import unittest

from htmlnode import HTMLNode

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


if __name__ == "__main__":
    unittest.main()