# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""

        lenList = []                                # First, find the shortest string and the
        for str in strs:                            # index at which it appears in strs
            lenList.append(len(str))
        shortIndex = lenList.index(min(lenList))

        for i in range(len(strs[shortIndex])):              # For every character in the shortest string
            matchCount = 0                                  # Keep track of how many matches there are for the character
            for j in range(len(strs)):                      # Check all the strings against the shortest one
                if j != shortIndex:                         # (Don't check shortest vs. shortest)
                    if strs[shortIndex][i] == strs[j][i]:   # If the characters match in the string,
                        matchCount += 1                     # add one to the matchCount

            if matchCount == len(strs)-1:                   # If one was counted for each string (except shortest)
                prefix += strs[shortIndex][i]               # Add the character to the prefix
            else:
                break                                       # If not, we have already found the longest prefix
        
        return prefix                                       # Return the prefix

sol = Solution()
tests = [["flower","flow","flight"],["dog","racecar","car"]]
for test in tests:
    print(sol.longestCommonPrefix(test))
