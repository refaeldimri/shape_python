def is_rectangle(list_of_sides):
    """
    This function get list of sided and check if it can be rectangle
    :param list_of_sides:
    :return bool:
    """
    if list_of_sides.count(list_of_sides[0]) == 4:
        return True
    for side in list_of_sides:
        if side <= 0:
            return False
    if len(list_of_sides) != 4:
        return False
    for side in list_of_sides:
        if list_of_sides.count(side) != 2:
            return False
        else:
            return True


def is_square(list_of_sides):
    """
    This function get list of sided and check if it can be square
    :param list_of_sides:
    :return bool:
    """
    for side in list_of_sides:
        if side <= 0:
            return False
    if list_of_sides.count(list_of_sides[0]) == 4:
        return True
    return False


def is_triangle(list_of_sides):
    """
    This function get list of sided and check if it can be rectangle
    :param list_of_sides:
    :return bool:
    """
    for side in list_of_sides:
        if side <= 0:
            return False
    if len(list_of_sides) != 3:
        return False
    for side in list_of_sides:
        if list_of_sides.count(side) > 1:
            return False
    if list_of_sides[0] + list_of_sides[1] > list_of_sides[2] and \
            list_of_sides[1] + list_of_sides[2] > list_of_sides[0] and list_of_sides[0] + list_of_sides[2] > list_of_sides[1]:
        return True
    return False





