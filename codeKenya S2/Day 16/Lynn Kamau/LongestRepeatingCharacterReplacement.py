def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0
    for num in nums:
        if num - 1 not in num_set:
            length = 0
            while num + length in num_set:
                length += 1
            longest = max(longest, length)
    return longest

# usage
print(longest_consecutive([100,4,200,1,3,2]))  # Output: 4

# Time Complexity: O(n)
# Space Complexity: O(n)
