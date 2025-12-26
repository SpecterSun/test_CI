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
        self.assertEqual(area("5", 3), "555")

    def test_area_list(self):
        self.assertEqual(area([5], 3), [5, 5, 5])

    def test_area_none(self):
        with self.assertRaises(TypeError):
            area(None, 3)

    def test_area_boolean(self):
        self.assertEqual(area(True, 3), 3)
        self.assertEqual(area(5, False), 0)

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(5, 3), 16)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 3), 6)
        self.assertEqual(perimeter(5, 0), 10)

    def test_perimeter_negative(self):
        self.assertEqual(perimeter(-5, 3), -4)
        self.assertEqual(perimeter(5, -3), 4)

    def test_perimeter_string(self):
        with self.assertRaises(TypeError):
            perimeter("5", 3)

    def test_perimeter_list(self):
        with self.assertRaises(TypeError):
            perimeter([5], 3)

    def test_perimeter_none(self):
        with self.assertRaises(TypeError):
            perimeter(None, 3)

    def test_perimeter_boolean(self):
        self.assertEqual(perimeter(True, 3), 8)
        self.assertEqual(perimeter(5, False), 10)


if __name__ == '__main__':
    unittest.main()
