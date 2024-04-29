
# Leetcode - Open the Lock

## Problem Description

You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: `'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'`. The wheels can rotate freely and wrap around: for example we can turn `9` to be `0`, or `0` to be `9`. Each move consists of turning one wheel one slot.

The lock initially starts at `0000`, a string representing the state of the 4 wheels.

You are given a list of `deadends` dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a `target` representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or `-1` if it is impossible.

## Solution

To solve this problem, we can use a Breadth-First Search (BFS) approach. We start with the initial state of the lock ('0000') and explore all possible combinations of turning each wheel. For each combination, we check if it's a valid move and not in the list of deadends. We continue this process until we find the target combination or exhaust all possible moves.


Here's how we can approach this problem:

1. Initialize a set `visited` to keep track of visited combinations.
2. Initialize a queue `queue` to store the combinations to be explored.
3. Enqueue the initial state of the lock ('0000') into the queue.
4. While the queue is not empty, dequeue a combination from the queue.
5. Check if the dequeued combination is the target. If yes, return the number of moves required to reach it.
6. Otherwise, generate all possible combinations by turning each wheel in both directions and enqueue valid and unvisited combinations into the queue.
7. Mark each visited combination to avoid revisiting them.
8. If all possible combinations are explored and the target is not found, return -1.

By performing a BFS traversal, we can determine the minimum total number of turns required to open the lock.


## Usage

To use the solution, create an instance of the `Solution` class and call the `openLock` method with the input parameters `deadends` and `target`:

```python
solution = Solution()
# Define the list of deadends and the target combination
# deadends = ["0201","0101","0102","1212","2002"]
# target = "0202"
# Call the openLock method
result = solution.openLock(deadends, target)
print(result)
```

```python
# deadends = ["0201","0101","0102","1212","2002"]
# target = "0202"
```


## Check Out this video

[![Video Explanation](https://img.youtube.com/vi/Pzg3bCDY87w/mqdefault.jpg)](https://youtu.be/Pzg3bCDY87w)


[![Video Explanation](https://img.youtube.com/vi/ZDxT25NjMxM/mqdefault.jpg)](https://youtu.be/ZDxT25NjMxM)


## Complexity Analysis

- **Time Complexity:** O(N^2 * A^N + D), where N is the number of wheels (4 in this case), A is the number of digits (10 in this case), and D is the size of the deadends list. We explore all possible combinations of the lock with a maximum depth of N, each combination requires O(N) time to generate, and there can be up to A^N combinations. Additionally, we iterate through the deadends list once.
- **Space Complexity:** O(A^N + D), where A^N is the maximum number of states in the queue, and D is the size of the deadends list. We use additional space for the queue and the visited set.

