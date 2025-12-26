import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):

    def test_area_normal(self):
        self.assertEqual(area(5), 25)

    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_negative(self):
        self.assertEqual(area(-5), 25)

    def test_area_string(self):
        self.assertEqual(area("5"), 25)

    def test_area_list(self):
        self.assertEqual(area([5]), [5, 5, 5, 5, 5])

    def test_area_none(self):
        with self.assertRaises(TypeError):
            area(None)

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(5), 20)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_negative(self):
        self.assertEqual(perimeter(-3), -12)

    def test_perimeter_string(self):
        self.assertEqual(perimeter("10"), 40)

    def test_perimeter_list(self):
        self.assertEqual(perimeter([3]), [3, 3, 3, 3])

    def test_perimeter_none(self):
        with self.assertRaises(TypeError):
            perimeter(None)


if __name__ == '__main__':
    unittest.main()
