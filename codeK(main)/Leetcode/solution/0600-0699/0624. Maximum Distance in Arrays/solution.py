class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        # Initialize min_value and max_value with the first array's min and max
        min_value = arrays[0][0]
        max_value = arrays[0][-1]
        max_distance = 0

        # Loop through the rest of the arrays
        for i in range(1, len(arrays)):
            # Calculate distance using the current array's max and min_value
            max_distance = max(max_distance, abs(arrays[i][-1] - min_value))
            # Calculate distance using the current array's min and max_value
            max_distance = max(max_distance, abs(arrays[i][0] - max_value))
            
            # Update min_value and max_value for next iteration
            min_value = min(min_value, arrays[i][0])
            max_value = max(max_value, arrays[i][-1])

        return max_distance