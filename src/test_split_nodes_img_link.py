import unittest
from textnode import TextNode, TextType
from split_nodes_img_link import split_nodes_image, split_nodes_link

class TestSplitNodesImgLink(unittest.TestCase):
  def test_split_images(self):
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            ),
        ],
        new_nodes,
    )

  def test_split_links(self):
    node = TextNode(
      "This is text with an [google](https://google.com) and another [x](https://x.com)",
      TextType.TEXT
    )
    new_nodes = split_nodes_link([node])
    self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("google", TextType.LINK, "https://google.com"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "x", TextType.LINK, "https://x.com"
            ),
        ],
        new_nodes,
    )

  def test_only_text_node(self):
    node = TextNode(
      "This is text without any image or link",
      TextType.TEXT
    )
    new_nodes_1 = split_nodes_image([node])
    new_nodes_1 = split_nodes_link(new_nodes_1)
    self.assertListEqual(
        [
            TextNode("This is text without any image or link", TextType.TEXT),
        ],
        new_nodes_1,
    )

  def test_blank_text_node(self):
    node = TextNode(
      "",
      TextType.TEXT
    )
    new_nodes_1 = split_nodes_image([node])
    self.assertListEqual([], new_nodes_1)

    new_nodes_2 = split_nodes_link([node])
    self.assertListEqual([], new_nodes_2)

  def test_multiple_nodes_img(self):
    node1 = TextNode(
      "This is text with an ![image1](https://google.com) and another [link](https://link.com)",
      TextType.TEXT
    )
    node2 = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT
    )
    new_nodes = split_nodes_image([node1, node2])
    self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image1", TextType.IMAGE, "https://google.com"),
            TextNode(" and another [link](https://link.com)", TextType.TEXT),
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            ),
        ],
        new_nodes,
    )
  
  def test_multiple_nodes_link(self):
    node1 = TextNode(
      "This is text with an [google](https://google.com) and another ![img][img-link]",
      TextType.TEXT
    )
    node2 = TextNode(
        "This is text with an [link1](https://i.imgur.com/zjjcJKZ.png) and another [link2](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT
    )
    new_nodes = split_nodes_link([node1, node2])
    self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("google", TextType.LINK, "https://google.com"),
            TextNode(" and another ![img][img-link]", TextType.TEXT),
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("link1", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "link2", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
            ),
        ],
        new_nodes,
    )

if __name__=="__main__":
  unittest.main()