class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        total_satisfied = 0
        additional_satisfied = 0
        max_additional_satisfied = 0
        
        for i in range(len(customers)):
            if grumpy[i] == 0:
                total_satisfied += customers[i]
        
        for i in range(len(customers)):
            if grumpy[i] == 1:
                additional_satisfied += customers[i]
            if i >= minutes and grumpy[i - minutes] == 1:
                additional_satisfied -= customers[i - minutes]
            max_additional_satisfied = max(max_additional_satisfied, additional_satisfied)
        
        return total_satisfied + max_additional_satisfied