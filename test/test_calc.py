import inspect
import os

import pytest
from Shape.shapes.calc import Calc
from Shape.utilities import Utilities
import dotenv


# some init
dotenv.load_dotenv()
utilities = Utilities()


@pytest.fixture()
def test_calc():
    return Calc()


@pytest.mark.test_calc_triangle_perimeter
def test_triangle_perimeter(test_calc):
    try:
        assert test_calc.triangle_perimeter() == float(os.getenv("SHAPE_PERIMETER"))
        utilities.write_file(str(inspect.currentframe().f_code.co_name)
                             + " " + os.getenv("TEST_PASS") + str(test_calc.detect.list_of_sides) + "\n")
    except AssertionError:
        utilities.write_file(str(inspect.currentframe().f_code.co_name) +
                             " " + os.getenv("TEST_FAILED") + str(test_calc.detect.list_of_sides) + "\n")


@pytest.mark.test_calc_triangle_area
def test_triangle_area(test_calc):
    try:
        assert test_calc.triangle_area() == float(os.getenv("SHAPE_AREA"))
        utilities.write_file(str(inspect.currentframe().f_code.co_name)
                             + " " + os.getenv("TEST_PASS") + str(test_calc.detect.list_of_sides) + "\n")
    except AssertionError:
        utilities.write_file(str(inspect.currentframe().f_code.co_name) +
                             " " + os.getenv("TEST_FAILED") + str(test_calc.detect.list_of_sides) + "\n")


@pytest.mark.test_calc_square_area
def test_square_area(test_calc):
    try:
        assert test_calc.square_area() == float(os.getenv("SHAPE_AREA"))
        utilities.write_file(str(inspect.currentframe().f_code.co_name)
                             + " " + os.getenv("TEST_PASS") + str(test_calc.detect.list_of_sides) + "\n")
    except AssertionError:
        utilities.write_file(str(inspect.currentframe().f_code.co_name) +
                             " " + os.getenv("TEST_FAILED") + str(test_calc.detect.list_of_sides) + "\n")


@pytest.mark.test_calc_square_perimeter
def test_square_perimeter(test_calc):
    try:
        assert test_calc.square_perimeter() == float(os.getenv("SHAPE_PERIMETER"))
        utilities.write_file(str(inspect.currentframe().f_code.co_name)
                             + " " + os.getenv("TEST_PASS") + str(test_calc.detect.list_of_sides) + "\n")
    except AssertionError:
        utilities.write_file(str(inspect.currentframe().f_code.co_name) +
                             " " + os.getenv("TEST_FAILED") + str(test_calc.detect.list_of_sides) + "\n")


@pytest.mark.test_calc_rectangle_perimeter
def test_rectangle_perimeter(test_calc):
    try:
        assert test_calc.rectangle_perimeter() == float(os.getenv("SHAPE_PERIMETER"))
        utilities.write_file(str(inspect.currentframe().f_code.co_name)
                             + " " + os.getenv("TEST_PASS") + str(test_calc.detect.list_of_sides) + "\n")
    except AssertionError:
        utilities.write_file(str(inspect.currentframe().f_code.co_name) +
                             " " + os.getenv("TEST_FAILED") + str(test_calc.detect.list_of_sides) + "\n")


@pytest.mark.test_calc_rectangle_area
def test_rectangle_area(test_calc):
    try:
        assert test_calc.rectangle_area() == float(os.getenv("SHAPE_AREA"))
        utilities.write_file(str(inspect.currentframe().f_code.co_name)
                             + " " + os.getenv("TEST_PASS") + str(test_calc.detect.list_of_sides) + "\n")
    except AssertionError:
        utilities.write_file(str(inspect.currentframe().f_code.co_name) +
                             " " + os.getenv("TEST_FAILED") + str(test_calc.detect.list_of_sides) + "\n")
