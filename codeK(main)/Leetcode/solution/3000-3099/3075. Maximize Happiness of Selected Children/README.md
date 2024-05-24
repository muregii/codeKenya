# Leetcode - Maximum Happiness Sum

## Problem Description

You are given an array `happiness` of length `n`, and a **positive** integer `k`.

There are `n` children standing in a queue, where the `ith` child has a **happiness value** `happiness[i]`. You want to select `k` children from these `n` children in `k` turns.

In each turn, when you select a child, the **happiness value** of all the children that have not been selected till now decreases by `1`. Note that the happiness value cannot become negative and gets decremented only if it is positive.

*Return the **maximum** sum of the happiness values of the selected children you can achieve by selecting `k` children.*

**Constraints:**

- `1 <= n == happiness.length <= 2 * 105`
- `1 <= happiness[i] <= 108`
- `1 <= k <= n`

## Solution

To solve this problem, we need to maximize the sum of happiness values by selecting children in an optimal order. Here's a step-by-step approach to achieve this:

1. **Sort the Happiness Values**: Sort the `happiness` array in descending order. This way, we prioritize selecting children with higher happiness values first.
2. **Initialize Variables**: Keep track of the total sum of selected happiness values.
3. **Select Children**: Select the first `k` children from the sorted list. For each selected child, add their happiness value to the total sum.
4. **Adjust Remaining Values**: As we select each child, decrease the happiness values of the remaining children by `1`, ensuring that no happiness value becomes negative.
5. **Return the Result**: The total sum after selecting `k` children is the maximum sum of happiness values.

By selecting children with the highest happiness values first and adjusting the remaining values, we can ensure that we achieve the maximum possible sum of happiness values.

## Usage

To use the solution, create an instance of the `Solution` class and call the `maximumHappinessSum` method with the input parameters `happiness` and `k`:

```python
class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
# Example Usage
solution = Solution()
happiness = [1, 2, 3, 4, 5]
k = 3
result = solution.maximumHappinessSum(happiness, k)
print(result)  # Output: 12 (5 + 4 + 3)
```

## Explanation

1. **Input**: The array `happiness` and integer `k` are given.
2. **Sorting**: We sort the happiness values in descending order to prioritize higher values.
3. **Selection**: We select the first `k` children from the sorted list and sum their happiness values.
4. **Result**: The total sum of selected happiness values is returned.

[Link to detailed explanation on FreeCodeCamp](https://www.freecodecamp.org/news/greedy-algorithms/)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/activity-selection-problem-greedy-algo-1/)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/maximize-the-happiness-of-the-groups-on-the-trip/)

## Check Out these videos

[![Video Explanation](https://img.youtube.com/vi/nDe67PStfys/mqdefault.jpg)](https://youtu.be/nDe67PStfys)


## Complexity Analysis

- **Time Complexity:** O(n log n), where n is the number of children. Sorting the happiness values takes O(n log n) time.
- **Space Complexity:** O(1). We use only constant extra space for variables.