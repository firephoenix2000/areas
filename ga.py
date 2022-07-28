# -- coding: utf-8 --
# @Time : 7/20/22 8:23 AM
# @Author : yudejun
# @Email : yudejun2000@outlook.com
# @File : ga.py
# @Software: PyCharm
import random

from shape import generate_triangle_data, Triangle, Point

CHECK_CHROMOSOME_NUMBER = 200
SELECTED_NUMBER = 20
TRIANGLE_POINT_SCOPE=10
MUTUTAION_PROBABILITY = 0.03
gene_list = ['a', 'b', 'c', 'd', 'e', 'f', '+', '-', '*']
symbol_list = ['a', 'b', 'c', 'd', 'e', 'f']
operator_list = ['+', '-', '*']


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
        # print('before select  number is', len(tmp1_chromosomes))
        selected = select(tmp1_chromosomes)

        # 2. crossover
        tmp1_chromosomes = crossover(selected)

        # 3. mutate
        length = len(tmp1_chromosomes)
        x = int(length*MUTUTAION_PROBABILITY)
        for j in range(x):
            t = random.randint(0,length-1)
            tmp1_chromosomes[t] = mutate(tmp1_chromosomes[t])

        # print('after select and corssover number is', len(tmp1_chromosomes))

        if i%10==0:
            print('now is {} times result.'.format(i))
            test_chromose =selected[0]
            print(test_chromose)
            print('calculate delta is {}'.format(calc_delta(test_chromose)))



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
        while chrom_len%2 == 0:  # and must be odd number
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

    #each chromosome was tested with 200 sets of randomly generated data, save average delta
    for i in range(CHECK_CHROMOSOME_NUMBER):
        (x1, y1, x2, y2, x3, y3) = generate_triangle_data(TRIANGLE_POINT_SCOPE)
        triangle = Triangle(Point(x1, y1), Point(x2, y2), Point(x3, y3))
        area = triangle.calc_area()
        data_item = [x1,y1,x2,y2,x3,y3,area]
        data.append(data_item)


    chromo_dict = {}
    i = 0
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
            i=i+1
            # chromo_dict[aver_delta] = chromosome
            chromo_dict[chromosome] = aver_delta

        if len(chromosomes) > 3*len(chromo_dict):
            print(chromosomes)
            print(chromo_dict)
        # print("the dict length is {0}, i is {1}, chrom length is {2}".format(len(chromo_dict), i,len(chromosomes)))

    except Exception:
        print("calculate is error: {}".format(chromosome))
        raise

    #maybe have some better method to do it, just do now!
    selected = []

    body, delta = zip(*chromo_dict.items())
    body_list = list(body)
    delta_list = list(delta)

    delta_list.sort(reverse= False)

    for m in range(SELECTED_NUMBER):
        # print(m)
        # the_chromo = chromo_dict.get(delta_list[m])
        the_chromo = [k for k,v in chromo_dict.items() if v == delta_list[m]]

        # must insert a string, not a list
        selected.append(the_chromo[0])

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
    # print(chromosomes)
    base_number = int(len(chromosomes)/2)
    # print('base_number is: ', base_number)
    for i in range(base_number):
        tmp_chrom1 = chromosomes[i]
        for k in range(base_number):
            tmp_chrom2 = chromosomes[base_number+k]

            magic_number = random.random()+1.6
            # length1 = int(len(tmp_chrom1)/magic_number)+1
            length1 = int(len(tmp_chrom1) / magic_number) + 1
            length2 = int(len(tmp_chrom2)/2)

            # print(type(tmp_chrom1))
            # print(type(tmp_chrom2))
            # print(len(tmp_chrom1), len(tmp_chrom2))
            #
            # print('length1 is :', length1)
            # print('length2 is :', length2)

            first_half = tmp_chrom1[0:length1]
            second_half = tmp_chrom2[length2:]
            # print("tmp_chrom1 is: ", tmp_chrom1)
            # print("first_half is: ", first_half)
            #
            # print("tmp_chrom2 is: ", tmp_chrom2)
            # print("second_half is: ", second_half)


            if first_half[-1] in symbol_list  and second_half[0] in symbol_list:
                first_half = tmp_chrom1[0:length1-1]

            if second_half[0] in operator_list and first_half[-1] in operator_list:
                second_half = second_half[1:]

            # print("first_half is: ", first_half)
            # print("second_half is: ", second_half)
            # print(first_half)
            # print(second_half)

            # new_chromosome = first_half.join(second_half)
            tmp_list = first_half + second_half


            # print(type(tmp_list))

            new_chromosome = ''.join(tmp_list)

            # if had same chromsome, mutate it !
            while new_chromosome in generate_chromosomes:
                new_chromosome = mutate(new_chromosome)


            # check it is right
            if check_chromosome(new_chromosome):
                generate_chromosomes.append(new_chromosome)
            else:
                print('it is not a right chromosome : {}'.format(new_chromosome))
                raise

    newlist = set(generate_chromosomes)
    if len(newlist) < len(generate_chromosomes):
        print('have {} repeat items!'.format(len(generate_chromosomes)-len(newlist)))

    return generate_chromosomes


def calc_delta(chromosome):

    data = []
    total_delta = 0

    #each chromosome was tested with 200 sets of randomly generated data, save average delta
    for i in range(CHECK_CHROMOSOME_NUMBER):
        (x1, y1, x2, y2, x3, y3) = generate_triangle_data(50)
        triangle = Triangle(Point(x1, y1), Point(x2, y2), Point(x3, y3))
        area = triangle.calc_area()
        data_item = [x1,y1,x2,y2,x3,y3,area]
        data.append(data_item)

    for item in data:
        a = item[0]
        b = item[1]
        c = item[2]
        d = item[3]
        e = item[4]
        f = item[5]
        s = item[6]
        result = 0.5 * abs(eval(chromosome))
        delta = (result - s) / s
        total_delta += abs(delta)

    aver_delta = total_delta / len(data)

    return aver_delta


def mutate(chromosome):
    '''
    Perform mutation processing on a given chromosome, and randomly select 1 to 4 symbols to change.
    letters become to letter, operators become to operators.
    Args:
        chromosome: source chromosome

    Returns: target chromosome

    '''

    new_chromosome = chromosome
    (a, b, c, d, e, f) = generate_triangle_data(10)

    #Ensue that the generated chromosome can be calculated through  while, try, except
    while new_chromosome == chromosome:
        try:
            # change number
            k = random.randint(1,4)
            tmp_list = list(new_chromosome)
            for i in range(k):
                #change location
                m = random.randint(0, len(chromosome)-1)
                if tmp_list[m]  in symbol_list:
                    tmp_list[m] = random.choice(symbol_list)
                elif tmp_list[m] in operator_list:
                    tmp_list[m] = random.choice(operator_list)
            mutated_chromosome =''.join(tmp_list)
            eval(mutated_chromosome)
            new_chromosome = mutated_chromosome
        except Exception:
            print("cannt calculate the formula: {}".format(mutated_chromosome))
            # raise

    return new_chromosome


def check_chromosome(chromosome):

    flag = True
    # print(len(chromosome))
    for i in range(len(chromosome)):
        # print(i)
        if chromosome[i] not in gene_list:
            flag = False
        if i%2 == 0:  # odd number, from zero
            if chromosome[i] not in symbol_list:
                flag = False
        elif i%2 == 1: # even number
            if chromosome[i] not in operator_list:
                flag = False

    return flag


if __name__ == '__main__':
    # chromosomes = init_chromosomes(60)
    # selected = select(chromosomes)
    # new_chromosomes = crossover(selected)
    result = genetic_algorithm(500)
    print(result)