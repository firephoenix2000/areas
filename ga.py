# -- coding: utf-8 --
# @Time : 7/20/22 8:23 AM
# @Author : yudejun
# @Email : yudejun2000@outlook.com
# @File : ga.py
# @Software: PyCharm
import random

from shape import generate_triangle_data, Triangle, Point

CHECK_CHROMOSOME_NUMBER = 200
SELECTED_NUMBER =20
TRIANGLE_POINT_SCOPE=10

def genetic_algorithm(epochs=1000):
    '''
    It is used for genetic and evolutionary algorithms to calculate the triangle area.
    Args:
        epochs: the number of iteration
    Returns: the best chromosome formula
    '''
    gene_set = ['a', 'b', 'c', 'd', 'e', 'f', '+', '-', '*']
    chromosomes = generate_chromosomes(100)
    # furmula is  the best chromosome
    formula =  chromosomes[0]

    for i in range(epochs):
        pass



    return formula


def generate_chromosomes(num=100):
    '''
    chromosome length must be odd number
    Args:
        num:

    Returns:
    '''

    gene_list = ['a', 'b', 'c', 'd', 'e', 'f', '+', '-', '*']
    random.seed()
    chromosomes = []
    for i in range(num):
        chromosome = []
        chrom_len = random.randint(20, 60) # the chromosome length is between in 25 and 60
        while chrom_len%2 == 0:
            chrom_len = random.randint(20, 60)

        for k in range(chrom_len):
            if k%2 == 0:
                chromosome.append(gene_list[random.randint(0, 5)])
            elif k%2 == 1:
                chromosome.append(gene_list[random.randint(6, 8)])

        chromosomes.append(''.join(chromosome))
    return chromosomes



def select(chromosomes):
    '''
    select the chromosomes that can be calculated ,and then from these chromosomes,
    find the top 20 ??? fitness, and arrange them in order.
    Args:
        chromosomes:  will to be selected chromosomes list, no order

    Returns:
        results: after selected and ordered, if result is great 20, return 20 , else return
        the number of can be calculated
    '''


    data = []

    for i in range(CHECK_CHROMOSOME_NUMBER):
        (x1, y1, x2, y2, x3, y3) = generate_triangle_data(TRIANGLE_POINT_SCOPE)
        triangle = Triangle(Point(x1, y1), Point(x2, y2), Point(x3, y3))
        area = triangle.calc_area()
        data_item = [x1,y1,x2,y2,x3,y3,area]
        data.append(data_item)

    chromo_dict = {}
    i = 0
    #each chromosome was tested with 100 sets of randomly generated data, save average delta
    for chromosome in chromosomes:
        total_delta = 0
        for item in data:
            a = item[0]
            b = item[1]
            c = item[2]
            d = item[3]
            e = item[4]
            f = item[5]
            s = item[6]
            result = 0.5 * abs(eval(chromosome))
            delta = (result - s)/s
            total_delta += abs(delta)

        aver_delta = total_delta/len(data)

        # chromo_dict[chromosome] = aver_delta
        chromo_dict[aver_delta] = chromosome

    #maybe have some better method to do it, just do now!
    # print(chromo_dict)

    selected = []

    delta, body = zip(*chromo_dict.items())
    body_list = list(body)
    delta_list = list(delta)


    delta_list.sort(reverse= False)

    for m in range(SELECTED_NUMBER):
        the_chromo = chromo_dict.get(delta_list[m])
        selected.append(the_chromo)

    return selected


def crossover():
    pass



def mutate():
    pass



if __name__ == '__main__':
    chromosomes = generate_chromosomes(60)
    selected = select(chromosomes)