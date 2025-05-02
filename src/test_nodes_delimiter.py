import unittest
from nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestNodesDelimiter(unittest.TestCase):
  def test_nodes_delimiter_bold(self):
    node = TextNode("This is **bold**", TextType.TEXT)
    output = split_nodes_delimiter([node], "**", TextType.BOLD)
    self.assertEqual(output, [TextNode("This is ", TextType.TEXT, None), TextNode("bold", TextType.BOLD, None)])

  def test_nodes_delimiter_italic(self):
    node = TextNode("This is _italic_", TextType.TEXT)
    output = split_nodes_delimiter([node], "_", TextType.ITALIC)
    self.assertEqual(output, [TextNode("This is ", TextType.TEXT, None), TextNode("italic", TextType.ITALIC, None)])

  def test_nodes_delimiter_code(self):
    node = TextNode("Here is `code`", TextType.TEXT)
    output = split_nodes_delimiter([node], "`", TextType.CODE)
    self.assertEqual(output, [TextNode("Here is ", TextType.TEXT, None), TextNode("code", TextType.CODE, None)])

  def test_nodes_delimiter_with_non_text_type(self):
    node = TextNode("`Bold`", TextType.BOLD)
    output = split_nodes_delimiter([node], "`", TextType.CODE)
    self.assertEqual(output, [TextNode("`Bold`", TextType.BOLD)])

  def test_nodes_delimiter_with_no_markdown_symbol(self):
    node = TextNode("This is a text", TextType.TEXT)
    output = split_nodes_delimiter([node], "**", TextType.BOLD)
    self.assertEqual(output, [TextNode("This is a text", TextType.TEXT)])

  def test_nodes_delimiter_invalid_markdown_error(self):
    node = TextNode("Here is `code`, and `print('foo')", TextType.TEXT)
    with self.assertRaises(Exception) as context:
      split_nodes_delimiter([node], "`", TextType.CODE)
    self.assertEqual(str(context.exception), "Invalid markdown syntax")

  def test_nodes_delimiter_presence_of_empty_values(self):
    node = TextNode("This is a **text**", TextType.TEXT)
    output = split_nodes_delimiter([node], "**", TextType.BOLD)
    self.assertEqual(output, [TextNode("This is a ", TextType.TEXT), TextNode("text", TextType.BOLD)])

if __name__ == "__main__":
  unittest.main()