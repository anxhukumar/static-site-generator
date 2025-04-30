
class HTMLNode():
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def to_html(self):
    raise NotImplementedError
  
  def props_to_html(self):
    final_str = ""
    for key in self.props:
      if final_str:
        final_str += " "
      final_str += f'{key}="{self.props[key]}"'
    return final_str
  
  def __eq__(self, other_node):
    return (
            self.tag == other_node.tag and
            self.value == other_node.value and
            self.children == other_node.children and
            self.props == other_node.props
           )

  def __repr__(self):
    return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"