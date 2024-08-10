# Title: Excel Sheet Column Title
# Submission ID: 1336364267
# Status: Accepted
# Date: July 28, 2024 at 10:24:09 AM CDT

class Solution(object):
    def convertToTitle(self, columnNumber):
        if columnNumber == 0:
            return ""
        columnNumber -=1
        
        return self.convertToTitle(columnNumber// 26) + chr(columnNumber % 26 + 65)
        