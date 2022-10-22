# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k,
# and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        tripletList = []        # The final list of triplets
        tripletSetList = []     # A list of sets of triplets (to prevent duplicates)
        currentTriplet = []     # The triplet currently being looked at

        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):      # Iterate through every triplet

                    if nums[i] + nums[j] + nums[k] == 0:            # If the triplet sum == 0
                        currentTriplet = [nums[i],nums[j],nums[k]]  # Set this as currentTriplet

                        if set(currentTriplet) not in tripletSetList:   # If any permutation of this triplet has already been seen (checked via tripletSetList)
                            tripletList.append(currentTriplet)          # then add the currentTriplet to the list
                            tripletSetList.append(set(currentTriplet))  # and add the set of its elements to the tripletSetList (for future duplicate checking)
                        else:                                           # If not, ignore it
                            pass
                        
                        currentTriplet = []         # Reset the currentTriplet after each addition

                    else:                           # If the triplet sum != 0, ignore it
                        pass

        return tripletList      # Return the full list of triplets

sol = Solution()
tests = [[-1,0,1,2,-1,-4],[0,1,1],[0,0,0]]
for test in tests:
    print(sol.threeSum(test))