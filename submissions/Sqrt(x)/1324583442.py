# Title: Sqrt(x)
# Submission ID: 1324583442
# Status: Accepted
# Date: July 17, 2024 at 04:47:14 PM CDT

class Solution(object):
    def mySqrt(self,x):
        left = 0
        right = x

        while left <= right:
            mid = (right + left) // 2
            square = mid * mid

            if square > x:
                right = mid - 1
            
            elif square < x:
                left = mid + 1

            else:
                return mid

        return right