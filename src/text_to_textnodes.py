from nodes_delimiter import split_nodes_delimiter
from split_nodes_img_link import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

def text_to_textnodes(text):
  text_node = TextNode(text, TextType.TEXT)
  img_link_nodes = split_nodes_link(split_nodes_image([text_node]))
  final_node_list = []
  for node in img_link_nodes:
    if node.text_type == TextType.TEXT:
     output = split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter([node], "**", TextType.BOLD), "_", TextType.ITALIC), "`", TextType.CODE)
     final_node_list.extend(output)
    else:
      final_node_list.extend([node])
  return final_node_list