class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        from collections import defaultdict

        # Create a dictionary to hold the indices of each character in the ring
        ring_dict = defaultdict(list)
        for i, ch in enumerate(ring):
            ring_dict[ch].append(i)

        # Initialize a cache for memoization
        cache = {}

        def dp(i, j):
            # If we have finished spelling the key, return 0
            if i == len(key):
                return 0

            # If the result is already in the cache, return it
            if (i, j) in cache:
                return cache[(i, j)]

            # Initialize the minimum steps to a large number
            min_steps = float('inf')

            # Iterate through all the indices of the current character in the key
            for k in ring_dict[key[i]]:
                # Calculate the distance in both directions and take the minimum
                diff = abs(j - k)
                step = min(diff, len(ring) - diff)
                # Recursively find the minimum steps for the rest of the key
                min_steps = min(min_steps, step + dp(i + 1, k))

            # Add the result to the cache
            cache[(i, j)] = min_steps + 1  # Plus one for pressing the center button
            return cache[(i, j)]

        # Start the recursion from the first character of the key and the '12:00' position of the ring
        return dp(0, 0)

# Example usage:
# sol = Solution()
# print(sol.findRotateSteps("god", "dog"))  # Replace "god" with the ring and "dog" with the key