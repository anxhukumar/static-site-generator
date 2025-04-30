import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
  def test_eq(self):
    node = HTMLNode("a", "This is a test", [HTMLNode, HTMLNode], {"href": "https://www.google.com"})
    node2 = HTMLNode("a", "This is a test", [HTMLNode, HTMLNode], {"href": "https://www.google.com"})
    self.assertEqual(node, node2)

  def test_none_input(self):
    node = HTMLNode()
    node2 = HTMLNode()
    self.assertEqual(node, node2)

  def test_props_to_html(self):
    node = HTMLNode("a", "This is a test", [HTMLNode, HTMLNode], {"href": "https://www.google.com"})
    props_to_html_string = node.props_to_html()
    expected_string_value = 'href="https://www.google.com"'
    self.assertEqual(props_to_html_string, expected_string_value)

  def test_diff_objects(self):
    node = HTMLNode("a", "This is a test", [HTMLNode, HTMLNode], {"href": "https://www.google.com"})
    node2 = HTMLNode(value="This is a test", children=[HTMLNode, HTMLNode], props={"href": "https://www.google.com"})
    self.assertNotEqual(node, node2)

if __name__ == "__main__":
  unittest.main()