class Solution(object):
    def minKBitFlips(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        flips = 0
        flip_queue = collections.deque()
        
        for i in range(len(nums)):
            # Remove elements from the queue that are outside the current window
            if flip_queue and flip_queue[0] == i:
                flip_queue.popleft()
            
            # Determine if a flip is needed
            if (len(flip_queue) % 2 == nums[i]):
                if i + k > len(nums):
                    return -1
                flip_queue.append(i + k)
                flips += 1
        
        return flips