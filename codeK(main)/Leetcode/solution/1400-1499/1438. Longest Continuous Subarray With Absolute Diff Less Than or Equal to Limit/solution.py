class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        from collections import deque
        
        min_deque = deque()
        max_deque = deque()
        left = 0
        result = 0
        
        for right in range(len(nums)):
            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()
            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()
                
            min_deque.append(right)
            max_deque.append(right)
            
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                if min_deque[0] == left:
                    min_deque.popleft()
                if max_deque[0] == left:
                    max_deque.popleft()
                left += 1
            
            result = max(result, right - left + 1)
        
        return result