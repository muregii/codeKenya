class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def heapify(nums, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            
            if left < n and nums[left] > nums[largest]:
                largest = left
                
            if right < n and nums[right] > nums[largest]:
                largest = right
                
            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                heapify(nums, n, largest)
        
        n = len(nums)
        
        # Build a maxheap
        for i in range(n // 2 - 1, -1, -1):
            heapify(nums, n, i)
        
        # Extract elements from heap one by one
        for i in range(n-1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]  # Swap
            heapify(nums, i, 0)
        
        return nums