import json
import os

from Shape.shapes.calc import Calc
import dotenv


# some init
dotenv.load_dotenv()


class Complex(object):

    def __init__(self):
        self.calc = Calc()
        self.list_complex = json.loads(os.getenv("PARAMETER_LIST_COMPLEX"))
        self.raise_error = int(os.getenv("RAISE_ERROR"))

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
            if self.raise_error:
                for shape in self.list_complex:
                    self.calc.detect.list_of_sides = shape
                    if not self.calc.detect.is_rectangle() and not \
                            self.calc.detect.is_triangle() and not self.calc.detect.is_square():
                        raise ValueError(str(shape) + " Is not shape")
            else:
                for shape in self.list_complex:
                    self.calc.detect.list_of_sides = shape
                    if self.calc.detect.is_rectangle():
                        s = set()
                        s.add(self.calc.rectangle_area())
                        s.add(self.calc.rectangle_perimeter())
                        if not self.check_duplicate_shape(list_of_set, s):
                            dict_shapes["rectangles"].append(self.create_object(shape))
                            list_of_set.append(s)
                    elif self.calc.detect.is_triangle():
                        s = set()
                        s.add(self.calc.triangle_area())
                        s.add(self.calc.triangle_perimeter())
                        if not self.check_duplicate_shape(list_of_set, s):
                            dict_shapes["triangles"].append(self.create_object(shape))
                            list_of_set.append(s)
                    elif self.calc.detect.is_square():
                        s = set()
                        s.add(self.calc.square_area())
                        s.add(self.calc.square_perimeter())
                        if not self.check_duplicate_shape(list_of_set, s):
                            dict_shapes["squares"].append(self.create_object(shape))
                            list_of_set.append(s)
                return dict_shapes
        except ValueError as e:
            return str(e)
