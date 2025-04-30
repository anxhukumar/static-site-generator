from htmlnode import HTMLNode

class LeafNode(HTMLNode):
  def __init__(self, tag = None, value = None):
    super().__init__(tag = tag, value = value)
  
  def to_html(self):
    if self.value:
      if self.tag:
        return f"<{self.tag}>{self.value}</{self.tag}>"
      else:
        return f"{self.value}"
    raise ValueError("All leaf nodes must have a value")