import unittest
from generate import *

class TestGenerate(unittest.TestCase):
    def test_heading_extract(self):
        md = """
# Hello
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        title = extract_title(md)
        self.assertEqual(title, "Hello")

    def test_farther_heading_extract(self):
        md = """
## Not title
text in a p
tag here
# Hello
This is another paragraph with _italic_ text and `code` here

"""
        title = extract_title(md)
        self.assertEqual(title, "Hello")

    def test_no_heading_extract(self):
        md = """
## Hello
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        self.assertRaises(Exception, "no h1 found")