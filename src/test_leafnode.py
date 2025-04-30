import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
  def test_leaf_to_html_p(self):
    node = LeafNode("p", "Hello, world!")
    self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

  def test_leaf_to_html_h1(self):
    node = LeafNode("h1", "This text is the heading")
    self.assertEqual(node.to_html(), "<h1>This text is the heading</h1>")

  def test_leaf_to_html_code(self):
    node = LeafNode("code", "print('Hello World')")
    self.assertEqual(node.to_html(), "<code>print('Hello World')</code>")
  
  def test_leaf_to_html_only_value(self):
    node = LeafNode(value="Hey its me!")
    self.assertEqual(node.to_html(), "Hey its me!")

  def test_leaf_to_html_raise_value_error(self):
    node = LeafNode("p")
    with self.assertRaises(ValueError):
      node.to_html()

if __name__ == "__main__":
  unittest.main()