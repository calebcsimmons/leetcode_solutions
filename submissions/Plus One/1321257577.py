# Title: Plus One
# Submission ID: 1321257577
# Status: Accepted
# Date: July 14, 2024 at 07:07:13 PM CDT

class Solution(object):
    def plusOne(self, digits):
        n = len(digits)

        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        
        return [1] + [0] * n
        