"""
https://leetcode.com/problems/reorder-log-files/submissions/
"""
class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        # remove the alphabet, put it in the list
        # sort the list
        # add alphhabet list and original list 
        # return it
        
        digits = []
        letters = [] 
        for i, log in enumerate(logs):
            if log.split(" ")[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        
        letterLogsSorted = sorted(letters, key = lambda x: ' '.join(x.split()[1:]))
        return letterLogsSorted + digits
    