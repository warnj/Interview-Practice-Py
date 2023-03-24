import unittest

from general_questions.array2d import Array2dPractice


class Array2dTesting(unittest.TestCase):
    a = Array2dPractice()

    def testLongestCommonPrefix(self):
        self.assertEqual(27, self.a.getLargestRhombusSum([[1,2,3,4],[6,7,8,9],[4,5,6,7],[9,8,7,6]], 2))
        # example: size=3
        # [1,2,3,4,5,7]
        # [6,7,8,9,2,4]  -> max(3+7+4+8+7+6+8+9, 4+8+5+7+6+7+9+2) -> max(52,48) -> 52
        # [4,5,6,7,8,9]
        # [9,8,7,6,7,1]
        # [9,8,7,6,7,1]
        self.assertEqual(52, self.a.getLargestRhombusSum([[1,2,3,4,5,7],[6,7,8,9,2,4],[4,5,6,7,8,9],[9,8,7,6,7,1],[9,8,7,6,7,1]], 3))


if __name__ == '__main__':
    unittest.main()
