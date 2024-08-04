# Leetcode - Find the Winner of the Circular Game

## Problem Description

There are `n` friends that are playing a game. The friends are sitting in a circle and are numbered from `1` to `n` in **clockwise order**. More formally, moving clockwise from the `ith` friend brings you to the `(i+1)`th friend for `1 <= i < n`, and moving clockwise from the `n`th friend brings you to the 1st friend.

The rules of the game are as follows:
- **Start** at the `1st` friend.
- Count the next `k` friends in the clockwise direction **including** the friend you started at. The counting wraps around the circle and may count some friends more than once.
- The last friend you counted leaves the circle and loses the game.
- If there is still more than one friend in the circle, go back to step `2` **starting** from the friend **immediately clockwise** of the friend who just lost and repeat.
- Else, the last friend in the circle wins the game.

Given the number of friends, `n`, and an integer `k`, return *the winner of the game*.

**Constraints:**
- `1 <= k <= n <= 500`

## Solution

To determine the winner of the game, we can use a simulation approach or a mathematical approach based on the Josephus problem.

1. **Understanding the Problem:**
   - Friends are eliminated in a circular manner every `k` counts.
   - The process continues until only one friend remains.

2. **Simulating the Process:**
   - Use a list to represent the friends.
   - Iterate through the list, removing the friend at each `k`th position.
   - Continue until only one friend is left.

3. **Algorithm Steps:**
   - Initialize a list of friends numbered from 1 to `n`.
   - Use a pointer to track the current position.
   - Remove the friend at the `k`th position repeatedly until one friend remains.
   - Return the last remaining friend as the winner.

### Example

Suppose you have `n = 5` friends and `k = 2`:

- Initial friends: [1, 2, 3, 4, 5]
- Start at friend 1 and count 2 friends: friend 2 is removed.
- Remaining friends: [1, 3, 4, 5]
- Start at friend 3 and count 2 friends: friend 4 is removed.
- Remaining friends: [1, 3, 5]
- Start at friend 5 and count 2 friends: friend 1 is removed.
- Remaining friends: [3, 5]
- Start at friend 3 and count 2 friends: friend 3 is removed.
- Remaining friend: [5]

The winner is friend 5.

### Python Code

```python
class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        
```

### Usage

To use the solution, create an instance of the `Solution` class and call the `findTheWinner` method with the number of friends and the step count:

```python
# Example usage
solution = Solution()
n = 5
k = 2
result = solution.findTheWinner(n, k)
print(result)  # Output: 3
```

### Additional Resources

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/find-winner-of-the-game-where-array-elements-are-reduced-in-each-turn/)

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/1823)

### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/PBBQgW_75e0/mqdefault.jpg)](https://youtu.be/PBBQgW_75e0)

[![Video Explanation](https://img.youtube.com/vi/8uFWG6xfkuc/mqdefault.jpg)](https://youtu.be/8uFWG6xfkuc)

[![Video Explanation](https://img.youtube.com/vi/V5CyomTb-94/mqdefault.jpg)](https://youtu.be/V5CyomTb-94)


### Complexity Analysis

- **Time Complexity:** O(n^2), due to the repeated removal of elements from the list.
- **Space Complexity:** O(n), for storing the list of friends.