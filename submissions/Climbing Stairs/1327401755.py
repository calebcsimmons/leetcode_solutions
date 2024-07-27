# Title: Climbing Stairs
# Submission ID: 1327401755
# Status: Time Limit Exceeded
# Date: July 20, 2024 at 10:03:26 AM CDT

class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


