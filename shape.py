# -- coding: utf-8 --
# @Time : 7/8/22 11:45 PM
# @Author : yudejun
# @Email : yudejun2000@outlook.com
# @File : shape.py
# @Software: PyCharm


class Point:
    """
    A point represented by two dimensional coordinates.
    """

    def __init__(self, x_pos=0, y_pos=0):
        """
        Initialize a point with x and y coordinate, default is (0,0)
        Args:
            x_pos:  x coordinate
            y_pos: y coordinate
        """

        self.x = x_pos
        self.y = y_pos


class Triangle:
    """
    A triangle represented by three points with coordinates.
    """

    def __init__(self, point_a, point_b, point_c):
        """
        Initialize a triangle with 3 points.
        Args:
            point_a:
            point_b:
            point_c:
        """
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c


    def calc_area(self):
        """
        Calculate the triangle areas
        Returns: areas
        """
        x1 = self.point_a.x
        y1 = self.point_a.y
        x2 = self.point_b.x
        y2 = self.point_b.y
        x3 = self.point_c.x
        y3 = self.point_c.y

        # s = 0.5*(x1*y2 - x1*y3 + x2*y3 -x2*y1 +x3*y1 - x2*y2)
        s =0.5 * (x1 * y2 - x1 * y3 + x2 * y3 - x2 * y1 + x3 * y1 - x2 * y2)

        return s

