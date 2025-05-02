from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
  new_node_list = []
  for node in old_nodes:

    if node.text_type == TextType.TEXT:
      if node.text.count(delimiter)%2 != 0:
        raise Exception("Invalid markdown syntax")
      split_node = node.text.split(delimiter)
      if (len(split_node)>1):
        for i in range(len(split_node)):
          if i%2==0:
            if split_node[i]:
              new_node_list.append(TextNode(split_node[i], node.text_type))
          else:
            if split_node[i]: 
              new_node_list.append(TextNode(split_node[i], text_type))
    else:
      new_node_list.append(node)
  
  return new_node_list