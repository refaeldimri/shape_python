import json
import os
from collections import Counter

from Shape.shapes.calc import Calc
import dotenv


# some init
dotenv.load_dotenv()


class Complex(object):
    list_complex_utils = []

    def __init__(self):
        self.calc = Calc()
        self.list_complex = json.loads(os.getenv("PARAMETER_LIST_COMPLEX"))
        self.raise_error = int(os.getenv("RAISE_ERROR"))

    @staticmethod
    def check_exist_shape(item_insert):
        flag = True
        for item in Complex.list_complex_utils:
            if Counter(item_insert) == Counter(item):
                return True
        if flag:
            return False

    @staticmethod
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

    def check_duplicate_list(self):
        for item in self.list_complex:
            if not Complex.check_exist_shape(item):
                Complex.list_complex_utils.append(item)
        return Complex.list_complex_utils

    def create_object(self, sides):
        """
        This function get a list of sides and create an object shape:
        {side: "", area: "", perimeter: ""}
        :param sides:
        :return object:
        """
        self.calc.detect.list_of_sides = sides
        shape = {"sides": sides}
        if self.calc.detect.is_triangle():
            shape["area"] = round(self.calc.triangle_area(), 2)
            shape["perimeter"] = round(self.calc.triangle_perimeter(), 2)
        if self.calc.detect.is_rectangle():
            shape["area"] = round(self.calc.rectangle_area(), 2)
            shape["perimeter"] = round(self.calc.rectangle_perimeter(), 2)
        if self.calc.detect.is_square():
            shape["area"] = round(self.calc.square_area(), 2)
            shape["perimeter"] = round(self.calc.square_perimeter(), 2)
        return shape

    def calculate_shape(self):
        """
        This function get list of shape and bool parameter and create
        dictionary of only shape without duplicate
        :return dict:
        """
        Complex.list_complex_utils = self.check_duplicate_list()
        dict_shapes = {
            "rectangles": [],
            "triangles": [],
            "squares": []
        }
        try:
            if self.raise_error:
                for shape in Complex.list_complex_utils:
                    self.calc.detect.list_of_sides = shape
                    if not self.calc.detect.is_rectangle() and not \
                            self.calc.detect.is_triangle() and not self.calc.detect.is_square():
                        raise ValueError(str(shape) + " Is not shape")
            else:
                for shape in Complex.list_complex_utils:
                    self.calc.detect.list_of_sides = shape
                    if self.calc.detect.is_rectangle():
                        dict_shapes["rectangles"].append(self.create_object(shape))
                    elif self.calc.detect.is_triangle():
                        dict_shapes["triangles"].append(self.create_object(shape))
                    elif self.calc.detect.is_square():
                        dict_shapes["squares"].append(self.create_object(shape))
                return dict_shapes
        except ValueError as e:
            return str(e)
