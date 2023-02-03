import dotenv


# some init
dotenv.load_dotenv()


class Detect(object):

    def __init__(self, list_of_sides):
        self.list_of_sides = list_of_sides

    def is_rectangle(self):
        """
        This function get list of sided and check if it can be rectangle
        :return bool:
        """
        for side in self.list_of_sides:
            if side <= 0:
                return False
        if len(self.list_of_sides) != 4:
            return False
        for side in self.list_of_sides:
            if not self.list_of_sides.count(side) == 2:
                return False
            else:
                return True

    def is_square(self):
        """
        This function get list of sided and check if it can be square
        :param list_of_sides:
        :return bool:
        """
        for side in self.list_of_sides:
            if side <= 0:
                return False
        if self.list_of_sides.count(self.list_of_sides[0]) == 4:
            return True
        return False

    def is_triangle(self):
        """
        This function get list of sided and check if it can be rectangle
        :return bool:
        """
        for side in self.list_of_sides:
            if side <= 0:
                return False
        if len(self.list_of_sides) != 3:
            return False
        if self.list_of_sides[0] + self.list_of_sides[1] > self.list_of_sides[2] and \
                self.list_of_sides[1] + self.list_of_sides[2] > \
                self.list_of_sides[0] and self.list_of_sides[0] + self.list_of_sides[2] > self.list_of_sides[1]:
            return True
        return False





