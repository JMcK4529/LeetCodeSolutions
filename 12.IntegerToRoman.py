# Given an integer (1 <= num <= 3999), convert it to a roman numeral.

class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""              # An emptry string in which to store the roman number

        while num > 0:          # While there is a part of the number left...
            if num >= 1000:     # Look for the highest roman symbol left in num,
                roman += "M"    # add it to the string and then take that amount from num...
                num -= 1000     # leaving only the remainder

            elif num >= 900:    # Every possible "symbol" must be considered,
                                # including combinations (e.g. XC):
                roman += "CM"   # M, CM, D, CD, C, XC, L, XL, X, IX, V, IV and I
                num -= 900

            elif num >= 500:
                roman += "D"
                num -= 500

            elif num >= 400:
                roman += "CD"
                num -= 400

            elif num >= 100:
                roman += "C"
                num -= 100

            elif num >= 90:
                roman += "XC"
                num -= 90

            elif num >= 50:
                roman += "L"
                num -= 50

            elif num >= 40:
                roman += "XL"
                num -= 40

            elif num >= 10:
                roman += "X"
                num -= 10

            elif num >= 9:
                roman += "IX"
                num -= 9

            elif num >= 5:
                roman += "V"
                num -= 5

            elif num >= 4:
                roman += "IV"
                num -= 4

            elif num >= 1:
                roman += "I"
                num -= 1

        return roman

sol = Solution()
tests = [3,58,1994]
for test in tests:
    print(sol.intToRoman(test))