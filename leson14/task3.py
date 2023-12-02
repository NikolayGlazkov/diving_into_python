import unittest
from task2 import clear_text
class TestStr(unittest.TestCase):
    def test_non_change(self):
        self.assertEqual("this is a sample", clear_text("this is a sample"))
    
    def test_register(self):
        self.assertEqual("this is a sample", clear_text("This is a sample"))

    def test_punctuation(self):
        self.assertEqual("this is a sample", clear_text("this is a sample,"))

    def test_another_alph(self):
        self.assertEqual("this is a sample ", clear_text("this is a sample вапвап"))

    def test_all(self):
        self.assertEqual("this is a sample  ", clear_text("This is a Sample, - вапвап"))


if __name__ ==  "__main__":
    unittest.main(verbosity=2)