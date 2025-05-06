from enum import Enum

class BlockType(Enum):
  PARAGRAPH = "paragraph"
  HEADING = "heading"
  CODE = "code"
  QUOTE = "quote"
  UNORDERED_LIST = "unordered_list"
  ORDERED_LIST = "ordered_list"

def block_to_block_type(markdown_block):
  #checks for heading(#)
  if markdown_block.startswith('#'):
      first_part = markdown_block.split()[0]
      if markdown_block.count('#') == len(first_part) and 1<= markdown_block.count('#') <= 6:
         return BlockType.HEADING
  
  #checks for code(```)
  if markdown_block.startswith('```') and markdown_block.endswith('```'):
     return BlockType.CODE
  
  #checks for quote(>)
  if markdown_block.startswith('>'):
    is_quote = True
    for line in markdown_block.split('\n'):
      if not line.startswith('>'):
          is_quote = False
          break
    
    if is_quote:
      return BlockType.QUOTE
  
  #checks for unordered list(-)
  if markdown_block.startswith('- '):
    is_ul = True
    for line in markdown_block.split('\n'):
      if not line.startswith('- '):
          is_ul = False
          break
    
    if is_ul:
      return BlockType.UNORDERED_LIST
  
  #checks for ordered list(1.)
  if markdown_block.startswith('1. '):
    count = 0
    is_ol = True
    for line in markdown_block.split('\n'):
       count += 1
       if not line.startswith(f"{count}. "):
          is_ol = False
          break
    
    if is_ol:
       return BlockType.ORDERED_LIST
    
  #returns normal paragraph
  return BlockType.PARAGRAPH