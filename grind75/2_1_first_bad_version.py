# 278. First Bad Version
# Solved
# Easy
# Topics
# Companies
# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
#
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
#
# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
#
#
#
# Example 1:
#
# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.
# Example 2:
#
# Input: n = 1, bad = 1
# Output: 1
#
#
# Constraints:
#
# 1 <= bad <= n <= 231 - 1


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # some sort of binary search should be done here
        # two pointers?
        # 1 -> n
        # but how do you decide to go right or left?
        # oh if its good go right, if its bad go left
        l, r = 1, n
        while l <= r:
            mid = (r + l) // 2  # take the midpoint of left and right
            is_bad = isBadVersion(mid)
            if is_bad:
                # check if -1 is bad, if it isnt thats the first bad version
                if not isBadVersion(mid - 1):
                    return mid
                r = mid - 1
            else:
                l = mid + 1
