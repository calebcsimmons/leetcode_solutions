# Title: Plus One
# Submission ID: 1321254079
# Status: Accepted
# Date: July 14, 2024 at 06:58:18 PM CDT

class Solution(object):
    def plusOne(self, digits):
        value = ""
        newnum = []

        for i in digits:
            value += str(i)
        
        val_1 = str(int(value) + 1)
        
        for i in val_1:
            newnum.append(int(i))
        
        return newnum
        