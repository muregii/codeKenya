# Leetcode - Relative Ranks

## Problem Description

You are given an integer array `score` of size `n`, where `score[i]` is the score of the `ith` athlete in a competition. All the scores are guaranteed to be **unique**.

The athletes are **placed** based on their scores, where the `1st` place athlete has the highest score, the `2nd` place athlete has the `2nd` highest score, and so on. The placement of each athlete determines their rank:

- The `1st` place athlete's rank is `"Gold Medal"`.
- The `2nd` place athlete's rank is `"Silver Medal"`.
- The `3rd` place athlete's rank is `"Bronze Medal"`.
- For the `4th` place to the nth place athlete, their rank is their placement number (i.e., the `xth` place athlete's rank is `"x"`).

Return an array `answer` of size `n` where `answer[i]` is the **rank** of the `ith` athlete.

**Constraints:**

 - `n == score.length`
- `1 <= n <= 104`
- `0 <= score[i] <= 106`
- All the values in `score` are **unique**.

## Solution

To solve this problem, we need to sort the scores and assign ranks based on their sorted positions. Here's a step-by-step approach to achieve this:

1. Create a list of tuples where each tuple contains the score and its corresponding index in the original array.
2. Sort this list of tuples based on the scores in descending order.
3. Traverse the sorted list and assign ranks based on the position in the sorted list:
   - The first element gets the "Gold Medal".
   - The second element gets the "Silver Medal".
   - The third element gets the "Bronze Medal".
   - All subsequent elements get their respective position numbers.
4. Construct the `answer` array using the ranks assigned in the previous step.

## Usage

To use the solution, create an instance of the `Solution` class and call the `findRelativeRanks` method with the input parameter `score`:

```python
class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """

# Example Usage
solution = Solution()
score = [10, 3, 8, 9, 4]
result = solution.findRelativeRanks(score)
print(result)  # Output: ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]
```

## Explanation

1. **Input**: The array `score` is given.
2. **Tuple Creation**: We create a list of tuples with each score and its index.
3. **Sorting**: We sort the list of tuples in descending order based on the scores.
4. **Rank Assignment**: We assign ranks to the athletes based on their positions in the sorted list.
5. **Output**: We construct the `answer` array with the assigned ranks and return it.

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/find-relative-rank-of-each-element-in-array/)


[Link to detailed explanation on Medium](https://medium.com/@somyagupta566/introduction-to-hashmap-data-structures-and-algorithm-7fac8ebefb90)


[Link to detailed explanation](https://afteracademy.com/blog/comparison-of-sorting-algorithms/)

[Link to detailed explanation on Medium](https://medium.com/@nikhilbd/intuitive-explanation-of-learning-to-rank-and-ranknet-lambdarank-and-lambdamart-fe1e17fac418)


## Check Out these videos

[![Video Explanation](https://img.youtube.com/vi/EcPtgVdK2R8/mqdefault.jpg)](https://youtu.be/EcPtgVdK2R8)


[![Video Explanation](https://img.youtube.com/vi/DISbLNx65qI/mqdefault.jpg)](https://youtu.be/DISbLNx65qI)



## Complexity Analysis

- **Time Complexity:** O(n log n), where n is the number of athletes. Sorting the scores takes O(n log n) time.
- **Space Complexity:** O(n). We use additional space to store the list of tuples and the `answer` array.