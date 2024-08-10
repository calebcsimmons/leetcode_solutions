# Title: Two Sum
# Submission ID: 1347225427
# Status: Accepted
# Date: August 6, 2024 at 09:44:01 PM CDT

class Solution(object):
    def twoSum(self, nums, target):
        # Initialize an empty dictionary to store the index of each number
        numIndex = {}
        
        # Iterate through the list with both index and value at that index
        for i, num in enumerate(nums):
            # Calculate the required pair value that would sum up to the target
            pair = target - num
            
            # Check if the pair value already exists in the dictionary
            if pair in numIndex:
                # If it exists, return the indices of the current number and its pair
                return [numIndex[pair], i]
            
            # If the pair value does not exist, store the index of the current number
            numIndex[num] = i