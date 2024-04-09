class Rectangle:
    """
    Rectangle class:
        Private instance attribute: width:
            property def width(self): to retrieve it
            property setter def width(self, value): to set it:
                width must be an integer, otherwise raise a TypeError
                exception with the message width must be an integer
                if width is less than 0, raise a ValueError
                exception with the message width must be >= 0
        Private instance attribute: height:
            property def height(self): to retrieve it
            property setter def height(self, value): to set it:
                height must be an integer, otherwise raise a
                TypeError exception with the message height must be an integer
                if height is less than 0, raise a ValueError
                exception with the message height must be >= 0
        Instantiation with optional width and height:
            def __init__(self, width=0, height=0):
        Public instance method: def area(self):
        that returns the rectangle area
        Public instance method: def perimeter(self):
        that returns the rectangle perimeter:
                if width or height is equal to 0,
                perimeter has to be equal to 0
        print() and str() should print the rectangle with
        the character #: (see example below)
                if width or height is equal to 0,
                return an empty string
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        return "#" * self.__width + "\n" + ("#" * self.__width + "\n") * (self.__height - 1)
