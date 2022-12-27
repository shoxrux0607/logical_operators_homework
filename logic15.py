def main(a):
    """
    Given a three-digit integer a, 
     check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    
    x = a % 10
    y = a // 10 % 10
    z = a // 100
    c = x + y + z

    return c % 2 != 0


print(main(322))
