# Leetcode - Kth Largest Element in a Stream

## Problem Description

You are part of a university admissions office and need to keep track of the `kth` highest test score from applicants in real-time. This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit their scores.

You are tasked to implement a class which, for a given integer `k`, maintains a stream of test scores and continuously returns the `kth` highest test score after a new score has been submitted. More specifically, we are looking for the `kth` highest score in the sorted list of all scores.

Implement the `KthLargest` class:
- `KthLargest(int k, int[] nums)` Initializes the object with the integer `k` and the stream of test scores `nums`.
- `int add(int val)` Adds a new test score `val` to the stream and returns the element representing the **kth largest** score so far.

**Constraints:**
- `0 <= nums.length <= 10^4`
- `1 <= k <= nums.length + 1`
- `-10^4 <= nums[i], val <= 10^4`
- At most `10^4` calls will be made to the `add` method.

## Solution

**Understanding the Problem:**
   - You need to maintain the **kth largest** score in a dynamically changing list of test scores.
   - The challenge is to efficiently find the **kth largest** element in a stream of incoming scores without having to fully sort the list after each addition.

**Breaking It Down**
   - **Heap Data Structure:**
     - A **min-heap** (priority queue) is an ideal data structure for this problem. By maintaining a heap of size `k`, the smallest element in the heap will always be the **kth largest** element.
     - Every time a new score is added:
       - If the heap size is less than `k`, we add the new element.
       - If the heap size is already `k`, we replace the smallest element in the heap with the new score (if the new score is larger).
     - The smallest element in the heap represents the **kth largest** element.
     
**Implementation Approach:**
   - Initialize a **min-heap** to keep track of the top `k` elements from the score stream.
   - Each time a new score is added, compare it to the smallest element in the heap.
   - Maintain the heap size at exactly `k`, ensuring the smallest element in the heap is the **kth largest** score.

**Algorithm Steps:**
   - **Heap Initialization:** Initialize a min-heap with the first `k` elements of `nums`.
   - **Maintain the Heap:** For each new score, add it to the heap, and if the heap size exceeds `k`, remove the smallest element.
   - **Return the Kth Largest Element:** The smallest element in the heap represents the **kth largest** score.

### Python Code

```python


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        
```

### Example

```python
# Input
k = 3
nums = [4, 5, 8, 2]
kthLargest = KthLargest(3, nums)
print(kthLargest.add(3))  # Output: 4
print(kthLargest.add(5))  # Output: 5
print(kthLargest.add(10)) # Output: 5
print(kthLargest.add(9))  # Output: 8
print(kthLargest.add(4))  # Output: 8
```

### Explanation

1. **Initialization:**
   - You start with the array `[4, 5, 8, 2]` and `k = 3`.
   - After initializing, the heap contains the three largest elements `[5, 8, 4]` (smallest of them is the **kth largest**, which is 4).
   
2. **Adding Elements:**
   - When `3` is added, it is smaller than the **kth largest** element (4), so the heap remains unchanged.
   - When `5` is added, the heap updates to `[5, 8, 5]`, and the new **kth largest** is 5.
   - Adding `10` replaces the smallest element, and the **kth largest** becomes 5.
   - Similarly, adding `9` changes the **kth largest** to 8.

### Usage

To use the solution, create an instance of the `KthLargest` class and call the `add` method with the incoming test score:

```python
# Example usage
k = 3
nums = [4, 5, 8, 2]
kthLargest = KthLargest(k, nums)
print(kthLargest.add(3))  # Output: 4
print(kthLargest.add(5))  # Output: 5
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/703)

[Link to detailed explanation on Medium](https://lenchen.medium.com/leetcode-703-kth-largest-element-in-a-stream-194ceb1572)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/kth-largest-element-in-a-stream/)


### Check Out These Video(s)

[![Video Explanation](https://img.youtube.com/vi/0tFmP1Eiilg/mqdefault.jpg)](https://youtu.be/0tFmP1Eiilg)

[![Video Explanation](https://img.youtube.com/vi/hOjcdrqMoQ8/mqdefault.jpg)](https://youtu.be/hOjcdrqMoQ8)


### Complexity Analysis

- **Time Complexity:**
  - `O(log k)` per `add` operation, as heap insertions and deletions take `O(log k)` time, where `k` is the size of the heap.
  - Initializing the heap takes `O(n log k)` time, where `n` is the size of the input list.

- **Space Complexity:** `O(k)` to store the top `k` elements in the heap.