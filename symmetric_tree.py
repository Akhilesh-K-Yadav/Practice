# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/627/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        else:
            self.check(root.left, root.right)

    def check(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val == right.val:
            out_pair = self.check(left.left, right.right)
            in_pair = self.check(left.right, right.left)
            return out_pair and in_pair
        else:
            return False
