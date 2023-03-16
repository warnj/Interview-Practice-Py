import sys
import math
from typing import List


class ArrayPractice:
    # https://leetcode.com/problems/maximum-sum-circular-subarray
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curSum, maxSum = 0, -sys.maxsize
        sums = 0
        for i in range(len(nums)):
            sums += nums[i]
            curSum += nums[i]
            maxSum = max(curSum, maxSum)
            if curSum < 0:
                curSum = 0
        curSum = 0
        max2 = 0
        for i in range(len(nums)):
            maxSum = max(maxSum, sums + max2)
            sums -= nums[i]
            curSum += nums[i]
            max2 = max(max2, curSum)
        return maxSum

    # returns the lowest int possible that is greater than lo from swapping any one pair of digits in tgt
    def __getSwap(self, lo, tgt) -> int:
        result = None
        num = list(map(int, list(str(tgt))))
        for i in range(len(num)-1):
            for j in range(i+1, len(num)):
                temp = num.copy()
                temp[i] = num[j]
                temp[j] = num[i]
                tInt = int("".join(str(x) for x in temp))
                if (not result and tInt > lo) or (result and result > tInt > lo):
                    result = tInt
        return result

    # given array of non-neg numbers, can choose any number from the array and swap any 2 digits
    # return if it's possible to apply swap at most once so elements are strictly increasing
    def swapOnceIncr(self, nums):
        swapped = False
        prevPrev = -sys.maxsize
        for i in range(1, len(nums)):
            prev = nums[i-1]
            cur = nums[i]
            if prev >= cur:
                if swapped:  # already done a swap, it's only allowed once
                    return False
                else:
                    s = self.__getSwap(prevPrev, prev)
                    if s:
                        swapped = True
                        # print('swapping {} for {}'.format(prev, s))
                        prev = s
                        nums[i-1] = s
                    else:
                        return False
            prevPrev = prev
        return True

    # given array of positive ints return sum of every possible string concatenation of a[i] and a[j]
    # example: [1,2,3] = 11+12+13+21+22+23+31+32+33=198
    def concatSum(self, nums: List[int]) -> int:
        lowSum = 0
        offsetSum = 0
        for i in range(len(nums)):
            lowSum += nums[i]
            size = len(str(nums[i]))
            offset = 10**size
            offsetSum += offset
        return lowSum * len(nums) + lowSum * offsetSum
    def concatSumSlowInts(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                result += self.__concatInts(nums[i], nums[j])
                if i != j:
                    result += self.__concatInts(nums[j], nums[i])
        return result
    def concatSumSlow(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                a = str(nums[i])
                b = str(nums[j])
                result += int(a+b) if i == j else int(a+b) + int(b+a)
        return result
    def concatSumSlowOG(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                print('i={} j={}'.format(i, j))
                result += int(str(nums[i]) + str(nums[j]))
        return result
    def __concatInts(self, x, y):
        if y != 0:
            a = math.floor(math.log10(y))
        else:
            a = -1
        return int(x*10**(1+a)+y)


def main() -> None:
    a = ArrayPractice()
    # print(a.maxSubarraySumCircular([1, -2, 3, -2]))
    # print(a.swapOnceIncr([1, 3, 9, 10]))


if __name__ == "__main__":
    main()
