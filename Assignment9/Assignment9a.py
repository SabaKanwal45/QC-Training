"""
This file contains add function that takes two arguments in the form
add(a)(b) and return sum  of a and b
"""


def add(x):
    """
    can be called as add(4)(5)
    :param x: first number
    :return: sum
    """
    return lambda y: x+y
