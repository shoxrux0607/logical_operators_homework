from math import *


def main(n):
    """
    A number consisting of one and zero is given (the number starts at once). 
    If the number of ones is greater than zero, true, otherwise False is returned.

    Args:
        n(int): parameter n
    Returns:
        bool: answer
    """
    12345
    d_1 = n % 10
    d_2 = n//10 % 10
    d_3 = n//100 % 10
    d_4 = n//1000 % 10
    d_5 = n//10000

    count_1 = d_1 == 1
    count_1 += d_2 == 1
    count_1 += d_3 == 1
    count_1 += d_4 == 1
    count_1 += d_5 == 1

    count_0 = d_1 == 0 and (d_2 or d_3 or d_4 or d_5)
    count_0 += d_2 == 0 and (d_3 or d_4 or d_5)
    count_0 += d_3 == 0 and (d_4 or d_5)
    count_0 += d_4 == 0 and d_5

    answer = count_1 > count_0
    return answer


print(main(1100))
