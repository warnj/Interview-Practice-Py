import unittest

from general_questions.array import ArrayPractice


class ArrayTesting(unittest.TestCase):
    a = ArrayPractice()

    def testMaxSubarraySumCircular(self):
        self.assertEqual(3, self.a.maxSubarraySumCircular([1, -2, 3, -2]))
        self.assertEqual(10, self.a.maxSubarraySumCircular([5, -3, 5]))
        self.assertEqual(-2, self.a.maxSubarraySumCircular([-3, -2, -3]))

    def testSwapOnceIncr(self):
        self.assertTrue(self.a.swapOnceIncr([1, 5, 10, 20]))
        self.assertTrue(self.a.swapOnceIncr([1, 3, 900, 10]))
        self.assertFalse(self.a.swapOnceIncr([13, 31, 30]))
        self.assertFalse(self.a.swapOnceIncr([20, 10, 9, 8]))
        self.assertTrue(self.a.swapOnceIncr([91, 20]))
        self.assertTrue(self.a.swapOnceIncr([17, 18, 91, 20]))

    def testConcatSum(self):
        self.assertEquals(198, self.a.concatSum([1, 2, 3]))
        self.assertEquals(1344, self.a.concatSum([10, 2]))


if __name__ == '__main__':
    unittest.main()
