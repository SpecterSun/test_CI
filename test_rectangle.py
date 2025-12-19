import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):

    def test_area_normal(self):
        self.assertEqual(area(10, 5), 50)

    def test_area_zero(self):
        self.assertEqual(area(10, 0), 0)

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(10, 5), 30)

    def test_perimeter_square(self):
        self.assertEqual(perimeter(4, 4), 16)


if __name__ == '__main__':
    unittest.main()
