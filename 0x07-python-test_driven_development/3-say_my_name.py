#!/usr/bin/python3
"""print 1st and last name"""


def say_my_name(first_name, last_name=""):
    """ print 1st and last name
        Arguments:
            @first_name: 1st name
            @second_name: 2nd name
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
