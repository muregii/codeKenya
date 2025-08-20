#Combination Sum Leetcode Challenge
#Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target.
#You may return the combinations in any order.
#The same number may be chosen from candidates an unlimited number of times.
#Two combinations are unique if the frequency of at least one of the chosen numbers is different.

def combination_sum(candidates, target):
    res = []
    def backtrack(start, total, path):
        if total == target:
            res.append(path[:])
            return
        if total > target:
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, total + candidates[i], path)
            path.pop()
    backtrack(0, 0, [])
    return res

# Test cases
print(combination_sum([2,5,6,9], 9))
print(combination_sum([3,4,5], 16))
print(combination_sum([3], 5))

# Time Complexity: O(2^t) where t = target
# Space Complexity: O(t)
