# Leetcode - Number of Valid Teams

## Problem Description

There are `n` soldiers standing in a line. Each soldier is assigned a **unique** `rating` value.

You have to form a team of 3 soldiers amongst them under the following rules:

- Choose 3 soldiers with index `(i, j, k)` with rating `(rating[i], rating[j], rating[k])`.
- A team is valid if: `(rating[i] < rating[j] < rating[k])` or `(rating[i] > rating[j] > rating[k])` where `(0 <= i < j < k < n)`.

Return the number of teams you can form given the conditions. (Soldiers can be part of multiple teams).

**Constraints:**
- `n == rating.length`
- `3 <= n <= 1000`
- `1 <= rating[i] <= 10^5`
- All the integers in `rating` are **unique**.

## Solution

**Understanding the Problem:**
   - We have `n` soldiers, each with a unique rating.
   - Our goal is to count the number of valid teams of 3 soldiers that can be formed. A team is valid if the ratings of the soldiers are either in strictly increasing or strictly decreasing order.

**Breaking It Down**
   - **Team Formation:**
     We need to select 3 soldiers `(i, j, k)` such that the ratings satisfy one of two conditions:
     1. `rating[i] < rating[j] < rating[k]`
     2. `rating[i] > rating[j] > rating[k]`
     
   - **Counting Valid Teams:**
     - For each soldier `j` (the middle soldier in the team), we need to count how many soldiers `i` before `j` have a rating either less than or greater than `rating[j]`.
     - Similarly, for each soldier `j`, count how many soldiers `k` after `j` have a rating either greater than or less than `rating[j]`.
     - The total number of valid teams for each `j` is the product of these counts for both conditions.

**Implementation Approach:**
   - Iterate over each soldier `j` in the list as the middle soldier.
   - For each `j`, calculate the number of valid soldiers `i` before `j` and `k` after `j` that can form a valid team.
   - Sum the valid teams for all `j`.

**Algorithm Steps:**
   - **Iterate Over All Soldiers:** Treat each soldier as the middle soldier `j` in potential teams.
   - **Count Valid Soldiers Before and After `j`:** For each soldier `j`, count how many soldiers `i` before `j` and how many soldiers `k` after `j` can form a valid team.
   - **Calculate Total Teams:** Sum the number of valid teams that can be formed for all `j`.

### Python Code

```python
class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
       
```

### Example

```python
# Input
rating = [2,5,3,4,1]

# Output
3
```

### Explanation
1. **Valid Teams:** The valid teams are `(2,3,4)`, `(5,4,1)`, and `(5,3,1)`.
2. **Counting:** The solution iterates through each soldier and calculates how many valid teams can be formed by considering that soldier as the middle one.

### Usage

To use the solution, create an instance of the `Solution` class and call the `numTeams` method with the `rating` array:

```python
# Example usage
solution = Solution()
rating = [2,5,3,4,1]
result = solution.numTeams(rating)
print(result)  # Output: 3
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/1395)

### Check Out These Video(s)

[![Video Explanation](https://img.youtube.com/vi/YfMfNKVOGH0/mqdefault.jpg)](https://youtu.be/YfMfNKVOGH0)

[![Video Explanation](https://img.youtube.com/vi/zONHzIqCr-o/mqdefault.jpg)](https://youtu.be/zONHzIqCr-o)

### Complexity Analysis

- **Time Complexity:** O(n^2), where `n` is the number of soldiers. The nested loops are needed to count valid teams.
- **Space Complexity:** O(1), as the algorithm only uses a few variables for counting.