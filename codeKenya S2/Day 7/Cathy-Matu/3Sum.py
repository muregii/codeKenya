#Two pointer approach
#Using O(N^2) time complexity and O(1) space complexity

class Solution:
    def threeSum(self, nums):
        nums.sort()  # In-place sort
        n = len(nums)
        result = []

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate `i`

            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for left and right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result
# Example usage:
print(Solution().threeSum([-1, 0, 1, 2, -1, -4])) 