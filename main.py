from field import field
from gen_random import gen_random
from unique import Unique
from print_result import print_result
from cm_timer import cm_timer_1
from cm_timer import cm_timer_2
from time import sleep

# The first task
#     goods = [
#         {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#         {'title': 'Диван для отдыха', 'color': 'black', 'price': 4500},
#         {'title': 'Кресло', 'color': "brown"},
#         {'title': 'Кафель', 'color': 'grey', 'price': 700, 'square': 70}
#     ]
#     field(goods,'title', 'price')
#     field(goods,'color')
# The second task
# arr = gen_random(5,1,5)
# print(arr)


# The third task
# data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
# obj = Unique(data, ignore_case=False)
# try:
#     while True:
#         print(obj.__next__(), end=' ')
# except StopIteration:
#     print('\nКонец цикла')

# The fourth task
# with lambda-function
# result_with_lambda = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]
# print(sorted(result_with_lambda, key=lambda el: abs(el), reverse=True))
#
# # without lambda-function
# result = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]
# print(sorted(result_with_lambda, key=abs, reverse=True))

# The fifth task
# @print_result
# def test_1():
#     return 1
#
#
# @print_result
# def test_2():
#     return 'iu5'
#
#
# @print_result
# def test_3():
#     return {'a': 1, 'b': 2}
#
#
# @print_result
# def test_4():
#     return [1, 2]
#
#
# print('!!!!!!!!')
# test_1()
# test_2()
# test_3()
# test_4()


# the sixth task
if __name__ == '__main__':
#realisation throught class
    with cm_timer_1():
        sleep(3)
#realisation throught contextmanager
    with cm_timer_2():
        sleep(3)


