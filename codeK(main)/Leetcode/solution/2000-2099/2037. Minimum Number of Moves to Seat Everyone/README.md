# Leetcode - Minimum Number of Moves to Seat Everyone

## Problem Description

There are `n` **availabe** seats and `n` students **standing** in a room. You are given an array `seats` of length `n`, where `seats[i]` is the position of the `ith` seat. You are also given the array `students` of length `n`, where `students[j]` is the position of the `jth` student.

You may perform the following move any number of times:

- Increase or decrease the position of the `ith` student by `1` (i.e., moving the `ith` student from position `x` to `x + 1` or `x - 1`)

Return *the **minimum number of moves** required to move each student to a seat such that no two students are in the same seat.*

Note that there may be **multiple** seats or students in the **same** position at the beginning.

**Constraints:**
- `n == seats.length == students.length`
- `1 <= n <= 100`
- `1 <= seats[i], students[j] <= 100`

## Solution

To minimize the number of moves required to seat all students:

1. **Understanding the Problem:**
   - We have `n` seats and `n` students with given positions.
   - The task is to move each student to a unique seat such that no two students end up in the same seat.
   - The challenge is to minimize the total number of moves needed to achieve this arrangement.

2. **Sorting for Efficient Pairing:**
   - By sorting both the `seats` and `students` arrays, we can align the closest available seat to each student.
   - Pairing the `i-th` seat with the `i-th` student ensures that each student is assigned to the nearest available seat.

3. **Calculate Moves:**
   - Iterate through the sorted lists and for each student, calculate the absolute difference between the student’s position and the seat’s position.
   - Sum these differences to get the minimum number of moves.

### Example

Suppose you have `seats = [4, 1, 5]` and `students = [3, 2, 7]`.

1. Sort `seats` and `students`:
   - Sorted `seats = [1, 4, 5]`
   - Sorted `students = [2, 3, 7]`
   
2. Calculate moves for each pair:
   - Moves for student `2` to seat `1`: `|2 - 1| = 1`
   - Moves for student `3` to seat `4`: `|3 - 4| = 1`
   - Moves for student `7` to seat `5`: `|7 - 5| = 2`
   
3. Total minimum moves: `1 + 1 + 2 = 4`.

### Python Code


```python
class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """

```

### Usage

To use the solution, create an instance of the `Solution` class and call the `minMovesToSeat` method with `seats` and `students`:

```python
solution = Solution()
seats = [4, 1, 5]
students = [3, 2, 7]
result = solution.minMovesToSeat(seats, students)
print(result)  # Output: 4
```

### Additional Resources

[Link to detailed explanation on GeeksforGeeks](https://www.geeksforgeeks.org/minimize-the-number-of-moves-required-to-seat-each-passenger-in-a-chair/)

[Link to detailed explanation on Medium](https://donic0211.medium.com/leetcode-2037-minimum-number-of-moves-to-seat-everyone-80d8fa8ecaa6)

[Link to detailed explanation on AlgoMonster](https://algo.monster/liteproblems/2037)

### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/wS7Ag33hf8E/mqdefault.jpg)](https://youtu.be/wS7Ag33hf8E)

[![Video Explanation](https://img.youtube.com/vi/9mO805GuZFI/mqdefault.jpg)](https://youtu.be/9mO805GuZFI)


### Complexity Analysis

- **Time Complexity:** O(n log n), where `n` is the length of the `seats` and `students` arrays. The complexity is dominated by the sorting step.
- **Space Complexity:** O(1), since no additional space proportional to the input size is required. The calculations are performed in-place.