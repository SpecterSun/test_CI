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
        self.assertEqual(area(10, -5), -25)

    def test_area_string(self):
        with self.assertRaises(TypeError):
            area("10", 5)

    def test_area_list(self):
        with self.assertRaises(TypeError):
            area([10], 5)

    def test_area_none(self):
        with self.assertRaises(TypeError):
            area(None, 5)

    def test_area_boolean(self):
        self.assertEqual(area(True, 5), 2.5)
        self.assertEqual(area(10, False), 0)

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

    def test_perimeter_string(self):
        with self.assertRaises(TypeError):
            perimeter("3", 4, 5)

    def test_perimeter_list(self):
        with self.assertRaises(TypeError):
            perimeter([3], 4, 5)

    def test_perimeter_none(self):
        with self.assertRaises(TypeError):
            perimeter(None, 4, 5)

    def test_perimeter_boolean(self):
        self.assertEqual(perimeter(True, 4, 5), 10)
        self.assertEqual(perimeter(3, False, 5), 8)
        self.assertEqual(perimeter(3, 4, True), 8)


if __name__ == '__main__':
    unittest.main()
