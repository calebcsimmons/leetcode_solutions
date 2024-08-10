# Title: Length of Last Word
# Submission ID: 1317021722
# Status: Accepted
# Date: July 10, 2024 at 09:08:14 PM CDT

class Solution(object):
    def lengthOfLastWord(self, string):

        words = string.split() # Auto splits string into list of words and removes trailing spaces
        if not words: # If words list is empty
            return 0
        return len(words[-1])
        