# Title: Palindrome Number
# Submission ID: 1336473410
# Status: Accepted
# Date: July 28, 2024 at 12:20:57 PM CDT

class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        if x == x[::-1]:
            return True
        return False
