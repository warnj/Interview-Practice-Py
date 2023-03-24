import sys
import math
from typing import List


class Array2dPractice:
    # return the largest rhombus sum in a matrix of given size
    # example: size=2
    # [1,2,3,4]      2     3     7     8
    # [6,7,8,9]  -> 6 8   7 9   4 6   5 7  ->  max(21  25  25  27)  ->  27
    # [4,5,6,7]      5     6     8     7
    # [9,8,7,6]
    def __rhombusSum(self, matrix, size, x, y):
        # print('summing for (x,y)=({},{})'.format(x,y))
        sum = 0
        xlo = x
        xhi = x
        for i in range(2*size-1):
            # print('i={} ylo={} yhi={}, xlo={}, xhi={}'.format(i, y, y+2*size-1, xlo, xhi))
            sum += matrix[y+i][xlo]
            if xlo != xhi:
                sum += matrix[y+i][xhi]
            if i < (2*size-1)//2:
                xlo -= 1
                xhi += 1
            else:
                xlo += 1
                xhi -= 1
        return sum
    def getLargestRhombusSum(self, matrix, size):
        maxSum = -sys.maxsize
        # height/width of rhombus = 2*size-1
        for x in range(size-1, len(matrix[0])-size+1):
            for y in range(0, len(matrix)-(2*size-1)+1):
                # find (x,y) that is the top point of a rhombus
                curSum = self.__rhombusSum(matrix, size, x, y)
                # print('cursum={}'.format(curSum))
                maxSum = max(maxSum, curSum)
        return maxSum


def main() -> None:
    a = Array2dPractice()
    print(a.getLargestRhombusSum([1, -2, 3, -2], 1))


if __name__ == "__main__":
    main()
