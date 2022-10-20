# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Standard import
from ctypes.wintypes import LPWIN32_FIND_DATAA
from typing import Optional

from numpy import true_divide

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Defining a function to return something human-legible
# for the entire linked list, from only the head
    def getAll(self):
        valList = []
        currentNode = self
        while currentNode.next != None:
            valList.append(currentNode.val)
            currentNode = currentNode.next
        valList.append(currentNode.val)
        return(valList)


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        list2 = []

        checker = l1                    # Iterate over the linked lists and
        while checker.next != None:     # gather vals into unlinked lists so
            list1.append(checker.val)   # they are easier to work with
            checker = checker.next
        list1.append(checker.val)

        checker = l2
        while checker.next != None:
            list2.append(checker.val)
            checker = checker.next
        list2.append(checker.val)

        if len(list1) < len(list2):     # Force list1 to be the longest
            list3 = list1
            list1 = list2
            list2 = list3
            list3 = []
        else:
            list3 = []
                                                # (Like column addition)
        print(len(list1),len(list2))
        carryOne = False                        # Add the values together from 1s -> 10s -> 100s -> etc. 
        for i in range(len(list1)):
            if i < len(list2):
                if carryOne:
                    if (list1[i]+list2[i]+1) >= 10:             # Throughout: check for val1+val2 >= 10...
                        remainder = (list1[i]+list2[i]) % 10    # this means we need to carryOne to the next addition
                        list3.append(remainder)                 # In all cases, add the new value to list3
                        carryOne = True
                    else:
                        list3.append(list1[i]+list2[i]+1)
                        carryOne = False
                else:
                    if (list1[i]+list2[i]) >= 10:
                        remainder = (list1[i]+list2[i]) % 10
                        list3.append(remainder)
                        carryOne = True
                    else:
                        list3.append(list1[i]+list2[i])
                        carryOne = False
            elif carryOne:
                list3.append(list1[i]+1)        # If there is no equivalent value in the shorter list
                carryOne = False                # then there is no addition to do and we can
            else:                               # just append the value from list1
                list3.append(list1[i])
                carryOne = False
        if carryOne:
            list3.append(1)                     # Once we have finished iterating, there is a chance that
                                                # we still need to carryOne. So, add a 1 at the end of list3

        list3[-1] = ListNode(list3[-1])                     # Change the last value in list3 into a ListNode with next = None
        for i in range(2,len(list3)+1):                     # Working backwards, turn list3[k] into a ListNode with next = list3[k+1]
            list3[-i] = ListNode(list3[-i],list3[-i+1])
        
        return list3[0]         # Return the head of the linked list        

# From here on is code used for debugging
LN13 = ListNode(3)
LN12 = ListNode(4,LN13)
LN11 = ListNode(2,LN12)

LN24 = ListNode(1)
LN23 = ListNode(8,LN24)
LN22 = ListNode(0,LN23)
LN21 = ListNode(7,LN22)

sol = Solution()
print((sol.addTwoNumbers(LN11,LN21)).getAll())