class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k == len(num):
            return "0"

        stack = []
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        # If k is still greater than 0, remove the last k digits from the stack
        result = "".join(stack[:-k] if k else stack).lstrip("0")
        return result if result else "0"