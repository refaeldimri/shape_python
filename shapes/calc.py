import math

from Shape.shapes.detect import *


def rectangle_perimeter(list_of_sides):
    """
    This function get a list of sides and
    check if it can be rectangle
    and his perimeter
    :param list_of_sides:
    :return float:
    """
    try:
        if not is_rectangle(list_of_sides):
            raise ValueError("Is not rectangle")
        perimeter = 0
        for side in list_of_sides:
            perimeter += side
        return perimeter
    except ValueError as e:
        return str(e)


def rectangle_area(list_of_sides):
    """
    This function get a list of sides and
    check if it can be rectangle
    and his area
    :param list_of_sides:
    :return float:
    """
    try:
        if not is_rectangle(list_of_sides):
            raise ValueError("Is not rectangle")
        set_of_sides = set(list_of_sides)
        if len(list(set_of_sides)) == 1:
            return list(set_of_sides)[0] ** 2
        else:
            return list(set_of_sides)[0] * list(set_of_sides)[1]
    except ValueError as e:
        return str(e)


def triangle_perimeter(list_of_sides):
    """
    This function get a list of sides and
    check if it can be triangle
    and calculate his perimeter
    :param list_of_sides:
    :return float:
    """
    try:
        if not is_triangle(list_of_sides):
            raise ValueError("Is not triangle")
        perimeter = 0
        for side in list_of_sides:
            perimeter += side
        return perimeter
    except ValueError as e:
        return str(e)


def triangle_area(list_of_sides):
    """
    This function get a list of sides and
    check if it can be rectangle
    and his area
    :param list_of_sides:
    :return float:
    """
    try:
        if not is_triangle(list_of_sides):
            raise ValueError("Is not triangle")
        semi_perimeter = (triangle_perimeter(list_of_sides)) / 2
        return \
            math.sqrt(semi_perimeter * (semi_perimeter - list_of_sides[0]) *
                      (semi_perimeter - list_of_sides[1]) * (semi_perimeter - list_of_sides[2]))
    except ValueError as e:
        return str(e)
