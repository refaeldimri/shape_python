import json
import os

from Shape.shapes.complex import Complex


if __name__ == '__main__':
    cmp = Complex()
    print(type(cmp.calculate_shape()))
    print(cmp.calculate_shape())
    print(type(json.dumps(os.getenv("RESULR_LIST_COMPLEX"))))
