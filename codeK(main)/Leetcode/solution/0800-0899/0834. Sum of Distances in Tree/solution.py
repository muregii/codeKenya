class Solution(object):
    def sumOfDistancesInTree(self, n, edges):
        # Create an adjacency list for the tree
        tree = [[] for _ in range(n)]
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)

        # Arrays to store the count of nodes in the subtree rooted at each node
        # and the sum of distances from each node to nodes in its subtree
        count = [1] * n
        answer = [0] * n

        # Post-order DFS to populate count and answer arrays
        def post_order(node, parent):
            for child in tree[node]:
                if child != parent:
                    post_order(child, node)
                    count[node] += count[child]
                    answer[node] += answer[child] + count[child]

        # Pre-order DFS to adjust answer array using the count array
        def pre_order(node, parent):
            for child in tree[node]:
                if child != parent:
                    answer[child] = answer[node] - count[child] + n - count[child]
                    pre_order(child, node)

        # Start the DFS from node 0
        post_order(0, -1)
        pre_order(0, -1)

        return answer