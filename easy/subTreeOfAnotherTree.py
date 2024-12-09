"""
572. Subtree of Another Tree

Given the roots of two binary trees root and subRoot, 
return true if there is a subtree of root with the same 
structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that 
consists of a node in tree and all of this node's descendants. 
The tree tree could also be considered as a subtree of itself.

Notes: Can use solution to LC problem "Same Tree". Basically, we are
       checking every part of main tree and seeing if a subtree of the main 
       tree is equal to the subtree passed in. The time complexity of checking
       if the subtrees are the same tree is O(m) where m is the number of nodes
       in the subtree. Now lets say a subtree and THE subtree is not the same 
       tree, now we have to pass in another node as the root (basically a 
       new subtree from the main tree), and check if that subtree and THE 
       subtree are equal. The time complexity is O(n*m) where n is 
       the number of nodes in the main tree. We can use recursion for the
       isSubtree problem too.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.sameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


        
    def sameTree(self, node, subNode):
        if not node and not subNode:
            return True
        
        if node and subNode and node.val == subNode.val:
            return self.sameTree(node.left, subNode.left) and self.sameTree(node.right, subNode.right)
        
        return False
            