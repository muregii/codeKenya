# Leetcode - Sandwich Problem

## Problem Description

The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers `0` and `1` respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a **stack**. At each step:

1. If the student at the front of the queue **prefers** the sandwich on the top of the stack, they will **take it** and leave the queue.
2. Otherwise, they will **leave it** and go to the queue's end.

This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

You are given two integer arrays `students` and `sandwiches` where `sandwiches[i]` is the type of the `i​​​​​th` sandwich in the stack (`i = 0` is the top of the stack) and `students[j]` is the preference of the `j​​​​​​th` student in the initial queue (`j = 0` is the front of the queue). Return _the number of students that are unable to eat._

## Solution

The solution to this problem can be implemented using a simulation approach. Here's how it works:


Okay, let me explain this again simply:

The goal is to figure out how many students won't be able to get a sandwich they like. We have two lists - one that tells us the type of each sandwich in the stack, and one that tells us the preference of each student in the line.

Here's how we can solve this:

1. We start by looking at the first student in the line and the sandwich on top of the stack.
2. If the student's preference matches the sandwich, we'll take the sandwich off the stack and move on to the next student and sandwich.
3. If the student's preference doesn't match, we'll move the student to the back of the line and move on to the next sandwich.
4. We keep doing this until either all the students have been served or there are no more sandwiches left.
5. The number of students who didn't get a sandwich they liked is the answer.

The key steps are:
1. Initialize a variable to keep track of the number of students who couldn't eat
2. Loop through the students and sandwiches
3. Check if the student's preference matches the sandwich on top of the stack
4. If it does, remove the student and sandwich; if it doesn't, move the student to the back of the line
5. Return the final count of students who couldn't eat

Does this make sense? Great!

## Usage

To use the solution, you can call the `countStudents` method with the `students` and `sandwiches` arrays:

```python
students = [1, 1, 0, 0]
sandwiches = [0, 1, 0, 1]
solution = Solution()
unable_to_eat = solution.countStudents(students, sandwiches)
print(unable_to_eat)  # Output: 0
```
## Check Out this video

[![Video Explanation](https://img.youtube.com/vi/d_cvtFwnOZg/0.jpg)](https://youtu.be/d_cvtFwnOZg)


## Complexity Analysis

- **Time Complexity:** O(n), where n is the length of the `students` and `sandwiches` arrays. This is because we are iterating through the arrays once.
- **Space Complexity:** O(1), as we are only using a constant amount of extra space to store the `unable_to_eat` variable.