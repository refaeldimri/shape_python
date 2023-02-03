import inspect
import json
import os

import pytest
from Shape.shapes.detect import Detect
from Shape.utilities import Utilities
import dotenv


# some init
dotenv.load_dotenv()
utilities = Utilities()


@pytest.fixture()
def test_detect():
    return Detect(json.loads(os.getenv("SHAPE")))


@pytest.mark.test_det_triangle
def test_is_triangle(test_detect):
    try:
        assert test_detect.is_triangle() == eval(os.getenv("IS_SHAPE"))
        utilities.write_file(str(inspect.currentframe().f_code.co_name)
                             + " " + os.getenv("TEST_PASS") + str(test_detect.list_of_sides) + "\n")
    except AssertionError:
        utilities.write_file(str(inspect.currentframe().f_code.co_name) +
                             " " + os.getenv("TEST_FAILED") + str(test_detect.list_of_sides) + "\n")


@pytest.mark.test_det_rectangle
def test_is_rectangle(test_detect):
    try:
        assert test_detect.is_rectangle() == eval(os.getenv("IS_SHAPE"))
        utilities.write_file(str(inspect.currentframe().f_code.co_name)
                             + " " + os.getenv("TEST_PASS") + str(test_detect.list_of_sides) + "\n")
    except AssertionError:
        utilities.write_file(str(inspect.currentframe().f_code.co_name) +
                             " " + os.getenv("TEST_FAILED") + str(test_detect.list_of_sides) + "\n")


@pytest.mark.test_det_square
def test_is_square(test_detect):
    try:
        assert test_detect.is_square() == eval(os.getenv("IS_SHAPE"))
        utilities.write_file(str(inspect.currentframe().f_code.co_name)
                             + " " + os.getenv("TEST_PASS") + str(test_detect.list_of_sides) + "\n")
    except AssertionError:
        utilities.write_file(str(inspect.currentframe().f_code.co_name) +
                             " " + os.getenv("TEST_FAILED") + str(test_detect.list_of_sides) + "\n")
