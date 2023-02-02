from Shape.shapes.detect import *
from Shape.shapes.calc import *


def check_exist_obj_in_list(first_list_of_objects, second_list_of_objects):
    """
    This function get two lists and check if there is same common object(Shape)
    NOTE: These two objects are different, but for us, they are same (because the arrays)
            {"sides": [6, 4, 3], "area": 6, "perimeter": 12}
            {"sides": [6, 3, 4], "area": 6, "perimeter": 12}
    :param first_list_of_objects:
    :param second_list_of_objects:
    :return bool:
    """
    for index, first_item in enumerate(first_list_of_objects):
        list1_object = set(first_list_of_objects[index].get("sides"))
        for second_item in second_list_of_objects:
            list2_object = set(second_item.get("sides"))
            if list1_object == list2_object:
                return True
    return False


def is_exist(dictionary, list_shapes):
    """
    This function get dictionary(the values are lists) and list and check
    if there is same common object in the list and in the dictionary's values
    :param dictionary:
    :param list_shapes:
    :return bool:
    """
    for list_values in dictionary:
        new_list_value = dictionary[list_values]
        flag = check_exist_obj_in_list(new_list_value, list_shapes)
        if flag:
            return True
    return False


def calculate_shape(list_of_shapes, raise_an_error):
    dict_shapes = {}
    try:
        for shape in list_of_shapes:
            if raise_an_error:
                if is_rectangle(shape):
                    raise ValueError("Is not shape")

                if is_triangle(shape):
                    raise ValueError("Is not shape")

                if is_square(shape):
                    raise ValueError("Is not shape")
              #  else:
                    # add dict
    except ValueError as e:
        return str(e)







