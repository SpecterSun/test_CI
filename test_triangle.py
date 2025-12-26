import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):

    def test_area_normal(self):
        self.assertEqual(area(10, 5), 25)

    def test_area_zero(self):
        self.assertEqual(area(10, 0), 0)
        self.assertEqual(area(0, 5), 0)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(-10, 5)
        with self.assertRaises(ValueError):
            area(10, -5)
        with self.assertRaises(ValueError):
            area(-10, -5)

    def test_area_string(self):
        with self.assertRaises(TypeError):
            area("10", 5)
        with self.assertRaises(TypeError):
            area(10, "5")

    def test_area_list(self):
        with self.assertRaises(TypeError):
            area([10], 5)
        with self.assertRaises(TypeError):
            area(10, [5])

    def test_area_none(self):
        with self.assertRaises(TypeError):
            area(None, 5)
        with self.assertRaises(TypeError):
            area(10, None)

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_perimeter_equal_sides(self):
        self.assertEqual(perimeter(5, 5, 5), 15)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 4, 5), 9)
        self.assertEqual(perimeter(3, 0, 5), 8)
        self.assertEqual(perimeter(3, 4, 0), 7)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-3, 4, 5)
        with self.assertRaises(ValueError):
            perimeter(3, -4, 5)
        with self.assertRaises(ValueError):
            perimeter(3, 4, -5)

    def test_perimeter_string(self):
        with self.assertRaises(TypeError):
            perimeter("3", 4, 5)
        with self.assertRaises(TypeError):
            perimeter(3, "4", 5)
        with self.assertRaises(TypeError):
            perimeter(3, 4, "5")

    def test_perimeter_list(self):
        with self.assertRaises(TypeError):
            perimeter([3], 4, 5)
        with self.assertRaises(TypeError):
            perimeter(3, [4], 5)
        with self.assertRaises(TypeError):
            perimeter(3, 4, [5])

    def test_perimeter_none(self):
        with self.assertRaises(TypeError):
            perimeter(None, 4, 5)
        with self.assertRaises(TypeError):
            perimeter(3, None, 5)
        with self.assertRaises(TypeError):
            perimeter(3, 4, None)


if __name__ == '__main__':
    unittest.main()
