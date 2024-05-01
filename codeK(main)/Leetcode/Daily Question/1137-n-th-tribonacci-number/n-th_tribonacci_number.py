class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n <= 2:
            return 1
        
        tribonacci_sequence = [0, 1, 1]
        
        for i in range(3, n+1):
            tribonacci_sequence.append(tribonacci_sequence[i-3] + tribonacci_sequence[i-2] + tribonacci_sequence[i-1])
        
        return tribonacci_sequence[n]