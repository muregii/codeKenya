class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        
        # Greedy factorization approach
        result = 0
        divisor = 2
        
        while n > 1:
            while n % divisor == 0:
                result += divisor
                n //= divisor
            divisor += 1
            
        return result