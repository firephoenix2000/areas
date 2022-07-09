import unittest

from shape import Triangle, Point


class MyTestCase(unittest.TestCase):


    def test_calc1(self):
        triangle1 = Triangle(Point(0,0), Point(3,0), Point(0,4))
        area = triangle1.calc_area()

        self.assertEqual(6, area)

    def test_calc2(self):
        triangle2 = Triangle(Point(0, 0), Point(3, 0), Point(0, 3))
        area = triangle2.calc_area()

        self.assertEqual(4.5, area)

    def test_calc3(self):
        triangle3 = Triangle(Point(0,0), Point(6,0), Point(4,3))
        area = triangle3.calc_area()

        self.assertEqual(9, area)


    def test_calc4(self):
        triangle4 = Triangle(Point(2,0), Point(5,0), Point(2,4))
        area = triangle4.calc_area()

        self.assertEqual(6, area)

    def test_calc5(self):
        triangle5 = Triangle(Point(2,3), Point(5,3), Point(2,7))
        area = triangle5.calc_area()

        self.assertEqual(6, area)


if __name__ == '__main__':
    unittest.main()
