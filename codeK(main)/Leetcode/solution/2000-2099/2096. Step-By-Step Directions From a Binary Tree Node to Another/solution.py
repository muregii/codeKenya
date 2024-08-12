# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def getDirections(self, root, startValue, destValue):
        """
        :type root: Optional[TreeNode]
        :type startValue: int
        :type destValue: int
        :rtype: str
        """
        def findPath(root, value, path):
            if not root:
                return False
            if root.val == value:
                return True
            path.append('L')
            if findPath(root.left, value, path):
                return True
            path.pop()
            path.append('R')
            if findPath(root.right, value, path):
                return True
            path.pop()
            return False
        
        startPath = []
        destPath = []
        
        findPath(root, startValue, startPath)
        findPath(root, destValue, destPath)
        
        i = 0
        while i < len(startPath) and i < len(destPath) and startPath[i] == destPath[i]:
            i += 1
        
        return 'U' * (len(startPath) - i) + ''.join(destPath[i:])