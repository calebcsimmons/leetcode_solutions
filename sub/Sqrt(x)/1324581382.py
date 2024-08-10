# Title: Sqrt(x)
# Submission ID: 1324581382
# Status: Accepted
# Date: July 17, 2024 at 04:43:08 PM CDT

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
                
        if x == 1:
            return 1

        return left