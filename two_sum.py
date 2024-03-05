# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
# target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
#
#
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
#
# Constraints:
#
# 2 <= nums.length <= 104
# -109 <= target <= 109
# -109 <= nums[i] <= 109


# naive solution would be to have two loops that keep the index of two pointers to values in the list and test each
# permutation


from typing import List


# Brute force solution
# Time: O(n^2)
# Space: O(1)?
def two_sum(nums: List[int], target: int) -> List[int]:
    res = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if (nums[i] + nums[j]) == target:
                res = [i, j]
                break
    return res


print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))
print(two_sum([-1, -2, -3, -4, -5], -8))
