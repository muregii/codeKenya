from typing import Optional

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        prev = None
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()

            if prev is not None and curr.val <= prev:
                return False
            prev = curr.val

            curr = curr.right
        
        return True
    
test_tree = TreeNode(2,
                    TreeNode(1),
                    TreeNode(0))

result = Solution().isValidBST(test_tree)
print(result)
