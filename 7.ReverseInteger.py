# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2**31, 2**31 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# In a 32-bit-only environment, the try/except should catch any oversized ints and return 0 instead.
class Solution:
  def reverse(self, x: int) -> int:
    try:
        isNeg = False
        if x < 0:
            isNeg = True        # If the number is negative, make a note of it for later
        x = abs(x)              # Work with |x| instead
        reversed = 0
        while x > 0:            # Reverse the number by grabbing each digit and adding it to the "reversed" variable
            digit = x % 10
            reversed = (reversed * 10) + digit
            x = x // 10
        if isNeg:
            return reversed*-1  # If the number was originally negative, make it negative again
        else:
            return reversed     # Otherwise, just return the reversed number
    except MemoryError:
        return 0                # Return 0 if the value goes outside the 32-bit range, triggering an exception

# There is also a sort of cheat's method using Python's ability to switch easily between str() and int().
# class Solution:
#     def reverse(self, x: int) -> int:
#         try:
#             isNeg = False
#             if x < 0:
#                 isNeg = True
#             x = str(abs(x))
#             if isNeg:
#                 y = "-"
#             else:
#                 y = ""
#             for i in range(1,len(x)+1):
#                 y += x[-i]
#             y = int(y)
#             return y
#         except MemoryError:
#             return 0

sol = Solution()
tests = [123,-123,4676,-2211]
for test in tests:
    print(sol.reverse(test))