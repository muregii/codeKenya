# House Robber II Leetcode Challenges
# You are given an integer array nums where nums[i] represents the amount of money the ith house has. 
# The houses are arranged in a circle, i.e. the first house and the last house are neighbors.
# You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.
# Return the maximum amount of money you can rob without alerting the police.

def rob_circle(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    def rob_line(nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]

    return max(rob_line(nums[:-1]), rob_line(nums[1:]))

# Test Cases
print(rob_circle([2,3,2])) 
print(rob_circle([1,2,3,1]))  

# Time Complexity: O(n)
# Space Complexity: O(n)