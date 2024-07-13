class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        position.sort()
        
        def canPlaceBalls(min_force):
            count = 1
            last_position = position[0]
            for i in range(1, len(position)):
                if position[i] - last_position >= min_force:
                    count += 1
                    last_position = position[i]
                    if count >= m:
                        return True
            return False
        
        left, right = 1, position[-1] - position[0]
        while left < right:
            mid = (left + right + 1) // 2
            if canPlaceBalls(mid):
                left = mid
            else:
                right = mid - 1
        
        return left