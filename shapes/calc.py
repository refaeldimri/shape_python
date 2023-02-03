import json
import math
import os

from Shape.shapes.detect import *
import dotenv

# some init
dotenv.load_dotenv()


class Calc(object):
    def __init__(self):
        self.detect = Detect(json.loads(os.getenv("SHAPE")))

    def rectangle_perimeter(self):
        """
        This function get a list of sides and
        check if it can be rectangle
        and his perimeter
        :return float:
        """
        try:
            if not self.detect.is_rectangle():
                raise ValueError(os.getenv("NOT_RECTANGLE"))
            perimeter = 0
            for side in self.detect.list_of_sides:
                perimeter += side
            return perimeter
        except ValueError as e:
            return str(e)

    def rectangle_area(self):
        """
        This function get a list of sides and
        check if it can be rectangle
        and his area
        :return float:
        """
        try:
            if not self.detect.is_rectangle():
                raise ValueError(os.getenv("NOT_RECTANGLE"))
            set_of_sides = set(self.detect.list_of_sides)
            if len(list(set_of_sides)) == 1:
                return list(set_of_sides)[0] ** 2
            else:
                return list(set_of_sides)[0] * list(set_of_sides)[1]
        except ValueError as e:
            return str(e)

    def triangle_perimeter(self):
        """
        This function get a list of sides and
        check if it can be triangle
        and calculate his perimeter
        :return float:
        """
        try:
            if not self.detect.is_triangle():
                raise ValueError(os.getenv("NOT_TRIANGLE"))
            perimeter = 0
            for side in self.detect.list_of_sides:
                perimeter += side
            return perimeter
        except ValueError as e:
            return str(e)

    def triangle_area(self):
        """
        This function get a list of sides and
        check if it can be rectangle
        and his area
        :return float:
        """
        try:
            if not self.detect.is_triangle():
                raise ValueError(os.getenv("NOT_TRIANGLE"))
            semi_perimeter = (self.triangle_perimeter()) / 2
            return \
                math.sqrt(semi_perimeter * (semi_perimeter - self.detect.list_of_sides[0]) *
                          (semi_perimeter - self.detect.list_of_sides[1]) *
                          (semi_perimeter - self.detect.list_of_sides[2]))
        except ValueError as e:
            return str(e)

    def square_area(self):
        """
        This function get a list of sides and
        check if it can be square
        and his area
        :return float:
        """
        try:
            if not self.detect.is_square():
                raise ValueError(os.getenv("NOT_SQUARE"))
            return self.detect.list_of_sides[0] ** 2
        except ValueError as e:
            return str(e)

    def square_perimeter(self):
        """
        This function get a list of sides and
        check if it can be
        and calculate his perimeter
        :return float:
        """
        try:
            if not self.detect.is_square():
                raise ValueError(os.getenv("NOT_SQUARE"))
            return self.detect.list_of_sides[0] * 4
        except ValueError as e:
            return str(e)
