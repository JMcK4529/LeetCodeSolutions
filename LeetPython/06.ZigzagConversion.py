# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
# string convert(string s, int numRows);

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Make an array with the right number of rows and columns for the zigzag
        x = len(s) # string length
        # Some maths to find the necesary number of columns
        y = x % (2*numRows - 2)
        z = x - y
        n = z / (numRows - 1)
        if x > z:
            numCols = int(n + 2*numRows - 2)
        else:
            numCols = int(n)
        
        # Creating an empty array with the right number of rows and columns (array[numCols][numRows])
        array = [None] * numCols
        for i in range(len(array)):
            array[i] = [None] * numRows
        
        # An iterable for progressing through the string
        charIndex = 0

        # Work out whether the column should be fully populated or just one value (and which value!)
        for i in range(numCols):
            # if m == 0, the column should be fully populated, otherwise it is part of the zigzag
            m = i % (numRows - 1)
            if m != 0:
                if charIndex < x:
                    array[i][numRows - m - 1] = s[charIndex]
                    charIndex += 1
            else:
                for j in range(numRows):
                    if charIndex < x:
                        array[i][j] = s[charIndex]
                        charIndex += 1

        # Reading the string back out of the array in the new order by swapping i,j (therefore working in the transpose)
        returnString = ""
        for i in range(numRows):
            for j in range(numCols):
                if array[j][i] != None:
                    returnString += array[j][i]

        return returnString

sol = Solution()
print(sol.convert("paypalishiring",4))