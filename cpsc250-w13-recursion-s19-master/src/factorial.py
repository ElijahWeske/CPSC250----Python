"""
  Calculate factorial using both loop and recursion

  @author <your name here>
  @version 0
 """

def factorial_loop(n):
    """
      Calculate factorial using a loop (150 style)
        Raise a ValueError if n < 0
    :param n: number
    :return: n!
    """

    pass  # @todo -fix this


def factorial_recursion(n):
    """
    Calculate factorial using recursion (250 style!)
        Raise a ValueError if n < 0
    :param n:
    :return: n!
    """
    pass  # @todo -fix this


if __name__ == '__main__':
    for i in range(16):
    # i = 5;
        print(" {:2d}! = {:15d} {:15d}".format(i, factorial_loop(i), factorial_recursion(i)))
