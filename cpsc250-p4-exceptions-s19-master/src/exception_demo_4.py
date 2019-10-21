
class ExceptionDemo4:
    @staticmethod
    def method():
        a = 12
        b = 2 # try with b=0 as well
        if b != 0:
            # arithmetic exception
            division = a / b
            print(" division=", division)
        else:
            print(" skip division if b==0")
            raise RuntimeError("Raised a RuntimeError manually")
 
 
if __name__ == '__main__':
    try:
        ExceptionDemo4.method()
        print("Yahoo!")
    except Exception as e:
        print("Exception first!",e)

    print("Done demo 4")


    

