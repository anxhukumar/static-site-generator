from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
  TEXT = "text"
  BOLD = "bold"
  ITALIC = "italic"
  CODE = "code"
  LINK = "link"
  IMAGE = "image"

class TextNode():
  def __init__(self, text, text_type, url=None):
    self.text = text
    self.text_type = text_type
    self.url = url

  def __eq__(self, other_node):
    return (
            self.text == other_node.text and
            self.text_type == other_node.text_type and
            self.url == other_node.url
            )
  
  def __repr__(self):
    return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
  text_type = text_node.text_type
  match text_type:
    case TextType.TEXT:
      return LeafNode(value=text_node.text)
    case TextType.BOLD:
      return LeafNode("b", text_node.text)
    case TextType.ITALIC:
      return LeafNode("i", text_node.text)
    case TextType.CODE:
      return LeafNode("code", text_node.text)
    case TextType.LINK:
      return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    case TextType.IMAGE:
      return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
    case _:
      raise Exception("Wrong type")