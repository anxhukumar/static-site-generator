import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
  def test_to_html_with_children(self):
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

  def test_to_html_with_grandchildren(self):
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
    )

  def test_to_html_with_nested_children(self):
    grandchild_node_2 = LeafNode("a", "https://github.com")
    granchild_node_1 = LeafNode("p", "grandchild1")
    child_node_2 = ParentNode("div", [granchild_node_1, grandchild_node_2])
    child_node_1 = ParentNode("span", [child_node_2])
    parent_node = ParentNode("div", [child_node_1])
    self.assertEqual(
        parent_node.to_html(),
        "<div><span><div><p>grandchild1</p><a>https://github.com</a></div></span></div>"
    )

  def test_to_html_raise_value_error_1(self):
    child_node = LeafNode("h1")
    parent_node = ParentNode(None, [child_node])
    with self.assertRaises(ValueError):
        parent_node.to_html()

  def test_to_html_raise_value_error_2(self):
    parent_node = ParentNode("div", None)
    with self.assertRaises(ValueError):
        parent_node.to_html()

if __name__ == "__main__":
  unittest.main()