# Title: Palindrome Number
# Submission ID: 1347082967
# Status: Accepted
# Date: August 6, 2024 at 04:44:17 PM CDT

class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        if x == x[::-1]:
            return True
        return False
