# Given a roman numeral (1 <= roman.length <= 15, 1 <= num <= 3999), convert it to an integer.

class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0                                     # The number to eventually be returned
        
        # Make a dictionary of Roman numeral values
        romanDict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

        highestSeen = "I"                           # Keep a record of the highest value numeral seen
        for i in range(1,len(s)+1):                 # Check the string backwards
            charVal = romanDict[s[-i]]              
            if charVal >= romanDict[highestSeen]:   # If the numeral has a higher value than highestSeen,
                num += charVal                      # add this to num and then replace the 
                highestSeen = s[-i]                 # highestSeen numeral
            else:
                num -= charVal                      # If the numeral is lower than highestSeen,
                                                    # it should be taken away (i.e. the "C" in "CM")
        return num                                  # Return the integer num.

sol = Solution()
tests = ["III", "LVIII", "MCMXCIV"]
for test in tests:
    print(sol.romanToInt(test))