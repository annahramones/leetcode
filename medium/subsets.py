"""
78. Subsets

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]

Notes: Use backtracking algorithm. Think of possible combinations like a decision tree
       with two decisions -- can either add the current number, or dont add the current
       number. Time complexity is O(n*2^n) (the n comes from having to make the copy).
       Space complexity is technically the same, but if you dont count the space the solution
       takes, it is the height of the tree or O(n).
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        currSet, subsets = [], []
        self.createSubsets(0, nums, currSet, subsets)
        return subsets
        
    def createSubsets(self, index, nums, currSet, subsets):
        if index >= len(nums):
            subsets.append(currSet.copy())
            return 

        # where we add the current number
        currSet.append(nums[index])
        self.createSubsets(index + 1, nums, currSet, subsets)

        # where we dont add the current number
        currSet.pop()
        self.createSubsets(index + 1, nums, currSet, subsets)
        