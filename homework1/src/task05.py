"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    maximum = nums[0]
    for i in range(len(nums)):
        if nums[i] > maximum:
            maximum = nums[i]
        sub_array_value = nums[i]
        for j in range(i + 1, min(i + k, len(nums))):
            sub_array_value += nums[j]
            if sub_array_value > maximum:
                maximum = sub_array_value
    return maximum
