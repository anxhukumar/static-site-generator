from htmlnode import HTMLNode

class ParentNode(HTMLNode):
  def __init__(self, tag, children, props=None):
    super().__init__(tag=tag, children=children, props=props)
  
  def to_html(self):
    if not self.tag:
      raise ValueError("Tag missing")
    
    if not self.children:
      raise ValueError("Children missing")
  
    html = f"<{self.tag}>"

    for child in self.children:
      html += child.to_html()

    html += f"</{self.tag}>"

    return html

    
