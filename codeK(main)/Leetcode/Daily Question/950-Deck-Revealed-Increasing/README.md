# Leetcode - Revealing Cards in Increasing Order

## Problem Description

You are given an integer array `deck`. There is a deck of cards where every card has a unique integer. The integer on the `ith` card is `deck[i]`.

You can order the deck in any order you want. Initially, all the cards start face down (unrevealed) in one deck.

You will do the following steps repeatedly until all cards are revealed:

1. Take the top card of the deck, reveal it, and take it out of the deck.
2. If there are still cards in the deck, then put the next top card of the deck at the bottom of the deck.
3. If there are still unrevealed cards, go back to step 1. Otherwise, stop.

Your task is to return an ordering of the deck that would reveal the cards in increasing order.

## Solution

We can solve this problem using the following steps:

1. Sort the `deck` in increasing order to get the desired output.
2. Create a queue `queue` that initially contains the indices of the cards in the `deck`.
3. Iterate through the sorted `deck` and perform the following steps:
   - Take the first index from the `queue` and assign the corresponding value from the sorted `deck` to the `result` list at that index.
   - If there are still elements in the `queue`, take the first element and add it to the end of the `queue`.
4. Return the `result` list, which represents the ordering of the deck that would reveal the cards in increasing order.


Does this make sense? Great!

## Usage

Our target is to get an deck array that an ordering of the deck that would reveal the cards in increasing order. It can be difficult to go through an original deck array. So we will start from the increasing order of deck array. And we will go to these reversed steps.

![leetcode-950-1](https://github.com/aTfure/codeKenya/assets/87364726/98f6a326-9648-4933-bebd-03838db0946c)



## Check Out this video

[![Video Explanation](https://img.youtube.com/vi/lx7sXPATO3U/mqdefault.jpg.jpg)](https://youtu.be/lx7sXPATO3U)

The video above explains the solution approach in detail.


## Complexity Analysis

- **Time Complexity**: O(n log n) due to the sorting step.
- **Space Complexity**: O(n) for the `queue` and `result` lists.
