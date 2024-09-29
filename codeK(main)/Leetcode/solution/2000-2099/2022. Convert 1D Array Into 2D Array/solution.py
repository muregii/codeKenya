class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        # Step 1: Check if the original array has enough elements to fill the 2D array
        if len(original) != m * n:
            return []  # Not possible to construct the array
        
        # Step 2: Create the 2D array by slicing the original array
        result = []
        for i in range(0, len(original), n):
            result.append(original[i:i+n])
        
        return result