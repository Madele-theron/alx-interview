#!/usr/bin/python3
"""
A method that calculates the fewest number of operations needed
to result in exactly n H characters in the file.
"""

def minOperations(n):
    """
    Repeatedly divides n by its smallest prime factor and adds the result to 
    count until n becomes 1.
    """
    count = 0
    operations = 2

    while n > 1:
        while n % operations == 0:
            count += operations
            n /= operations
        operations += 1

    return count
