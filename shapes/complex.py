from Shape.shapes.detect import *
from Shape.shapes.calc import *


def check_exist_shape_in_list(list_of_shapes, shape_objct):
    """
    This function get list and obj and check if this obj exist in the list
    NOTE: These two objects are different, but for us, they are same (because the arrays)
            {"sides": [6, 4, 3], "area": 6, "perimeter": 12}
            {"sides": [6, 3, 4], "area": 6, "perimeter": 12}
    :param list_of_shapes:
    :param shape_objct:
    :return bool:
    """
    for item in list_of_shapes:
        if set(shape_objct.get("sides")) == set(item.get("sides")):
            return True
    return False


def is_exist(dictionary, shape_object):
    """
    This function get dictionary(the values are lists) and object and check
    if this object exist in the dictionary's list
    :param dictionary:
    :param shape_object:
    :return bool:
    """
    for list_values in dictionary.values():
        if check_exist_shape_in_list(list_values, shape_object):
            return True
    return False


def calculate_shape(list_of_shapes, raise_an_error):
    dict_shapes = {
        "rectangles": [],
        "triangles": [],
        "squares": []
    }
    try:
        for shape in list_of_shapes:
            if not raise_an_error:
                if is_rectangle(shape):
                    if not is_exist(dict_shapes, shape):
                        dict_shapes["rectangles"].append(shape)
                else:
                    raise ValueError("Is not shape")
                if is_triangle(shape):
                    if not is_exist(dict_shapes, shape):
                        dict_shapes["triangles"].append(shape)
                else:
                    raise ValueError("Is not shape")
                if is_square(shape):
                    if not is_exist(dict_shapes, shape):
                        dict_shapes["squares"].append(shape)
                    pass
                else:
                    raise ValueError("Is not shape")
            else:
                return dict_shapes
    except ValueError as e:
        return str(e)







