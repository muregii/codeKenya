class Solution:
    def iterate(self, nums):
        left, right = 0, len(nums)-1
        while left <= right:
            print(nums[left])
            left+=1
            print (nums[right])
            right-=1
        return nums

Solution().iterate([1, 2, 3, 4, 5])
