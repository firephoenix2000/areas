# -- coding: utf-8 --
# @Time : 7/20/22 8:24 AM
# @Author : yudejun
# @Email : yudejun2000@outlook.com
# @File : test_GA.py
# @Software: PyCharm


import unittest
from ga import genetic_algorithm, generate_chromosomes, select
from shape import generate_triangle_data, Triangle, Point

class TestGA(unittest.TestCase):

    def setUp(self) -> None:
        self.default_formula = genetic_algorithm(1000)

    def tearDown(self) -> None:
        self.default_formula = None


    def test_strings(self):
        '''
        the formula must be in the gene sets.

        '''
        gene_set = {'a', 'b', 'c', 'd', 'e', 'f', '+', '-', '*'}
        for s in self.default_formula:
            # print(s)
            # self.assertEqual(True, s in gene_set)
            self.assertIn(s, gene_set)

    def test_calculate(self):
        '''
        the formula can calculate and result is a number.
        '''
        the_formula = genetic_algorithm(100)
        # result = eval(self.default_formula)
        #
        # result1 = eval(the_formula)


    def test_generate_chromosomes(self):
        '''
        the formula length is between 20 and 60, and gene is  in gene list.
        '''
        gene_list = ['a', 'b', 'c', 'd', 'e', 'f', '+', '-', '*']
        chromosomes = generate_chromosomes(10)
        for chromosome in chromosomes:
            length = len(chromosome)
            self.assertLessEqual(length, 60)
            self.assertGreaterEqual(length, 20)
            for i in chromosome:
                self.assertIn(i, gene_list)

            print(chromosome)

    def test_select(self):

        chromosomes = generate_chromosomes(100)
        selected = select(chromosomes)
        (a, b, c, d, e, f) = generate_triangle_data(10)
        triangle = Triangle(Point(a, b), Point(c, d), Point(d, f))
        s = triangle.calc_area()

        # for k in range(0,len(selected)-1, 5):
        #     print(k)

        start_formula = selected[0]
        end_formula = selected[len(selected)-1]

        s1 = 0.5 * abs(eval(start_formula))
        s2 = 0.5 * abs(eval(end_formula))

        self.assertLess(abs(s1-s),abs(s2-s))


if __name__ == '__main__':
    unittest.main()
