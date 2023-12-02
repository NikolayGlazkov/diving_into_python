import unittest
class TestCaseName(unittest.TestCase):
    def test_method(self):
        self.assertEqual(2 * 1, 5, msg='Видимо и в этой вселенной не работает :-(')

if __name__ == '__main__':
    unittest.main()