"""
  Calculate Fibonacci value using both loop and recursion

  @author <your name here>
  @version 0
 """

class Fibonacci:

    def __init__(self):
        # Initialize counters
        self.loop_count = 0
        self.recursion_count = 0

    def fibonacci_loop(self, n):
        """
        Calculate value of Fibonacci sequence at given index
        using a loop (150 style)
            Raise a IndexError if n < 0
        :param n: index
        :return: value at index
        """
        
        self.loop_count += 1 # count this call

        pass  # @todo -fix this

    def fibonacci_recursion(self,n):
        """
        Calculate value of Fibonacci sequence at given index
        using recursion (250 style)
            Raise a IndexError if n < 0
        :param n: index
        :return: value at index
        """
        self.recursion_count += 1 # count this call
        pass  # @todo -fix this


if __name__ == '__main__':

    print("  index     loop (count)   recursion (count)")
    for i in range(16):
    # i = 5;
        fib=Fibonacci()
        print(" fib[{:2d}] = {:15d}({:3}) {:15d} ({:3d})".format(i,
                                               fib.fibonacci_loop(i),fib.loop_count,
                                               fib.fibonacci_recursion(i), fib.recursion_count))

