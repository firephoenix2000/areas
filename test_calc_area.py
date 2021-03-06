# -- coding: utf-8 --
# @Time : 7/8/22 11:50 PM
# @Author : yudejun
# @Email : yudejun2000@outlook.com
# @File : test_calc_area.py
# @Software: PyCharm



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
        triangle5 = Triangle(Point(2,2), Point(5,2), Point(2,6))
        area = triangle5.calc_area()

        self.assertEqual(6, area)


    def test_calc6(self):
        triangle6 = Triangle(Point(-1,-1), Point(2,-1), Point(-1,3))
        area = triangle6.calc_area()

        self.assertEqual(6, area)


    def test_calc7(self):
        triangle7 = Triangle(Point(3.872345,2.5), Point(2,1), Point(4.5,1))
        area = triangle7.calc_area()

        self.assertEqual(1.875, area)


    def test_calc8(self):
        triangle8 = Triangle(Point(2.872345,2.5), Point(2,1), Point(4.5,1))
        area = triangle8.calc_area()

        self.assertEqual(1.875, area)


if __name__ == '__main__':
    unittest.main()
