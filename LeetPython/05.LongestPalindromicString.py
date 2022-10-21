# Given a string s, return the longest palindromic substring in s.
# A string is called a palindrome string if the reverse of that string is the same as the original string.

# For every substring (currentSub: str), check if it is palindromic
# If it is, add it to a subList
# Else move on
# return subList[subList.index(max(subList))]

class Solution:
    def isPalindrome(self, pal: str) -> bool:       # Defining a function to return True if the passed string is a palindrome
        isPalindrome = True
        for i in range(int(len(pal)/2)+1):          # For each character in the first half (rounded up) of the string
            if pal[i] == pal[-(i+1)]:               # check if it is the same as its corresponding character, starting at the other end
                pass                                # If it does, leave isPalindrome = True
            else:
                isPalindrome = False                # If not, then it is NOT a palindrome. So, isPalindrome = False
                break                               # So, we can stop checking
        return isPalindrome                         # Return the boolean isPalindrome

    def longestPalindrome(self, s: str) -> str:
        subList = []                                # Keep a record of all the palindromic strings
        currentSub = ""                             # Store a temporary string, currentSub

        for i in range(len(s)):
            for j in range(i+1,len(s)):             # Iterate through every pair of characters
                for k in range(i,j+1):              
                    currentSub += s[k]              # Add all the characters between (inclusive) to currentSub

                if self.isPalindrome(currentSub):   # If the currentSub is a palindrome
                    subList.append(currentSub)      # add it to the subList
                else:
                    pass                            # If not, then ignore it
                currentSub = ""                     # Reset the currentSub at the end of each loop

        return max(subList, key=len)                # Return the longest string in subList

sol = Solution()
tests = ["babad","cbbd"]
for test in tests:
    print(sol.longestPalindrome(test))