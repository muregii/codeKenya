#Assignment Two: Contains Duplicate LeetCode Challenge
#Given an integer array nums
#Return true if any value appears at least twice in the array
#Return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()  
        for i in range(1, len(nums)):  
            if nums[i] == nums[i - 1]:  
                return True
        return False
    
# Example usage:
if __name__ == "__main__":
    solution = Solution()
    print(solution.containsDuplicate([1, 2, 3, 1]))  
    print(solution.containsDuplicate([1, 2, 3, 4]))  
    print(solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  