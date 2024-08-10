# Title: Find the Index of the First Occurrence in a String
# Submission ID: 1321218603
# Status: Accepted
# Date: July 14, 2024 at 05:28:13 PM CDT

class Solution(object):
    def strStr(self, haystack, needle):
        if needle not in haystack:
            return -1

        return haystack.index(needle)
        