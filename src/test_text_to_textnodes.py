import unittest
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
  def test_text_to_node(self):
    text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    output = text_to_textnodes(text)
    self.assertListEqual(output, 
                         [
                          TextNode("This is ", TextType.TEXT),
                          TextNode("text", TextType.BOLD),
                          TextNode(" with an ", TextType.TEXT),
                          TextNode("italic", TextType.ITALIC),
                          TextNode(" word and a ", TextType.TEXT),
                          TextNode("code block", TextType.CODE),
                          TextNode(" and an ", TextType.TEXT),
                          TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                          TextNode(" and a ", TextType.TEXT),
                          TextNode("link", TextType.LINK, "https://boot.dev")
                          ]
                          )
  
  def test_text_to_node_only_bold(self):
    text = "This is **text** and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    output = text_to_textnodes(text)
    self.assertListEqual(output, 
                         [
                          TextNode("This is ", TextType.TEXT),
                          TextNode("text", TextType.BOLD),
                          TextNode(" and an ", TextType.TEXT),
                          TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                          TextNode(" and a ", TextType.TEXT),
                          TextNode("link", TextType.LINK, "https://boot.dev")
                          ]
                          )
  
  def test_text_to_node_only_italic(self):
    text = "This is _italic_ and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    output = text_to_textnodes(text)
    self.assertListEqual(output, 
                         [
                          TextNode("This is ", TextType.TEXT),
                          TextNode("italic", TextType.ITALIC),
                          TextNode(" and an ", TextType.TEXT),
                          TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                          TextNode(" and a ", TextType.TEXT),
                          TextNode("link", TextType.LINK, "https://boot.dev")
                          ]
                          )
  
  def test_text_to_node_only_code(self):
    text = "This is `code` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    output = text_to_textnodes(text)
    self.assertListEqual(output, 
                         [
                          TextNode("This is ", TextType.TEXT),
                          TextNode("code", TextType.CODE),
                          TextNode(" and an ", TextType.TEXT),
                          TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                          TextNode(" and a ", TextType.TEXT),
                          TextNode("link", TextType.LINK, "https://boot.dev")
                          ]
                          )
  
  def test_text_to_node_only_img(self):
    text = "![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and some text"
    output = text_to_textnodes(text)
    self.assertListEqual(output, 
                         [
                          TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                          TextNode(" and some text", TextType.TEXT)
                          ]
                          )
  
  def test_text_to_node_only_link(self):
    text = "some text [link](https://boot.dev)"
    output = text_to_textnodes(text)
    self.assertListEqual(output, 
                         [
                          TextNode("some text ", TextType.TEXT),
                          TextNode("link", TextType.LINK, "https://boot.dev")
                          ]
                          )
  
  def test_text_to_node_except_img_link(self):
    text = "This is **text** with an _italic_ word and a `code block`"
    output = text_to_textnodes(text)
    self.assertListEqual(output, 
                         [
                          TextNode("This is ", TextType.TEXT),
                          TextNode("text", TextType.BOLD),
                          TextNode(" with an ", TextType.TEXT),
                          TextNode("italic", TextType.ITALIC),
                          TextNode(" word and a ", TextType.TEXT),
                          TextNode("code block", TextType.CODE),
                          ]
                          )

if __name__ == "__main__":
  unittest.main()