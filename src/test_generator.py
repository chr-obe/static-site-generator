import unittest

from generator import extract_title


class TestGenerator(unittest.TestCase):
    def test_extract_header(self):
        markdown = """
    # title

    ## heading 2
    words words words
    **bolded words**
    """
        title = extract_title(markdown)
        self.assertEqual("title", title)
