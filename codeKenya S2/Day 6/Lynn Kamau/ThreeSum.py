# Threesum Leetcode Challenge
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.


def three_sum(nums):
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = n - 1
        target = -nums[i]

        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return result


# Test cases
print(three_sum([-1, 0, 1, 2, -1, -4]))
print(three_sum([0, 0, 0]))
print(three_sum([0, 1, 1]))
print(three_sum([-2, 0, 1, 1, 2]))
print(three_sum([]))