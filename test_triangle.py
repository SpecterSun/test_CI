import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):

    def test_area_normal(self):
        self.assertEqual(area(10, 5), 25)

    def test_area_zero(self):
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(10, 0), 0)

    def test_area_negative(self):
        self.assertEqual(area(-10, 5), -25)
        self.assertEqual(area(10, -5), -50)

    def test_area_string(self):
        self.assertEqual(area("10", 5), 50)
        self.assertEqual(area(10, "5"), 50)

    def test_area_list(self):
        self.assertEqual(area([10], 5), 50)
        self.assertEqual(area(10, [5]), 50)

    def test_area_none(self):
        self.assertEqual(area(None, 5), 0)
        self.assertEqual(area(10, None), 0)

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_perimeter_equal_sides(self):
        self.assertEqual(perimeter(5, 5, 5), 15)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 4, 5), 9)
        self.assertEqual(perimeter(3, 0, 5), 8)
        self.assertEqual(perimeter(3, 4, 0), 7)

    def test_perimeter_negative(self):
        self.assertEqual(perimeter(-3, 4, 5), 6)
        self.assertEqual(perimeter(3, -4, 5), 4)
        self.assertEqual(perimeter(3, 4, -5), 2)

    def test_perimeter_triangle_inequality(self):
        self.assertEqual(perimeter(1, 2, 10), 13)
        self.assertEqual(perimeter(10, 2, 1), 13)
        self.assertEqual(perimeter(2, 10, 1), 13)

    def test_perimeter_string(self):
        self.assertEqual(perimeter("3", 4, 5), 12)
        self.assertEqual(perimeter(3, "4", 5), 12)
        self.assertEqual(perimeter(3, 4, "5"), 12)

    def test_perimeter_list(self):
        self.assertEqual(perimeter([3], 4, 5), 12)
        self.assertEqual(perimeter(3, [4], 5), 12)
        self.assertEqual(perimeter(3, 4, [5]), 12)

    def test_perimeter_none(self):
        self.assertEqual(perimeter(None, 4, 5), 9)
        self.assertEqual(perimeter(3, None, 5), 8)
        self.assertEqual(perimeter(3, 4, None), 7)


if __name__ == '__main__':
    unittest.main()
