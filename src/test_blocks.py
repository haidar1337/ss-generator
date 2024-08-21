import unittest
from util import block_to_block_type, markdown_to_blocks
from block_types import *

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""

        expected = [
            'This is **bolded** paragraph',
            'This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line',
            '* This is a list\n* with items'
        ]

        self.assertListEqual(expected, markdown_to_blocks(markdown))

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_list_first(self):
        markdown = """
1. This is list item one.
2. This is list item two.
3. This is list item three.

This is a raw paragraph."""

        expected = [ 
            "1. This is list item one.\n2. This is list item two.\n3. This is list item three.",
            "This is a raw paragraph.",
        ]

        self.assertListEqual(expected, markdown_to_blocks(markdown))


    def test_block_to_block_type_heading(self):
        block = "##### Heading 5"

        self.assertEqual(block_type_heading, block_to_block_type(block))

    def test_block_to_block_type_code(self):
        block = """```print(\"Hello, World!\")```"""

        self.assertEqual(block_type_code, block_to_block_type(block))

    def test_block_to_block_type_quote(self):
        block = """>Endure today, freedom tomorrow\n>Practice makes perfect"""

        self.assertEqual(block_type_quote, block_to_block_type(block))

    def test_block_to_block_type_ordered_list(self):
        block = """1. This is list item one.\n2. This is list item two.\n3. This is list item three."""

        self.assertEqual(block_type_ordered_list, block_to_block_type(block)) 

    def test_block_to_block_type_unordered_list(self):
        block = """* This is a list item.\n* This is another list item.\n* This is one more list item"""

        self.assertEqual(block_type_unordered_list, block_to_block_type(block))

    def test_block_to_block_type_paragraph(self):
        block = "This is a raw paragraph"

        self.assertEqual(block_type_paragraph, block_to_block_type(block))

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), block_type_ordered_list)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)



if __name__ == "__main__":
    unittest.main()