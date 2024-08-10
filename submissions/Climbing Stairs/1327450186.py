# Title: Climbing Stairs
# Submission ID: 1327450186
# Status: Time Limit Exceeded
# Date: July 20, 2024 at 10:28:53 AM CDT

class Solution(object):
    def climbStairs(self, n, dic = None):
        # Recursive Function: f(n) = f(n-1) + f(n-2)
        
        if dic is None:
            dic = {}

        if n in dic:
            return dic[n]

        if n <= 2:
            return n
        
        dic[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return dic[n]

        # Memoization
        # (Create dictionary to store values already calculated for recall later.
        # This improves the Time Complexity from O(2^n) to O(n)