import unittest
from extract_markdown_img_link import extract_markdown_images, extract_markdown_links

class TestExtractMarkdownImgLink(unittest.TestCase):
  def test_extract_markdown_images(self):
      matches = extract_markdown_images(
          "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
      )
      self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

  def test_extract_markdown_links(self):
      matches = extract_markdown_links(
          "This is text with an [to boot dev](https://www.boot.dev)"
      )
      self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)

  def test_extract_markdown_images_in_text_containing_links(self):
      matches = extract_markdown_images(
          """
          Check out this cool ![cat](https://i.imgur.com/cat.png) and visit [Boot.dev](https://www.boot.dev).
          Also look at ![dog](https://i.imgur.com/dog.jpg) or read more on [Docs](https://docs.example.com).
          """
      )
      self.assertListEqual([("cat", "https://i.imgur.com/cat.png"), ("dog", "https://i.imgur.com/dog.jpg")], matches)

  def test_extract_markdown_links_in_text_containing_images(self):
      matches = extract_markdown_links(
          """
          Check out this cool ![cat](https://i.imgur.com/cat.png) and visit [Boot.dev](https://www.boot.dev).
          Also look at ![dog](https://i.imgur.com/dog.jpg) or read more on [Docs](https://docs.example.com).
          """
      )
      self.assertListEqual([("Boot.dev", "https://www.boot.dev"), ("Docs", "https://docs.example.com")], matches)

if __name__ == "__main__":
    unittest.main()