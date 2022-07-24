# -- coding: utf-8 --
# @Time : 7/20/22 8:24 AM
# @Author : yudejun
# @Email : yudejun2000@outlook.com
# @File : test_GA.py
# @Software: PyCharm


import unittest
from ga import genetic_algorithm, init_chromosomes, select, crossover, mutate, check_chromosome
from shape import generate_triangle_data, Triangle, Point

class TestGA(unittest.TestCase):

    def setUp(self) -> None:
        # self.default_formula = genetic_algorithm(1000)
        pass

    def tearDown(self) -> None:
        # self.default_formula = None
        pass



    def test_calculate(self):
        '''
        the formula can calculate and result is a number.
        '''
        the_formula = genetic_algorithm(100)
        (a, b, c, d, e, f) = generate_triangle_data(10)
        print(the_formula)
        result = 0.5*abs(eval(the_formula))
        self.assertGreater(result,0)


    def test_generate_chromosomes(self):
        '''
        the formula length is between 20 and 60, and gene is  in gene list.
        '''
        gene_list = ['a', 'b', 'c', 'd', 'e', 'f', '+', '-', '*']
        chromosomes = init_chromosomes(10)
        for chromosome in chromosomes:
            length = len(chromosome)
            self.assertLessEqual(length, 60)
            self.assertGreaterEqual(length, 20)
            for i in chromosome:
                self.assertIn(i, gene_list)

            print(chromosome)

    def test_select(self):

        chromosomes = init_chromosomes(100)
        selected = select(chromosomes)
        (a, b, c, d, e, f) = generate_triangle_data(10)
        triangle = Triangle(Point(a, b), Point(c, d), Point(d, f))
        s = triangle.calc_area()


        start_formula = selected[0]
        end_formula = selected[len(selected)-1]

        s1 = 0.5 * abs(eval(start_formula))
        s2 = 0.5 * abs(eval(end_formula))

        self.assertLess(abs(s1-s),abs(s2-s))


    def test_crossover(self):
        init_chroms = [ 'e*d*e*a*b-b*e*c+f+a+a+c', 'f*b*b-c*f+c*b+d*d+b+e+a+f+e' , 'e*e-b-e+d+d+b+e*d-b-c-e-b+b*f*d*b*c', 'e-a+c-a*b*d+c*f-c+a*f-e+d-e*e']

        gene_chroms = crossover(init_chroms)

        self.assertEqual(4, len(gene_chroms))

        self.assertEqual('e*d*e*a*b-b*b-c-e-b+b*f*d*b*c', gene_chroms[0])
        self.assertEqual('f*b*b-c*f+c*b+b-c-e-b+b*f*d*b*c', gene_chroms[2])

    def test_mutate(self):
        begin = 'f*b*b-c*f+c*b+b-c-e-b+b*f*d*b*c'
        after = mutate(begin)
        self.assertNotEqual(begin,after)
        # print(after)
        gene_set = {'a', 'b', 'c', 'd', 'e', 'f', '+', '-', '*'}
        for s in after:
            self.assertIn(s, gene_set)

    def test_check_chromosome(self):
        right_chroms = ['e*d*e*a*b-b*e*c+f+a+a+c', 'f*b*b-c*f+c*b+d*d+b+e+a+f+e', 'e*e-b-e+d+d+b+e*d-b-c-e-b+b*f*d*b*c',
                       'e-a+c-a*b*d+c*f-c+a*f-e+d-e*e']
        for rc in right_chroms:
            self.assertTrue(check_chromosome(rc))

        error_chroms = ['e*d*e*a*b-b*e*cef+a+a+c', 'f*b*-c*f+c*b+d*d+b+e+a+f+e', 'e*e-bbe+d+d+b+e*d-b-c-e-b+b*f*d*b*c',
                       'e-a+c-a*+*d+c*f-++a*f-e+d-e*e']
        for ec in error_chroms:
            self.assertFalse(check_chromosome(ec))



if __name__ == '__main__':
    unittest.main()
