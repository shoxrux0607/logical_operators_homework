from math import *


def main(a, b, c):
    """
    Given three integers a, b, c, 
     check the following statement "The number b is between a and c".
    Args:
        a(int): parameter a
        b(int): parameter b
        c(int): parameter c
    Returns:
        bool: answer
    """
    x = floor(a)
    y = floor(b)
    z = floor(c)
    answer = (x == a < y == b and y == b < z == c) or ( x == a > y == b and y == b > z == c)
    return answer


print(main(13, 15, 1))
