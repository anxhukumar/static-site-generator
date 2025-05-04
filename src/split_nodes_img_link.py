from textnode import TextNode, TextType
from extract_markdown_img_link import extract_markdown_links, extract_markdown_images

def split_nodes_image(old_nodes):
  new_node_list = []
  for node in old_nodes:
    if node.text_type != TextType.TEXT:
            new_node_list.append(node)
            continue
    split_node = split_node_text_img(node.text)
    for text in split_node:
      image_tuple = extract_markdown_images(text)
      if image_tuple:
        new_node_list.append(TextNode(image_tuple[0][0], TextType.IMAGE, image_tuple[0][1]))
      else:
        new_node_list.append(TextNode(text, node.text_type))
  return new_node_list

def split_node_text_img(text):
  
  if len(text)<1:
    return []

  split_node = []
  index1 = text.find("![")

  if index1==-1:
    return [text]

  split_node.append(text[:index1])
  index2 = text.find(")", index1) + 1

  if index2==0:
    return [text]

  split_node.append(text[index1:index2])
  
  split_node.extend(split_node_text_img(text[index2:]))
  
  return split_node
      

def split_nodes_link(old_nodes):
  new_node_list = []
  for node in old_nodes:
    if node.text_type != TextType.TEXT:
            new_node_list.append(node)
            continue
    split_node = split_node_text_link(node.text)
    for text in split_node:
      link_tuple = extract_markdown_links(text)
      if link_tuple:
        new_node_list.append(TextNode(link_tuple[0][0], TextType.LINK, link_tuple[0][1]))
      else:
        new_node_list.append(TextNode(text, node.text_type))
  return new_node_list

def split_node_text_link(text):
  
  if len(text)<1:
    return []

  split_node = []
  index1 = text.find("[")

  if index1==-1:
    return [text]

  split_node.append(text[:index1])
  index2 = text.find(")", index1) + 1

  if index2==0:
    return [text]

  split_node.append(text[index1:index2])
  
  split_node.extend(split_node_text_link(text[index2:]))
  
  return split_node