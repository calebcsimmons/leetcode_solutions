# Title: Sqrt(x)
# Submission ID: 1324579724
# Status: Wrong Answer
# Date: July 17, 2024 at 04:39:42 PM CDT

class Solution(object):
    def mySqrt(self, x):
        left = 0
        right = x

        while right - left > 1:
            mid = (right + left) // 2
            square = mid * mid

            if square > x:
                right = mid
            
            elif square < x:
                left = mid 

            elif square == x:
                return mid

        return left