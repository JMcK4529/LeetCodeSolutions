# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxSize = 0                                 # The maximum container size so far
        for i in range(len(height)-1):
            for j in range(i,len(height)):          # Iterate through each pair of lines
                conWidth = j-i                      # Find the width
                if height[i] <= height[j]:          # Find the lowest height of the pair
                    conHeight = height[i]           # this is the point at which water would
                else:                               # start to leak out of the container
                    conHeight = height[j]

                if conWidth*conHeight > maxSize:    # Check the container area compared to the
                    maxSize = conWidth*conHeight    # current maxSize and update if larger
                else:
                    pass
        return maxSize                              # Return the maximum size recorded

sol = Solution()
tests = [[1,8,6,2,5,4,8,3,7],[1,1]]
for test in tests:
    print(sol.maxArea(test))