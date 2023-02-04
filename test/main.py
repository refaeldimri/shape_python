import json
import os
from collections import Counter
from Shape.shapes.complex import Complex
from Shape.shapes.complex import *


def is_rectangle(listt):
    """
    This function get list of sided and check if it can be rectangle
    :return bool:
    """
    for side in listt:
        if side <= 0:
            return False
    if len(listt) != 4:
        return False
    for side in listt:
        if not listt.count(side) == 2:
            return False
    return True


if __name__ == '__main__':
    cmp = Complex()
    print(cmp.calc.detect.is_rectangle())
    print(cmp.calculate_shape())













