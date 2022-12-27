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
    x = a < b and a < c
    return x


print(main(3, 4, 5))
