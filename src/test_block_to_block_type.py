import unittest
from block_to_block_type import block_to_block_type, BlockType

class TestBlockToBlockType(unittest.TestCase):
  def test_heading(self):
    self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)
    self.assertEqual(block_to_block_type("###### Level 6 heading"), BlockType.HEADING)
    self.assertNotEqual(block_to_block_type("####### Too many hashes"), BlockType.HEADING)

  def test_code(self):
    self.assertEqual(block_to_block_type("```\ncode block\n```"), BlockType.CODE)
    self.assertNotEqual(block_to_block_type("`` code ``"), BlockType.CODE)

  def test_quote(self):
    self.assertEqual(block_to_block_type("> quote line\n> another quote"), BlockType.QUOTE)
    self.assertNotEqual(block_to_block_type("> valid\ninvalid"), BlockType.QUOTE)

  def test_unordered_list(self):
    self.assertEqual(block_to_block_type("- item 1\n- item 2"), BlockType.UNORDERED_LIST)
    self.assertNotEqual(block_to_block_type("- item 1\nnot a list"), BlockType.UNORDERED_LIST)

  def test_ordered_list(self):
    self.assertEqual(block_to_block_type("1. First\n2. Second\n3. Third"), BlockType.ORDERED_LIST)
    self.assertNotEqual(block_to_block_type("1. First\n3. Second"), BlockType.ORDERED_LIST)

  def test_paragraph(self):
    self.assertEqual(block_to_block_type("This is a paragraph.\nStill a paragraph."), BlockType.PARAGRAPH)

if __name__ == "__main__":
  unittest.main()