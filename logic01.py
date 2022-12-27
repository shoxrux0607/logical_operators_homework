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
    y = a < b and a < c
    return y


print(main(3, 4, 5))
