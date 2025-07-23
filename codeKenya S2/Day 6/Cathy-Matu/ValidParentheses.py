class Solution(object):
    def isValid(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        # UMPIRE
        # U - Understand the problem
        # M - Match with a data structure (stack)
        # P - Plan
        # I - Implement
        # R - Review
        # E - Evaluate with test cases

        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping.values(): 
                stack.append(char)
            elif char in mapping:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                return False 

        return not stack

# Test outside the class
s = "([{}])"
print(Solution().isValid(s))
