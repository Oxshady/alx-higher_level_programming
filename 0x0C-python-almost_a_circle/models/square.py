#!/usr/bin/python3
"""
contain square inheritc from Rectangle class
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
    def __str__(self):
        """
		overrides __str__
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

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
        return {'id': self.id,'size': self.size, 'x': self.x, 'y': self.y}
if __name__ == "__main__":

    s1 = Square(5)
    print(s1)
    print(s1.area())
    s1.display()

    print("---")

    s2 = Square(2, 2)
    print(s2)
    print(s2.area())
    s2.display()

    print("---")

    s3 = Square(3, 1, 3)
    print(s3)
    print(s3.area())
    s3.display()
