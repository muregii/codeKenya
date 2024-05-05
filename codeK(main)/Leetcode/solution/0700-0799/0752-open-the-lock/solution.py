from collections import deque

class Solution(object):
    def openLock(self, deadends, target):
        def neighbors(node):
            for i in range(4):
                x = int(node[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    yield node[:i] + str(y) + node[i+1:]

        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        if "0000" == target:
            return 0

        queue = deque([("0000", 0)])
        visited = set(["0000"])

        while queue:
            curr, depth = queue.popleft()
            for nbr in neighbors(curr):
                if nbr == target:
                    return depth + 1
                if nbr not in deadends and nbr not in visited:
                    visited.add(nbr)
                    queue.append((nbr, depth + 1))

        return -1