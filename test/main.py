from Shape.shapes.detect import *
from Shape.shapes.calc import *
from Shape.shapes.complex import *
from collections import Counter


if __name__ == '__main__':
    # s=set()
    # s1=set()
    # listt = []
    # s.add(2)
    # s.add(5)
    # listt.append(s)
    # print(s)
    # print(listt)
    # s1.add(3)
    # s1.add(52)
    # listt.append(s1)
    # print(s1)
    # print(listt)
    # print(check_duplicate_shape(listt, {8,9}))


    dict1 = {
            "triangles":
                [
                    {"sides": [9, 6, 4], "area":6, "perimeter":12},
                    {"sides": [3, 3, 6], "area":6, "perimeter":12},
                    {"sides": [3, 1, 6], "area": 6, "perimeter": 12}
                ],
            "squares": [{"sides": [2, 2, 1, 1], "area":2, "perimeter":6}, {"sides": [1, 4, 2], "area": 6, "perimeter": 12}],
            "rectangles": [{"sides": [3, 2, 6], "area": 6, "perimeter": 12}, {"sides": [3, 1, 6], "area": 6, "perimeter": 12}]
            }
    # # a = [
    # #     {"sides": [6, 3, 4], "area": 6, "perimeter": 12},
    # #     {"sides": [6, 2, 1], "area": 6, "perimeter": 12},
    # #     ]
    #
    # # print(dict1.get("triangles"))
    # b = {"sides": [8,9,7], "area": 6, "perimeter": 12}
    #
    # dict1["triangles"].append({"sides": [8,9,7], "area": 6, "perimeter": 12})
    #
    # a = [[1, 2, 3], [2, 2, 2, 2]]

    # c = [2,2,1,1]

    # for list_values in dict1.values():
    #     for item in list_values:
    #         set(item.get("sides")) == set(list)
    shapes = [[2, 2, 2, 2], [3, 4, 5], [5, 6, 6], [2, 3, 2, 3], [2, 3, 8], [3, 4, 5]]
 #   print(calculate_shape(b, False))
    print(calculate_shape(shapes, True))
    #print(is_exist(dict1, [3,4,5]))
    # print(triangle_perimeter([3, 4, 0]))
    # print(triangle_area([3, 4, 5]))
   # print(check_duplicate_shape([[3,4,5], [4,5,3], [9,6,4,3]]))





    # a = [
    #     {"sides": [6, 3, 4], "area": 6, "perimeter": 12},
    #     {"sides": [6, 3, 4], "area": 6, "perimeter": 12},
    # ]
    # b = [{"sides": [1, 4, 6], "area": 6, "perimeter": 12}, {"sides": [6, 2, 3], "area": 6, "perimeter": 12}]

    # a = set(a[0].get("sides"))
    # b = set(b.get("sides"))


    # def check_exist_obj_in_list(first_list_of_objects, second_list_of_objects):
    #     for index, item in enumerate(first_list_of_objects):
    #         list1_object = set(first_list_of_objects[index].get("sides"))
    #         for second_item in second_list_of_objects:
    #             list2_object = set(second_item.get("sides"))
    #             if list1_object == list2_object:
    #                 return True
    #     return False




