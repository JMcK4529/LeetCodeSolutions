# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subList = []            # This will be a list of all the non-repeating substrings
        currentSub = []         # This will be a list of the characters found in each pass

        for i in range(len(s)):                 # Iterate through the characters in the string
            currentSub.append(s[i])             # Add it to the currentSub

            for j in range(i+1,len(s)):         # Iterate through all the so far unchecked characters
                if s[j] in currentSub:          # If it has already been seen...
                    subList.append(currentSub)  # End the currentSub by adding it to the subList
                    break                       # and stop looking at this substring
                else:                           # If it HASN'T already been seen,
                    currentSub.append(s[j])     # add it to the currentSub

            currentSub = []                     # Reset the currentSub before moving onto the next starting character

        return len(subList[subList.index(max(subList,key=len))])    # Return the length of the longest substring in subList

sol = Solution()
tests = ["abcabcbb","bbbbb","pwwkew"]
for test in tests:
    print(sol.lengthOfLongestSubstring(test))