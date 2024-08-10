# Title: Roman to Integer
# Submission ID: 1317929562
# Status: Accepted
# Date: July 11, 2024 at 01:53:06 PM CDT

class Solution(object):
    def romanToInt(self, romNum):
        romInt = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000} 
        intNum = 0
        prevNum = romInt[romNum[0]]

        for char in romNum:
            if romInt[char] > prevNum:
                intNum += romInt[char] - 2*prevNum
            else:
                intNum += romInt[char]

            prevNum = romInt[char]
        return intNum