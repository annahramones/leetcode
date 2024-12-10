"""
235. Lowest Common Ancestor of a Binary Search Tree
Given a binary search tree (BST), find the lowest common ancestor (LCA) 
node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor
is defined between two nodes p and q as the lowest node in T that has both p 
and q as descendants (where we allow a node to be a descendant of itself).”

Notes: Use property of BST. There are essentially 4 cases, where p and q are greater than
current node (go right), p and q are less than current node (go left), where p and q diverge (
meaning one goes right and one goes left) so return the current node because it will be the
lowest common ancestor, and where p or q equals the current node, return the current node because
a node can be an ancestor of itself.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        curr = root

        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr
            