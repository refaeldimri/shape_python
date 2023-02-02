from Shape.shapes.detect import *
from Shape.shapes.calc import *
from Shape.shapes.complex import *


if __name__ == '__main__':

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
    a = [
        {"sides": [4, 1, 2], "area": 6, "perimeter": 12},
        {"sides": [6, 2, 1], "area": 6, "perimeter": 12},
        ]

    # print(dict1.get("triangles"))
    def check_exist_obj_in_list(first_list_of_objects, second_list_of_objects):
        for index, first_item in enumerate(first_list_of_objects):
            list1_object = set(first_list_of_objects[index].get("sides"))
            for second_item in second_list_of_objects:
                list2_object = set(second_item.get("sides"))
                if list1_object == list2_object:
                    return True
        return False

    def is_exist(dictionary, list_shapes):
        for list_values in dictionary:
            new_list_value = dictionary[list_values]
            flag = check_exist_obj_in_list(new_list_value, list_shapes)
            if flag:
                return True
        return False

    print(is_exist(dict1, a))




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




