import sys
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


def main() -> None:
    a = ArrayPractice()
    print(a.maxSubarraySumCircular([1, -2, 3, -2]))


if __name__ == "__main__":
    main()
