# Title: Search Insert Position
# Submission ID: 1321233503
# Status: Accepted
# Date: July 14, 2024 at 06:05:10 PM CDT

class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1

        while right >= left:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                left = mid + 1
            
            elif nums[mid] > target:
                right = mid - 1
        
        return left
        