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
MUTUTAION_PROBABILITY = 0.03
gene_list = ['a', 'b', 'c', 'd', 'e', 'f', '+', '-', '*']


def genetic_algorithm(epochs=1000):
    '''
    It is used for genetic and evolutionary algorithms to calculate the triangle area.
    Args:
        epochs: the number of iteration
    Returns: the best chromosome formula
    '''

    i_chromosomes = init_chromosomes(100)

    tmp1_chromosomes = i_chromosomes
    #the first epoch
    # selected = select(i_chromosomes)
    # tmp1_chromosomes = crossover(selected)

    for i in range(epochs):
        # 1. select
        selected = select(tmp1_chromosomes)

        # 2. crossover
        tmp1_chromosomes = crossover(selected)

        # 3. mutate
        length = len(tmp1_chromosomes)
        x = int(length*MUTUTAION_PROBABILITY)
        for j in range(x):
            t = random.randint(0,length)
            tmp1_chromosomes[t] = mutate(tmp1_chromosomes[t])


    the_best_chromosome = selected[0]

    return the_best_chromosome


def init_chromosomes(num=100):
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
    try:
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

            chromo_dict[aver_delta] = chromosome
    except Exception:
        print("calculate is error: {}".format(chromosome))
        raise

    #maybe have some better method to do it, just do now!
    selected = []

    delta, body = zip(*chromo_dict.items())
    body_list = list(body)
    delta_list = list(delta)


    delta_list.sort(reverse= False)

    for m in range(SELECTED_NUMBER):
        the_chromo = chromo_dict.get(delta_list[m])
        selected.append(the_chromo)

    return selected


def crossover(chromosomes):
    '''
    for a given odered chromosomes list, crossover refers to the operation of replacing and
    recombinging part of the structure of the two parent chromosome to generate a new individual
    20->100, 10->25,  4->4,
    Args:
        chromosomes: the parents chromosome

    Returns: after generated chromosomes,

    '''

    generate_chromosomes =[]
    base_number = int(len(chromosomes)/2)
    for i in range(base_number):
        tmp_chrom1 = chromosomes[i]
        for k in range(base_number):
            tmp_chrom2 = chromosomes[base_number+k]
            length1 = int(len(tmp_chrom1)/2)+1
            length2 = int(len(tmp_chrom2)/2)+1
            first_half = tmp_chrom1[:length1]
            second_half = tmp_chrom2[length2:]
            new_chromosomes = first_half + second_half
            generate_chromosomes.append(new_chromosomes)


    return generate_chromosomes



def mutate(chromosome):
    '''

    Args:
        chromosome:

    Returns:

    '''

    new_chromosome = chromosome
    (a, b, c, d, e, f) = generate_triangle_data(10)

    #Ensue that the generated chromosome can be calculated through  while, try, except
    while new_chromosome == chromosome:
        try:
            k = random.randint(1,4)
            tmp_list = list(new_chromosome)
            for i in range(k):
                m = random.randint(0, len(chromosome))
                tmp_list[m] = random.choice(gene_list)
            mutated_chromosome =''.join(tmp_list)
            eval(mutated_chromosome)
            new_chromosome = mutated_chromosome
        except Exception:
            print("cannt calculate the formula: {}".format(mutated_chromosome))

    return new_chromosome



if __name__ == '__main__':
    # chromosomes = init_chromosomes(60)
    # selected = select(chromosomes)
    # new_chromosomes = crossover(selected)
    result = genetic_algorithm(1000)
    print(result)