# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
# The algorithm for myAtoi(string s) is as follows:
# Read in and ignore any leading whitespace.
# Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
# Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
# Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
# If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -2^31 should be clamped to -2^31, and integers greater than 2^31 - 1 should be clamped to 2^31 - 1.
# Return the integer as the final result.

class Solution:
    def myAtoi(self, s: str) -> int:
        s = list(s)
        parse = ""
        isNeg = False
        for char in s:              # For each character in the string
            if char != " ":         # Check for (and ignore) whitespace
                if char == "-":     # Make a note (isNeg = True) of negative numbers
                    isNeg = True
                elif char == "+":
                    pass
                else:
                    parse += char   # Add the character to the new string (parse)
        
        if len(parse) == 0:         # If parse is empty, the integer is 0
            return 0
        else:
            returnInt = int(parse)  # Check if the number should be negative (if so, make it happen)
            if isNeg:
                returnInt *= -1
            
            if returnInt >= 2**31:      # Clamp numbers outside the range to the correct values
                returnInt = 2**31
            elif returnInt < -2**31:
                returnInt = -2**31
            
            return returnInt            # Return the number

sol = Solution()
tests = ["+123","   -4567","   ","9999999999"]
for test in tests:
    print(sol.myAtoi(test))