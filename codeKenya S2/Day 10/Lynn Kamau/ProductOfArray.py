#Product of Array Except Self Leetcode Challenge
#Given an array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit signed integer.

#code performance optimised
def product_except_self(nums):
    n = len(nums)
    answer = [1] * n
    
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]
    
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]
    
    return answer

# Example usage
if __name__ == "__main__":  
    nums = [1, 2, 4, 6]
    result = product_except_self(nums)
    print(result) 

    nums = [-1,0,1,2,3]
    result = product_except_self(nums)
    print(result)

# Time Complexity: O(n)
# Space Complexity: O(1) (excluding the output array)

