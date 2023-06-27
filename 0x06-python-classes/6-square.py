#!/usr/bin/python3
"""class square"""


class Square():
    """square class with size"""

    def __init__(self, size=0, position=(0, 0)):
        """"Initialization"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """"size getter"""
        return self.__size

    @property
    def position(self):
        """"position getter"""
        return self.__position

    @size.setter
    def size(self, value):
        """"size setter"""
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """"position setter"""
        if (type(value) is not tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(value[0]) is not int) or (type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """"square area"""
        return self.size ** 2

    def my_print(self):
        """print square"""
        if self.size == 0:
            print()
        else:
            for x in range(self.position[1]):
                print("")
            for x in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
