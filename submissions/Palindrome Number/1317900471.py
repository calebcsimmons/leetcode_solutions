# Title: Palindrome Number
# Submission ID: 1317900471
# Status: Accepted
# Date: July 11, 2024 at 01:24:10 PM CDT

class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        if x == x[::-1]:
            return True
        return False
