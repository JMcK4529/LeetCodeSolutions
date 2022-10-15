# Given an integer x, return true if x is palindrome integer.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:           # Quickly rule out any negative ints, as anything with a minus sign cannot be palindromic
            return False
        else:
            forward = x
            reversed = 0
            while x > 0:        # Reverse the number
                digit = x % 10
                reversed = (reversed * 10) + digit
                x = x // 10
            if reversed == forward: # Compare the original number (now stored as a copy, forward) with the reversed one
                return True         # If they are the same, it's a palindrome. Return True.
            else:
                return False        # If not, return False.

sol = Solution()
tests = [123,313,4455665544,-112,-111]
for test in tests:
    print(sol.isPalindrome(test))