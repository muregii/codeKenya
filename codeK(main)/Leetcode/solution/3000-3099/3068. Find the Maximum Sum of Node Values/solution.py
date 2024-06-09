class Solution(object):
    def maximumValueSum(self, nums, k, edges):
        # Create an adjacency list for the tree
        tree = {i: [] for i in range(len(nums))}
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        # Helper function to perform DFS and calculate the maximum value sum
        def dfs(node, parent):
            # Calculate the potential gain from XORing the node's value with k
            gain = max(nums[node], nums[node] ^ k) - nums[node]
            # Initialize the current sum as the value of the current node
            current_sum = nums[node] + gain
            # Visit all adjacent nodes
            for neighbor in tree[node]:
                if neighbor == parent:
                    continue
                # Recursively visit children
                current_sum += dfs(neighbor, node)
            # Return the sum of values for the subtree rooted at the current node
            return current_sum

        # Start DFS from node 0 (assuming 0 is always part of the tree)
        return dfs(0, -1)

# Define the variables with the given input
nums = [1, 2, 1]
k = 3
edges = [[0, 1], [0, 2]]

# Create an instance of the Solution class
solution = Solution()

# Now you can call the method and print the result
print(solution.maximumValueSum(nums, k, edges))