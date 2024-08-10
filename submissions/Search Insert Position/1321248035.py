# Title: Search Insert Position
# Submission ID: 1321248035
# Status: Accepted
# Date: July 14, 2024 at 06:43:01 PM CDT

class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                right = mid - 1
            
            elif nums[mid] < target:
                left = mid + 1
        
        return left
        