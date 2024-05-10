class Solution(object):
    def minOperations(self, nums, k):
        # Calculate the current XOR of all elements in the array
        current_xor = 0
        for num in nums:
            current_xor ^= num
        
        # Find the XOR of the current XOR with k
        xor_with_k = current_xor ^ k
        
        # Count the number of set bits in the XOR result
        # Each set bit represents a bit flip
        operations = bin(xor_with_k).count('1')
        
        # Return the minimum operations required
        return operations

# Example usage:
# sol = Solution()
# print(sol.minOperations([2, 1, 3, 4], 1))  # Output should be 2