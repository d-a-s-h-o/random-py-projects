'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

nums = [2, 7, 11, 15]
List = []
target = 18

class Solution:
  def twoSum(self, nums: List, target: int) -> List:
    numToIndex = {}

    for i, num in enumerate(nums):
      if target - num in numToIndex:
        return numToIndex[target - num], i
      numToIndex[num] = i

    return None

new = Solution().twoSum(nums, target)
print(new)