# Leetcode - Hand of Straights

## Problem Description

Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size `groupSize`, and consists of `groupSize` consecutive cards.

Given an integer array `hand` where `hand[i]` is the value written on the `i-th` card, and an integer `groupSize`, return `true` if she can rearrange the cards, or `false` otherwise.

**Constraints:**
- `1 <= hand.length <= 10^4`
- `0 <= hand[i] <= 10^9`
- `1 <= groupSize <= hand.length`

## Solution

To determine if Alice can rearrange her cards into groups where each group has `groupSize` consecutive cards, we need to check if it's possible to group all cards this way without leaving any cards out.


Imagine you have a deck of numbered cards, and you want to create sets of cards where each set has the same number of cards and the numbers are in sequence. For example, if you have the numbers `[1, 2, 3, 4, 5, 6]` and you want to make groups of `3`, you would make `[1, 2, 3]` and `[4, 5, 6]`. But if you had `[1, 2, 4, 5, 6]`, you couldn’t make a group of 3 starting from 1 because you're missing a 3.


Here are the steps:

1. **Sort the Cards:**
   - Start by sorting the cards so that we can easily check for consecutive sequences.

2. **Count Each Card:**
   - Use a dictionary to count how many times each card appears.

3. **Form Groups of Consecutive Cards:**
   - For each card, try to form a group starting from that card. Use the counts to check if you can complete the group of `groupSize`.
   - Reduce the count of each card in the group as you use them.
   - If at any point you can’t form a complete group, return `false`.

4. **Check All Cards:**
   - Make sure that every card has been used in forming groups.


By sorting the cards and using a dictionary to keep track of how many times each card appears, we can efficiently check if we can form groups of consecutive cards. Each time we start a new group, we reduce the count of each card in the group to ensure no card is left out.


```python

class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """

```

## Usage

To use the solution, create an instance of the `Solution` class and call the `isNStraightHand` method with the list of cards (`hand`) and the desired group size (`groupSize`):

```python
solution = Solution()
hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
groupSize = 3
result = solution.isNStraightHand(hand, groupSize)
print(result)  # Output: True, because we can form groups [1,2,3], [2,3,4], [6,7,8]

hand = [1, 2, 3, 4, 5]
groupSize = 4
result = solution.isNStraightHand(hand, groupSize)
print(result)  # Output: False, because we cannot form groups of 4 with consecutive numbers
```

[Link to detailed explanation on AlgoMonster](https://algo.monster/liteproblems/846)

## Check Out This Video

[![Video Explanation](https://img.youtube.com/vi/lpVhzcdiHMs/mqdefault.jpg)](https://youtu.be/lpVhzcdiHMs)

[![Video Explanation](https://img.youtube.com/vi/amnrMCVd2YI/mqdefault.jpg)](https://youtu.be/amnrMCVd2YI)

[![Video Explanation](https://img.youtube.com/vi/CnMwFyoD0Bk/mqdefault.jpg)](https://youtu.be/CnMwFyoD0Bk)

## Complexity Analysis

- **Time Complexity:** O(n log n + nk), where `n` is the number of cards in `hand` and `k` is the `groupSize`. Sorting takes `O(n log n)` and checking the counts takes `O(nk)`.
- **Space Complexity:** O(n), as we are using a counter to store the frequency of each card.