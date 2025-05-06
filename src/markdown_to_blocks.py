def markdown_to_blocks(markdown):
  markdown_list= map(lambda block: block.strip(), markdown.split("\n\n"))
  clean_markdown_list = filter(lambda block: len(block)>0, markdown_list)
  return list(clean_markdown_list)