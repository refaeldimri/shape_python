from collections import Counter
from Shape.shapes.detect import *
from Shape.shapes.calc import *


def check_duplicate_shape(list_set, set_shape):
    """
    This function get list and list of list and check if this list exist in the list
    NOTE: These two list are different, but for this function, they are same
        [6, 4, 3]
        [6, 3, 4]
    :param list_set:
    :param set_shape:
    :return bool:
    """
    return list_set.count(set_shape) == 1


def create_object(sides):
    """
    This function get a list of sides and create an object shape:
    {side: "", area: "", perimeter: ""}
    :param sides:
    :return object:
    """
    shape = {"sides": sides}
    if is_triangle(sides):
        shape["area"] = triangle_area(sides)
        shape["perimeter"] = triangle_perimeter(sides)
    if is_rectangle(sides):
        shape["area"] = rectangle_area(sides)
        shape["perimeter"] = rectangle_perimeter(sides)
    if is_square(sides):
        shape["area"] = sides[0] ** 2
        shape["perimeter"] = sides[0] * 4
    return shape


def calculate_shape(list_of_shapes, raise_an_error):
    """
    This function get list of shape and bool parameter and create
    dictionary of only shape without duplicate
    :param list_of_shapes:
    :param raise_an_error:
    :return:
    """
    s = set()
    list_of_set = []
    dict_shapes = {
        "rectangles": [],
        "triangles": [],
        "squares": []
    }
    try:
        if raise_an_error:
            for shape in list_of_shapes:
                if not is_rectangle(shape) and not is_triangle(shape) and not is_square(shape):
                    raise ValueError(str(shape) + " Is not shape")
        else:
            for shape in list_of_shapes:
                if is_rectangle(shape):
                    s = set()
                    s.add(rectangle_area(shape))
                    s.add(rectangle_perimeter(shape))
                    if not check_duplicate_shape(list_of_set, s):
                        dict_shapes["rectangles"].append(create_object(shape))
                        list_of_set.append(s)
                elif is_triangle(shape):
                    s = set()
                    s.add(triangle_area(shape))
                    s.add(triangle_perimeter(shape))
                    if not check_duplicate_shape(list_of_set, s):
                        dict_shapes["triangles"].append(create_object(shape))
                        list_of_set.append(s)
                elif is_square(shape):
                    s = set()
                    s.add(shape[0] ** 2)
                    s.add(shape[0] ** 2)
                    if not check_duplicate_shape(list_of_set, s):
                        dict_shapes["squares"].append(create_object(shape))
                        list_of_set.append(s)
            return dict_shapes
    except ValueError as e:
        return str(e)