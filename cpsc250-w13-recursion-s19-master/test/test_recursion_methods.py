import unittest
from inspect import signature

from src.recursion_methods import *

class TestRecursionMethods(unittest.TestCase):
    
    def test_MaxEmpty(self):
        lst=[]
        exp=None
        act = max_list_recursive(lst)

        self.assertEqual(exp,act,msg="{} returns {} for max not {}".format(lst,exp,act))


    def test_MaxOne(self):
        lst = [11]
        exp = 11
        act = max_list_recursive(lst)
        self.assertEqual(exp,act,msg="{} returns {} for max not {}".format(lst,exp,act))


    def test_MaxPositives(self):
        lst =[1, 3, 13, 2, 4, 42, 0, 99]
        exp = 99;
        act = max_list_recursive(lst)
        self.assertEqual(exp,act,msg="{} returns {} for max not {}".format(lst,exp,act))

    def test_MaxNegatives(self):
        lst =[-3, -13, -2, -4, -42, -99, -6]
        exp = -2
        act = max_list_recursive(lst)
        self.assertEqual(exp, act, msg="{} returns {} for max not {}".format(lst,exp,act))

    def test_MaxMixed(self):
        lst =[-1, 3, -13, 2, -4, 42, 0, -6]
        exp = 42;
        act = max_list_recursive(lst)
        self.assertEqual(exp, act, msg="{} returns {} for max not {}".format(lst,exp,act))

    def test_SumEmpty(self):
        lst =[]
        exp = 0
        act = sum_list_recursive(lst)
        self.assertEqual(exp, act, msg="{} returns {} for sum not {}".format(lst, exp, act))

    def test_SumOne(self):
        lst =[11]
        exp = 11
        act = sum_list_recursive(lst)
        self.assertEqual(exp, act, msg="{} returns {} for sum not {}".format(lst, exp, act))

    def test_SumPositives(self):
        lst =[1, 3, 13, 2, 4, 42, 0, 99]

        exp = 164
        act = sum_list_recursive(lst)
        self.assertEqual(exp, act, msg="{} returns {} for sum not {}".format(lst, exp, act))

    def test_SumNegatives(self):
        lst =[-1, -3, -13, -2, -4, -42, 0, -99, -6]

        exp = -170
        act = sum_list_recursive(lst)
        self.assertEqual(exp, act, msg="{} returns {} for sum not {}".format(lst, exp, act))

    def test_SumMixed(self):
        lst =[-1, 3, -13, 2, -4, 42, 0, 99, -6]

        exp = 122
        act = sum_list_recursive(lst)
        self.assertEqual(exp, act, msg="{} returns {} for sum not {}".format(lst, exp, act))



    def test_InvalidNegative(self):
        try:
            calc_seq(-1)
            self.fail("Failed to throw exception for negative index")
        except IndexError:
            pass
        except Exception:
            self.fail(msg="Throw IndexError for negative index")
            
        calc_seq(4) # Make sure we attempted something


    def test_Index0(self):
        self.assertEqual(0, calc_seq(0))
    

    def test_Index1(self):
        self.assertEqual(1, calc_seq(1))
    

    def test_Index2(self):
        self.assertEqual(2, calc_seq(2))
    

    def test_Index3(self):
        self.assertEqual(1, calc_seq(3))
    

    def test_Index4(self):
        self.assertEqual(-2, calc_seq(4))
    

    def test_Index5(self):
        self.assertEqual(-5, calc_seq(5))
    

    def test_Index6(self):
        self.assertEqual(-4, calc_seq(6))
    

    def test_Index7(self):
        self.assertEqual(3, calc_seq(7))
    

    def test_Index8(self):
        self.assertEqual(12, calc_seq(8))
    

    def test_Index15(self):
        self.assertEqual(103, calc_seq(15))
    

    def test_Index22(self):
        
        self.assertEqual(692, calc_seq(22))


if __name__ == '__main__':
    unittest.main()
