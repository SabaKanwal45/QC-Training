"""
This file contains Code for add function that accepts arbitrary number of arguments
pylint Score=9.29
"""
# pylint: disable-msg=C0103
numbers = []

add_iterator = lambda y: return_sum() if y is None else append_number(y)


def return_sum():
    """
    Calculate sum of globally defined list
    :return: sum
    """
    return sum(numbers)


def append_number(number):
    """
    Append given number to global numbers list
    :param number: Number to append
    :return:
    """
    numbers.append(number)
    print numbers
    return add_iterator


def add(x):
    """
    Add function takes arbitrary No of arguments and return sum
    :param x: first argument of add function
    :return: Sum of all iteration
    """
    global numbers
    numbers = [x]
    print numbers
    return add_iterator

print add(4)(3)
