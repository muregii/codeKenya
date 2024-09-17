# Leetcode - Stone Game II

## Problem Description

Alice and Bob continue their game with piles of stones. There are a number of piles **arranged in a row**, and each pile has a positive integer number of stones `piles[i]`. The objective of the game is to end with the most stones.

Alice and Bob take turns, with Alice starting first.

On each player's turn, that player can take **all the stones** from the **first** `X` remaining piles, where `1 <= X <= 2M`. Then, we set `M = max(M, X)`. Initially, M = 1.

The game continues until all the stones have been taken.

Given that Alice and Bob play optimally, *return the maximum number of stones Alice can collect*.

### Constraints:
- `1 <= piles.length <= 100`
- `1 <= piles[i] <= 10^4`

## Solution

**Understanding the Problem:**
- The goal is to maximize the number of stones Alice can collect while Bob also plays optimally.
- Each player can take `X` piles from the beginning of the remaining piles, where `1 <= X <= 2M`. After each turn, `M` is updated to the maximum of the current `M` and `X` (the number of piles taken in that turn).
- This problem can be approached using **dynamic programming** because the decisions of the players depend on the current state of the game (how many piles remain and the value of `M`).

**Breaking It Down:**
- We need to define a way to track the optimal choices for both Alice and Bob as they alternate turns. A dynamic programming (DP) approach can be used to calculate the optimal number of stones Alice can collect by considering different strategies and outcomes.
  
**Key Concepts:**
- `M`: This controls the number of piles the player can take. Each time a player takes a number of piles, `M` is updated.
- **Optimal Strategy**: Since both Alice and Bob play optimally, Alice’s goal is to maximize her stones, while Bob’s goal is to minimize Alice's gains.

**Implementation Approach:**
1. Use dynamic programming (DP) to simulate the game.
2. Define a DP table `dp[i][M]` where `i` represents the index of the current pile and `M` is the current value of `M`. This table stores the maximum number of stones Alice can collect starting from pile `i` with the current `M` value.
3. Start from the last pile and work backward, determining the best strategy for each player based on the remaining piles and value of `M`.

**Algorithm Steps:**
1. **Initialize the DP Table:** Create a DP table where each entry `dp[i][M]` holds the maximum number of stones Alice can collect starting from pile `i` with `M`.
2. **Base Case:** If `i` is the last pile, Alice can take all remaining stones.
3. **Transition:** For each pile, simulate all possible numbers of piles Alice can take and update the value of `dp[i][M]` based on the remaining piles and the updated value of `M`.
4. **Final Answer:** The value of `dp[0][1]` will hold the result for the maximum number of stones Alice can collect starting from the first pile with `M = 1`.

### Python Code

```python
class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        
```

### Example

```python
# Input
piles = [2, 7, 9, 4, 4]

# Output
10
```

### Explanation
1. Alice starts the game. She can take between 1 and `2M` piles, and `M` starts as 1.
2. By taking the optimal number of piles on each turn, Alice maximizes the number of stones she collects, while Bob tries to minimize it.
3. In this example, Alice can collect 10 stones optimally.

### Usage

To use the solution, create an instance of the `Solution` class and call the `stoneGameII` method with the `piles` array:

```python
# Example usage
solution = Solution()
piles = [2, 7, 9, 4, 4]
result = solution.stoneGameII(piles)
print(result)  # Output: 10
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/1140)

[Link to detailed explanation on Medium](https://medium.com/@_monitsharma/daily-leetcode-problems-problem-1140-stone-game-i-d5900f42239b)

### Check Out These Video(s)

[![Video Explanation](https://img.youtube.com/vi/cGjwD8jRgJc/mqdefault.jpg)](https://youtu.be/cGjwD8jRgJc)

[![Video Explanation](https://img.youtube.com/vi/I-z-u0zfQtg/mqdefault.jpg)](https://youtu.be/I-z-u0zfQtg)

[![Video Explanation](https://img.youtube.com/vi/6hu5G-abkdg/mqdefault.jpg)](https://youtu.be/6hu5G-abkdg)

### Complexity Analysis

- **Time Complexity:** O(n^2), where `n` is the number of piles. We compute the best strategy for each pile and each value of `M`.
- **Space Complexity:** O(n^2), for storing the DP table.