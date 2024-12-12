"""
74. Search a 2D Matrix

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Notes: First search for the correct row using binary search, then search for 
       the actual value using binary search. The only tricky part is when
       calculating the mid value use (end-start)//2 + start. This will help
       us get the first and last rows/cols. 
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # row search
        row_start = 0
        row_end = len(matrix) - 1
        row = -1 

        while row_start <= row_end:
            curr_row = ((row_end - row_start)//2) + row_start
            if target < matrix[curr_row][0]:
                row_end = curr_row - 1
            elif target > matrix[curr_row][len(matrix[0]) -1]:
                row_start = curr_row + 1
            else:
                row = matrix[curr_row]
                break
        if row == -1:
            return False
        
        # search row
        start = 0
        end = len(row)

        while start <= end:
            curr = ((end - start)//2) + start
            if target < row[curr]:
                end = curr - 1
            elif target > row[curr]:
                start = curr + 1
            else:
                return True
        
        return False