from src.my_very_own_error import MyVeryOwnError
class ExceptionDemo3:
    @staticmethod
    def method():
        try:
            #arithmetic exception
            divByZero = 12 / 0
            print(" divByZero=", divByZero)

        except Exception as e:
            print("Caught exception:",e)
            # Try raising these 3 exceptions, and try without any of them
            #raise Exception(str(e))
            #raise MyVeryOwnError(str(e))
            #raise RuntimeError(str(e))
        finally:
            print("Tootles")


if __name__ == '__main__':

    try:
        ExceptionDemo3.method()
        print("Yahoo!")
    except RuntimeError as e:
        print("Runtime rules!")
    except MyVeryOwnError as e:
        print("MyVeryOwnError rules!")

    print("I love Rock’n Roll")


