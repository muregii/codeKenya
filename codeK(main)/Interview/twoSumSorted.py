
def twoSum(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left < right:
        check = nums[left] + nums[right]
        if check == target:
           return True
    
        if sum < target:
            left+=1
        else:
            right -=1
    
    return False