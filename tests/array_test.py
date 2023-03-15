import unittest

from general_questions.array import ArrayPractice


class ArrayTesting(unittest.TestCase):
    a = ArrayPractice()

    def testMaxSubarraySumCircular(self):
        self.assertEqual(3, self.a.maxSubarraySumCircular([1, -2, 3, -2]))
        self.assertEqual(10, self.a.maxSubarraySumCircular([5,-3,5]))
        self.assertEqual(-2, self.a.maxSubarraySumCircular([-3,-2,-3]))


if __name__ == '__main__':
    unittest.main()
