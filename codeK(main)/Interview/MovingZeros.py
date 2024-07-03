class MovingZeros:
    def moving_zeros(self, nums):
     #[0, 1, 0, 2, 3, 4] -> [1, 2, 3, 4, 0, 0]
     #Two Pointers
        right = 0
        for left in range(len(nums)):
            if(nums[left] != 0):
             nums[right] = nums[left]
             right +=1
        for left in range(len(nums)):
            nums[left] = 0
        
        return nums
    
    
             
    

