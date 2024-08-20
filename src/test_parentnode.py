import unittest

from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main(exit=False)