class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        # Sort the happiness array in descending order
        happiness.sort(reverse=True)
        
        # Initialize the sum of happiness to 0
        happiness_sum = 0
        
        # Loop over the first k elements of the sorted array
        for i in range(k):
            # Add the current happiness value to the sum
            happiness_sum += happiness[i]
            # Decrement the happiness of the remaining children
            for j in range(i+1, len(happiness)):
                if happiness[j] > 0:
                    happiness[j] -= 1
        
        return happiness_sum