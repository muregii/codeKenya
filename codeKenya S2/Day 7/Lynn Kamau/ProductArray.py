#Product of Array Except Self Leetcode Challenge
#Given an array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit signed integer.

def product_except_self(nums):
    n = len(nums)

    prefix = [1] * n
    suffix = [1] * n
    answer = [1] * n

    for i in range(1, n):
        prefix[i] = prefix[i - 1] * nums[i - 1]

    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] * nums[i + 1]

    for i in range(n):
        answer[i] = prefix[i] * suffix[i]

    return answer

# Example usage
if __name__ == "__main__":  
    nums = [1, 2, 3, 4]
    result = product_except_self(nums)

    print(result)
