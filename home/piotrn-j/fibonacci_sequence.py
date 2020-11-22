"""
Fibonacci sequence
"""

import unittest
import datetime


def fib_it(n):
    """Iterative method"""

    no1 = 1
    no2 = 0

    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        for i in range(n):
            no1_old = no1
            no1 = no2
            no2 = no1_old + no1

    return no2


print(fib_it(19))

num1 = 1
num2 = 0


def fib_rec(n):
    """Recursive method"""

    global num1
    global num2

    num1_old = num1
    num1 = num2
    num2 = num1 + num1_old

    if n > 1:
        fib_rec(n-1)

    return num2


print(fib_rec(19))


class FibonacciTest(unittest.TestCase):
    """Test for Fibonacci sequence functions"""

    def test_handcrafted_examples(self):
        """Test some hand picked examples"""
        self.assertEqual(fib_it(19), 4181)
        self.assertEqual(fib_rec(19), 4181)

    def test_both_methods(self):
        """Check if both functions return same results"""
        for test_case in range(1, 1000):
            result_it = fib_it(test_case)
            result_rec = fib_rec(test_case)

            self.assertEqual(result_it, result_rec)


# def test_time():

#    """Compare differences in running time of both functions"""

#    global difference_for_1000

#    it1 = datetime.datetime.now
#    fib_it(1000)
#    it2 = datetime.datetime.now
#    time_it = it2 - it1

#    rec1 = datetime.datetime.now
#    fib_rec(1000)
#    rec2 = datetime.datetime.now
#    time_rec = rec2 - rec1

#    difference_for_1000 = time_rec/time_it


# test_time()

# This code is a failure and I do not really know why

if __name__ == '__main__':

    unittest.main()

    print(fib_it(1000))
    print("Recursion method is", difference_for_1000, "times longer for the number 1000")

    print(datetime.datetime.now)