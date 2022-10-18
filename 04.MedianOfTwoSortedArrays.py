# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
            nums3 = []
            median = 0          # Declaring the median variable early... not necessary in Python but probably good practice.
            checker1 = 0
            checker2 = 0
            i = 0
            while i <= (len(nums1)+len(nums2))/2:       # Iterate over the arrays, up to halfway
                if nums1[checker1] < nums2[checker2]:
                    nums3.append(nums1[checker1])       # Compare values at the checker1/checker2 indices, add the lowest and scroll past it in that array
                    checker1 += 1                       # This means always we are appending the next lowest value to nums3
                else:                                   # We only need to get to halfwayas then we have definitely included the median
                    nums3.append(nums2[checker2])       # It will either be the last value in the nums3 array (odd cases) or halfway between nums3[-2] and nums3[-1] (even cases)
                    checker2 += 1
                i += 1
            if (len(nums1) + len(nums2))%2 != 0:        # Produce the correct median depending on evenness/oddness...
                median = nums3[len(nums3)-1]/1.0        # (Dividing by 1.0 to go from int to float)
            else:
                median = (nums3[len(nums3)-2] + nums3[len(nums3)-1])/2
            return median                               # Return the median

sol = Solution()
tests = [[1,3,7],[2,4,5,6],[3,6,6,7],[1,1,1,1,1,1,1,1,1,1,7,7,7,7,7,7,7]]
for i in range(1,len(tests)):
    print(sol.findMedianSortedArrays(tests[i-1], tests[i]))