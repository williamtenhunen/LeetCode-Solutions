# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(node, res):
            if not node:
                return
            helper(node.left, res)
            res.append(node.val)
            helper(node.right, res)
        
        result = []
        helper(root, result)
        return result