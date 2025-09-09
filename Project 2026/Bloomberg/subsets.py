"""Given an integer array nums of unique elements, return all possible subsets (power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []

        def backtrack(start_index: int, path: List[int]) -> None:
            result.append(path.copy())
            for i in range(start_index, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.subsets([1, 2, 3]))
