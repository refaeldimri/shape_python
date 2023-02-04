import json
import os
from collections import Counter

from Shape.shapes.complex import Complex
from Shape.shapes.complex import *


if __name__ == '__main__':
    cmp = Complex()
    print(type(cmp.calculate_shape()))
    print(cmp.calculate_shape())
    # print(type(json.dumps(os.getenv("RESULT_LIST_COMPLEX"))))
    #
    # initializing list
    # test_list = [[2, 2, 2, 2], [3, 4, 5], [5, 6, 6], [2, 3, 2, 3], [2, 3, 8], [3, 4, 5]]
    # list2 = []
    # item_insert = [4, 5, 6]
    # print(cmp.check_duplicate_list())
   # print(Complex.check_exist_shape([1, 2, 3]))



    # # printing original list
    # print("The original list : " + str(test_list))
    #
    # # removing duplicate sublist
    # res1 = []
    # for i in test_list:
    #     x = sorted(i)
    #     res1.append(x)
    # res = []
    # for i in res1:
    #     if tuple(i) not in res:
    #         res.append(tuple(i))
    #
    # # print result
    # print("The list after duplicate removal : " + str(res))
    #
    # for i in range(len(res)):
    #     res[i] = list(res[i])
    # print("The list after duplicate removal : " + str(res))















