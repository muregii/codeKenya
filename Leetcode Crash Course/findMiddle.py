"find the middle number in an array"
from typing import List
def find_middle(nums: List[int]) -> int:
    slow, fast = 0, 0
    mid_val = None
    
    while fast < len(nums) - 1:
        slow += 1
        fast += 2
        
        
        if fast == len(nums) and len(nums) % 2 == 0:
            mid_val = (nums[slow - 1] + nums[slow]) // 2
            print(f"we executed the if statement, mid_val is : {mid_val}")
            return mid_val
    
    # Odd length → slow ends exactly at middle
   
    return nums[slow]

test_arr1 = [1,2,3,4,5]
test_arr2 = [1, 2, 3, 4, 5, 6, 7,8]
middle = find_middle(test_arr1)
middle2 = find_middle(test_arr2)
#print((2+3)//2)
print(middle)
print(middle2)
