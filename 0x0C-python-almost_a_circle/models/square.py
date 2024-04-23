#!/usr/bin/python3
"""
contain square inheritc from Rectangle class
"""


import turtle
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    square inheritc from Rectangle class

    Args:
    size of the square
    x of the square
    y of the square
    id of the square
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        overrides __str__
        """
        s = "[Square] ({}) {}/{}\
        - {}".format(self.id, self.x, self.y, self.width)
        return s

    @property
    def size(self):
        """
        size getter
        """
        return (self.__size)

    @size.setter
    def size(self, S):
        """
        size setter
        """
        if type(S) is not int:
            raise TypeError("height must be an integer")
        if S <= 0:
            raise ValueError("height must be > 0")
        self.__size = S

    def update(self, *args, **kwargs):
        """
        Update the attributes of the square instance
        """
        if len(args) > 0:
            if len(args) > 4:
                raise ValueError("Incorrect number of positional arguments")
            if args[0] is not None:
                self.id = args[0]
            if args[1] is not None:
                self.size = args[1]
            if args[2] is not None:
                self.x = args[2]
            if args[3] is not None:
                self.y = args[3]
        for k, v in kwargs.items():
            if k == "id":
                self.id = v
            elif k == "size":
                self.size = v
            elif k == "x":
                self.x = v
            elif k == "y":
                self.y = v

    def to_dictionary(self):
        """
        returns the dictionary representation of a Square
        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

    def draw(self, window):
        """
        draw the Square
        """
        turtle.up()
        turtle.goto(self.x, self.y)
        turtle.down()

        for _ in range(4):
            turtle.forward(self.size)
            turtle.right(90)
