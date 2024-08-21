import unittest

from util import extract_markdown_images, extract_markdown_links

class TestMarkdown(unittest.TestCase):
    def test_markdown_image_extraction(self):
        mdtext = 'This is an image of a cat ![Grey cat](https://images.rawpixel.com/image_800/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvbHIvcHUyMzMxNjM2LWltYWdlLWt3dnk3dzV3LmpwZw.jpg)'

        expected = [("Grey cat", "https://images.rawpixel.com/image_800/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvbHIvcHUyMzMxNjM2LWltYWdlLWt3dnk3dzV3LmpwZw.jpg")]
        actual = extract_markdown_images(mdtext)

        self.assertListEqual(expected, actual)

    def test_markdown_link_extraction(self):
        mdtext = 'This is a link [to google](https://google.com)'

        expected = [("to google", "https://google.com")]
        actual = extract_markdown_links(mdtext)

        self.assertListEqual(expected, actual)

    def test_markdown_link_extraction_multiple(self):
        mdtext = 'This is a link [to youtube](https://youtube.com), and this is a link [to twitch](https://twitch.tv)'

        expected = [("to youtube", "https://youtube.com"), ("to twitch", "https://twitch.tv")]
        actual = extract_markdown_links(mdtext)

        self.assertListEqual(actual, expected)

    def test_markdown_image_extraction_multiple(self):
        mdtext = "This is an image of a cat ![Grey cat](https://images.rawpixel.com/image_800/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvbHIvcHUyMzMxNjM2LWltYWdlLWt3dnk3dzV3LmpwZw.jpg), and this is an image of a dog ![Dog](https://cdn.britannica.com/79/232779-050-6B0411D7/German-Shepherd-dog-Alsatian.jpg)"

        expected = [("Grey cat", "https://images.rawpixel.com/image_800/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvbHIvcHUyMzMxNjM2LWltYWdlLWt3dnk3dzV3LmpwZw.jpg"), ("Dog", "https://cdn.britannica.com/79/232779-050-6B0411D7/German-Shepherd-dog-Alsatian.jpg")]
        actual = extract_markdown_images(mdtext)

        self.assertListEqual(actual, expected)

    def test_markdown_image_link_extraction(self):
        mdtext = 'This is a link [to youtube](https://youtube.com), and this is an image of a cat [Grey cat](https://images.rawpixel.com/image_800/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvbHIvcHUyMzMxNjM2LWltYWdlLWt3dnk3dzV3LmpwZw.jpg)'

        expected = [("to youtube", "https://youtube.com"),("Grey cat", "https://images.rawpixel.com/image_800/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvbHIvcHUyMzMxNjM2LWltYWdlLWt3dnk3dzV3LmpwZw.jpg")]
        actual = extract_markdown_images(mdtext) + extract_markdown_links(mdtext)

        self.assertListEqual(actual, expected)

    def test_markdown_image_empty(self):
        mdtext = "This is an image of a cat"

        expected = []
        actual = extract_markdown_images(mdtext)

        self.assertListEqual(actual, expected)