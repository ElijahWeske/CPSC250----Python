
class ExceptionDemo1:
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
        try:
            ExceptionDemo1.method();
            print("Yahoo!")
        except ArithmeticError as e:
            print("Math rules!")
            # return # try with and without the return here!
        except RuntimeError as e:
            print("Runtime rules!")
            # return # try with and without the return here!
        except Exception as e:
            println("Exception last!")
            # return # try with and without the return here!
        finally:
            print("Finally!")
            # return # try with and without the return here!

        print("I love Rock’n Roll")
