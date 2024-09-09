# Leetcode - Combination Sum II

## Problem Description

Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the `candidate` numbers sum to the target. 

Each number in `candidates` may only be used **once** in the combination.

**Note:** The solution set must not contain duplicate combinations.

**Constraints:**
- `1 <= candidates.length <= 100`
- `1 <= candidates[i] <= 50`
- `1 <= target <= 30`

## Solution

**Understanding the Problem:**
   - The task is to find all unique combinations of numbers from `candidates` that sum to the `target`.
   - A key point here is that each number can be used **only once** in each combination.
   - We must also ensure that there are no duplicate combinations in the result.

**Breaking It Down**
   - **Backtracking Approach:**
     - Backtracking is a common technique used to explore all possible combinations of candidates.
     - Start with an empty combination and explore adding each candidate to the combination while keeping track of the current sum.
     - Once a combination matches the target, we add it to the result.
     - If the sum exceeds the target, we stop exploring further.
     
   - **Handling Duplicates:**
     - Since candidates can have duplicate values, we need to ensure that the same number is not used multiple times in different combinations.
     - To handle this, we first sort the `candidates` array and skip over duplicates during the backtracking process.

**Implementation Approach:**
   - **Sorting**: First, sort the `candidates` array to easily skip duplicates.
   - **Backtracking**: Use a recursive function to explore all combinations. The function keeps track of the current combination, the current index in `candidates`, and the remaining sum needed to reach the target.
   - **Result Collection**: Once a valid combination (one that sums to `target`) is found, it is added to the result list.

**Algorithm Steps:**
   - **Sort the Candidates:** Sorting the array helps in easily skipping duplicate numbers.
   - **Backtrack and Explore Combinations:** Recursively explore adding each candidate to the combination while ensuring that:
     - The sum doesn't exceed the target.
     - Duplicates are skipped.
   - **Add Valid Combinations:** When a combination's sum equals the target, add it to the result list.

### Python Code

```python
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
```

### Example

```python
# Input
candidates = [10,1,2,7,6,1,5]
target = 8

# Output
[
 [1,1,6],
 [1,2,5],
 [1,7],
 [2,6]
]
```

### Explanation

1. **Initial Sorting:**
   - After sorting, `candidates` becomes `[1, 1, 2, 5, 6, 7, 10]`.

2. **Backtracking:**
   - The algorithm explores each possible combination of numbers that sum up to the target `8`. 
   - Combinations like `[1,1,6]`, `[1,2,5]`, and `[2,6]` are found to match the target.

3. **Skipping Duplicates:**
   - The algorithm skips duplicate combinations such as `[1, 1, 6]` appearing twice by checking if the current element is the same as the previous one during iteration.

### Usage

To use the solution, create an instance of the `Solution` class and call the `combinationSum2` method with the `candidates` array and `target`:

```python
# Example usage
solution = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
result = solution.combinationSum2(candidates, target)
print(result)  # Output: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/40)

[Link to detailed explanation on Medium](https://medium.com/@sheefanaaz6417/40-combination-sum-ii-f418a7043b86)


### Check Out These Video(s)

[![Video Explanation](https://img.youtube.com/vi/G1fRTGRxXU8/mqdefault.jpg)](https://youtu.be/G1fRTGRxXU8)

[![Video Explanation](https://img.youtube.com/vi/rSA3t6BDDwg/mqdefault.jpg)](https://youtu.be/rSA3t6BDDwg)

[![Video Explanation](https://img.youtube.com/vi/FOyRpNUSFeA/mqdefault.jpg)](https://youtu.be/FOyRpNUSFeA)

### Complexity Analysis

- **Time Complexity:** O(2^n), where `n` is the number of elements in the `candidates` array. The number of possible subsets is exponential due to backtracking.
- **Space Complexity:** O(k * n), where `k` is the average length of combinations and `n` is the number of candidates. The space complexity includes storing the combinations.