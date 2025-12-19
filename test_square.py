import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):

    def test_area_normal(self):
        self.assertEqual(area(5), 25)

    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(5), 20)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)


if __name__ == '__main__':
    unittest.main()
