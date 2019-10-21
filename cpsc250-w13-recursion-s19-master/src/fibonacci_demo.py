"""
Demo the cost of recursion for Fibonacci sequences
"""
class FibonacciDemo:

    def __init__(self):
        self.loop_count = 0;
        self.rec_count = 0;

    def fib_loop(self, n):
        a = 0
        b = 1
        while (n > 0):
            oldA = a
            a = b
            b = oldA + b
            n-=1
            self.loop_count+=1

        return a


    def print_level(self, level,  string):
        for i in range(level):
            print("\t",end='')
        print(" l({:3d}) r({:3d})  >{}".format( level,self.rec_count,string))


    def fib_recursion(self, n, level):
        self.rec_count+=1
        if (n < 1):
            self.print_level(level, " fibR(" + str(n) + ")");
            return 0


        if (n == 1):
            self.print_level(level, " fibR(" + str(n) + ")");
            return 1

        self.print_level(level, "fibR({:3d}) = fibR({:3d}) + fibR({:3d})".format(n,
                n - 1, n - 2));
        a = self.fib_recursion(n - 1, level + 1)
        b = self.fib_recursion(n - 2, level + 1)
        self.print_level(level, " fibR({:3d}) = {:3d} + {:3d}".format(n, a, b));
        return a + b


if __name__ == '__main__':
    for i in range(8,9):
        # Reset counters for each top level call
        fib = FibonacciDemo()

        print("fib["+str(i) + "] =  loop:" + str(fib.fib_loop(i)) + " cnt(" + str(fib.loop_count) + ") recursion:"
                + str(fib.fib_recursion(i, 0)) + " (" + str(fib.rec_count) + ") ")

