import unittest

from task5 import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self) -> None:
        self.rectangle1 = Rectangle(5, 4)
        self.rectangle2 = Rectangle(2, 7)

    def test_perimeter(self):
        self.assertEqual(self.rectangle1.perimeter(), 18)

    def test_square(self):
        self.assertEqual(self.rectangle1.square(), 20)

    def test_create(self):
        self.assertEqual(self.rectangle2.width, Rectangle(2, 7).width)

    def test_equal(self):
        self.assertFalse(self.rectangle1 == self.rectangle2)


if __name__ == "__main__":
    unittest.main(verbosity=2)