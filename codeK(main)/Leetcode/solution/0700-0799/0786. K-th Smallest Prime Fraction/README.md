# Leetcode - Kth Smallest Prime Fraction

## Problem Description

You are given a sorted integer array `arr` containing `1` and **prime** numbers, where all the integers of `arr` are unique. You are also given an integer `k`.

For every `i` and `j` where `0 <= i < j < arr.length`, we consider the fraction `arr[i] / arr[j]`.

*Return the `kth` smallest fraction considered*. Return your answer as an array of integers of size 2, where `answer[0] == arr[i]` and `answer[1] == arr[j]`.

**Constraints:**

- `2 <= arr.length <= 1000`
- `1 <= arr[i] <= 3 * 104`
- `arr[0] == 1`
- `arr[i]` is a **prime** number for `i > 0`.
- All the numbers of arr are **unique** and sorted in **strictly increasing** order.
- `1 <= k <= arr.length * (arr.length - 1) / 2`

## Solution

To solve this problem, we can use a min-heap to efficiently find the `kth` smallest fraction. Here's a step-by-step approach to achieve this:

1. **Initialize the Min-Heap**: Start by pushing all possible fractions `arr[i] / arr[j]` into the heap, but only push the first element of each potential fraction `arr[0] / arr[j]` initially to keep the heap size manageable.
2. **Heap Operations**: Extract the smallest element from the heap `k` times. For each extracted element `arr[i] / arr[j]`, if there are more fractions with the same denominator, push the next fraction into the heap.
3. **Return the Result**: After extracting `k` elements, the `kth` extracted element is the desired fraction.

This method ensures that we efficiently find the `kth` smallest fraction using the properties of a min-heap.

## Usage

To use the solution, create an instance of the `Solution` class and call the `kthSmallestPrimeFraction` method with the input parameters `arr` and `k`:

```python
class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """

# Example Usage
solution = Solution()
arr = [1, 2, 3, 5]
k = 3
result = solution.kthSmallestPrimeFraction(arr, k)
print(result)  # Output: [2, 5]
```

## Explanation

1. **Input**: The array `arr` and integer `k` are given.
2. **Heap Initialization**: We initialize a min-heap with the fractions where the numerator is `arr[0]` and the denominator is every other element in `arr`.
3. **Heap Operations**: We extract the smallest fraction from the heap `k-1` times, pushing the next fraction with the same denominator into the heap each time.
4. **Result**: The `kth` extracted element gives us the desired fraction.

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/introduction-to-min-heap-data-structure/)


[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/k-th-prime-factor-given-number/)


[Link to detailed explanation on AlgoMonster](https://algo.monster/problems/heap_intro)



[Link to detailed explanation on AlgoMonster](https://algo.monster/problems/kth_smallest_element_in_a_sorted_matrix)


## Check Out these videos

[![Video Explanation](https://img.youtube.com/vi/SmxdebjWvfs/mqdefault.jpg)](https://youtu.be/SmxdebjWvfs)


[![Video Explanation](https://img.youtube.com/vi/sJdJTXhxqjo/mqdefault.jpg)](https://youtu.be/sJdJTXhxqjo)

## Complexity Analysis

- **Time Complexity:** O(k log k), where k is the number of operations performed in the heap. Each insertion and extraction operation in the heap takes O(log k) time.
- **Space Complexity:** O(k), where k is the number of elements in the heap at any given time.