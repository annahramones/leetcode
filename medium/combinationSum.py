"""
39. Combination Sum

Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers 
sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up 
to target is less than 150 combinations for the given input.

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []

Notes: Backtracking algorithm. Tricky part is not having duplicates (but not accounting for
       duplicates actually makes it efficient). To not include duplicates, think of a decision
       tree where you have 2 decisions. You can either add the current element to the list, 
       or not. The current element is incremented on the next call of the recursive function.
       It's helpful to draw it out.
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if target == 1:
            return []
        curr, result = [], []
        self.findCombos(0, candidates, curr, result, target, 0)
        return result
        
    def findCombos(self, index, candidates, curr, result, target, total):
        if total == target:
            result.append(curr.copy())
            return
        if index >= len(candidates) or total > target:
            return
        
        curr.append(candidates[index])
        total += candidates[index]
        self.findCombos(index, candidates, curr, result, target, total)

        curr.pop()
        total -= candidates[index]
        self.findCombos(index+1, candidates, curr, result, target, total)