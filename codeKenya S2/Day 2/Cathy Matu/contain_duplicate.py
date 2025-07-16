# The code below checks if a list, nums, contains any duplicates.
# A class named Solution has a method containsDuplicate defined, 
# which takes a list of integers as input and returns if the list has duplicates or not using bool.

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


user_input = input("Enter numbers separated by commas (e.g., 2,3,4,5,5): ")


nums = list(map(int, user_input.split(",")))

sol = Solution()
result = sol.containsDuplicate(nums)

print("Contains Duplicate:", result)
