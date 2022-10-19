# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pCursor = 0                     # Iterator for p
        i = 0                           # Iterator for s
        while i < len(s):
            if pCursor > len(p):        # If pCursor out of range,
                return False            # return False...

            if (pCursor + 1) < len(p):
                if p[pCursor + 1] == "*":   # If "*"" is next, keep checking
                    if p[pCursor] == s[i]:  # for either s[i] or "." until
                        i += 1              # False... then move the pCursor
                    elif p[pCursor] == ".": # past the "*" to check for the 
                        i += 1              # next part of the pattern
                    else:
                        pCursor += 2

                elif p[pCursor] == ".":     # Check against the pattern for
                    pCursor += 1            # either "." or s[i].
                    i += 1
            
                elif p[pCursor] == s[i]:
                    pCursor += 1
                    i += 1
            
                else:                       # If the pattern doesn't match
                    return False            # return False

            elif p[pCursor] == ".":     # 
                pCursor += 1            #
                i += 1                  #
                                        # Checking again
            elif p[pCursor] == s[i]:    # (but only for the last value in p)
                pCursor += 1            # (i.e. pCursor+1 >= len(p))
                i += 1                  #
            
            else:                       # If the pattern doesn't match
                return False            # return False

        return True


sol = Solution()
tests = ["aaabcdeef","a*bcdee.","aaaaaa",".*","abbabb","a.b..c"]
for i in range(int(len(tests)/2)):
    print(sol.isMatch(tests[2*i],tests[2*i+1]))

# It is worth noting that any pattern, p, containing ".*" at any point
# it will always return True (despite any following characters)
# provided the pattern matches up to that point.