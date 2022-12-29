def main(x):
    """
    Given an integer x, return true if x is palindrome integer.
    An integer is a palindrome when it reads the same backward as forward.

    Args:
        x(int): parameter x
    Returns:
        bool: answer
    """
  

    return (x >= 10 and x < pow(10,2) and x%10 == x//10) or (x >= pow(10,2) and x < pow(10,3) and x%10 == x//100)


print(main(121))
