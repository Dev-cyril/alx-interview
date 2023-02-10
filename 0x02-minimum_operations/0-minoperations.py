#!/usr/bin/python3
"""
    Minimum Operations
"""

def minOperations(n):
    """A function that calculates the minimum number of operations
        needed to result in n H characters

        Retun: minimum number of operations
    """
    index = 1
    c_p = 0
    num_op = 0
    while index < n:
        remainder = n - index
        if (remainder % index == 0):
            c_p = index
            index += c_p
            num_op += 2
        else:
            index += c_p
            num_op += 1
    return num_op

