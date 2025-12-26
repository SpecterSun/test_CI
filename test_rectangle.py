import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):

    def test_area_normal(self):
        self.assertEqual(area(5, 3), 15)

    def test_area_zero(self):
        self.assertEqual(area(0, 3), 0)
        self.assertEqual(area(5, 0), 0)

    def test_area_negative(self):
        self.assertEqual(area(-5, 3), -15)
        self.assertEqual(area(5, -3), -15)

    def test_area_string(self):
        self.assertEqual(area("5", 3), 15)
        self.assertEqual(area(5, "3"), 15)

    def test_area_list(self):
        self.assertEqual(area([5], 3), 15)
        self.assertEqual(area(5, [3]), 15)

    def test_area_none(self):
        self.assertEqual(area(None, 3), 0)
        self.assertEqual(area(5, None), 0)

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(5, 3), 16)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 3), 6)
        self.assertEqual(perimeter(5, 0), 10)

    def test_perimeter_negative(self):
        self.assertEqual(perimeter(-5, 3), -4)
        self.assertEqual(perimeter(5, -3), 4)

    def test_perimeter_string(self):
        self.assertEqual(perimeter("5", 3), 16)
        self.assertEqual(perimeter(5, "3"), 16)

    def test_perimeter_list(self):
        self.assertEqual(perimeter([5], 3), 16)
        self.assertEqual(perimeter(5, [3]), 16)

    def test_perimeter_none(self):
        self.assertEqual(perimeter(None, 3), 6)
        self.assertEqual(perimeter(5, None), 10)


if __name__ == '__main__':
    unittest.main()
