import random


def gen_random(num,min,max):
    my_list = []
    for iter in range (num):
        my_list.append(random.randint(min,max))
    return my_list
