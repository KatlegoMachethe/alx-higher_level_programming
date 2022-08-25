#!/user/bin/python3
"""
Module rectangle
Has class "rectangle" which inherits from "Base"
"""


from models.base import Base


class Rectangle(Base):
    """
    Class inherit base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor: Instantiate rectangle
        """

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, w):
        """setter for width"""
        self.__width = w

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, h):
        """Height setter"""
        self.__height = h

    @property
    def x(self):
        """ x getter"""
        return self.__x

    @x.setter
    def x(self, x_value):
        """x setter"""
        self.__x = x_value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y_value):
        """y setter"""
        self.__y = y_value
