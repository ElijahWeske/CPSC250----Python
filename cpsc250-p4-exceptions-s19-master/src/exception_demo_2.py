class ExceptionDemo2:
    @staticmethod
    def method():
        ## Try these 5 different commands below
        # raise ArithmeticError("ArithmeticError") # try these as well!
        # raise RuntimeError("RuntimeError")
        # raise AttributeError("Attribute error")
        # div_by_zero = 12 / 0
        div_by_two = 12 / 2  # No exception here!
        print("Tootles")


if __name__ == '__main__':

    # This is almost the same as ExceptionDemo1, with one minor difference
    try:
        ExceptionDemo2.method();
        print("Yahoo!")
    except Exception as e:
        println("Exception first!")
        # return # try with and without the return here!
    except ArithmeticException as e:
        print("Math rules!")
        # return # try with and without the return here!
    except RuntimeError as e:
        print("Runtime rules!")
        # return # try with and without the return here!
    finally:
        print("Finally!")
        # return # try with and without the return here!

    print("I love Rock’n Roll")
