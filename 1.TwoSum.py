# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
                for j in range(len(nums)):
                    # For every pair of values (i,j) in nums, do they sum to the target?
                    # Do not pair any value with itself (i.e. i != j)
                    if i != j:
                        if nums[i] + nums[j] == target:
                            return [i,j]

# Test inputs
nums1 = [2,7,11,15]
target1 = 9

nums2 = [3,2,4]
target2 = 6

nums3 = [3,3]
target3 = 6

# Instantiating the Solution class
sol = Solution()

# Test 1, should print [0,1]
print(sol.twoSum(nums1,target1))

# Test 2, should print [1,2]
print(sol.twoSum(nums2,target2))

# Test 3, should print [0,1]
print(sol.twoSum(nums3,target3))