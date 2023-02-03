import inspect
import os
import ast

import pytest
from Shape.utilities import Utilities
import dotenv
from Shape.shapes.complex import Complex


# some init
dotenv.load_dotenv()
utilities = Utilities()


@pytest.fixture()
def test_complex():
    return Complex()


@pytest.mark.test_complex_
def test_complex_shape(test_complex):
    try:
        assert test_complex.calculate_shape() == ast.literal_eval(os.environ["RESULT_LIST_COMPLEX"])
        utilities.write_file(str(inspect.currentframe().f_code.co_name)
                             + " " + os.getenv("TEST_PASS") + str(test_complex.list_complex) + "\n")
    except AssertionError:
        utilities.write_file(str(inspect.currentframe().f_code.co_name) +
                             " " + os.getenv("TEST_FAILED") + str(test_complex.list_complex) + "\n")
