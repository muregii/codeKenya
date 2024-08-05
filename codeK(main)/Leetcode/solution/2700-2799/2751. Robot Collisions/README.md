# Leetcode - Robot Collisions

## Problem Description

There are `n` **1-indexed** robots, each having a position on a line, health, and movement direction.

You are given **0-indexed** integer arrays `positions`, `healths`, and a string `directions` (directions[i] is either **'L'** for **left** or **'R'** for **right**). All integers in `positions` are **unique**.

All robots start moving on the line **simultaneously** at the **same speed** in their given directions. If two robots ever share the same position while moving, they will **collide**.

If two robots collide, the robot with **lower health** is **removed** from the line, and the health of the other robot **decreases** by **one**. The surviving robot continues in the **same** direction it was going. If both robots have the **same** health, they are both removed from the line.

Your task is to determine the **health** of the robots that survive the collisions, in the same **order** that the robots were given, i.e., final health of robot 1 (if survived), final health of robot 2 (if survived), and so on. If there are no survivors, return an empty array.

Return *an array containing the health of the remaining robots (in the order they were given in the input) after no further collisions can occur*.

**Note**: The positions may be unsorted.

**Constraints:**
- `1 <= positions.length == healths.length == directions.length == n <= 10^5`
- `1 <= positions[i], healths[i] <= 10^9`
- `directions[i] == 'L' or directions[i] == 'R'`
- All values in `positions` are distinct

## Solution

To solve this problem, simulate the collisions and determine the remaining health of each robot.

1. **Understanding the Problem:**
   - Robots move in either left ('L') or right ('R') direction.
   - Collisions occur when two robots share the same position.
   - The robot with lower health is removed, and the surviving robot's health decreases by one.
   - If both robots have the same health, they are both removed.

2. **Simulating the Process:**
   - Sort robots by their positions.
   - Use a stack to manage the collisions:
     - Push right-moving robots onto the stack.
     - For each left-moving robot, check for collisions with the stack's top robot.
     - Resolve collisions according to the rules.
   - Continue until all collisions are resolved.

3. **Algorithm Steps:**
   - Sort robots by position to ensure we process them in the correct order.
   - Use a stack to handle collisions:
     - Push robots moving right ('R') onto the stack.
     - For each robot moving left ('L'), resolve collisions with robots in the stack.
   - Collect the health of surviving robots and return them in the input order.

### Example

Suppose you have:
- `positions = [1, 3, 5, 6]`
- `healths = [10, 5, 6, 8]`
- `directions = "RLRL"`

1. Sort robots by positions.
2. Use a stack to simulate collisions:
   - Robot at position 1 moves right, push to stack.
   - Robot at position 3 moves left, collide with robot at position 1.
   - Robot at position 5 moves right, push to stack.
   - Robot at position 6 moves left, collide with robot at position 5.

### Python Code

```python
class Solution(object):
    def survivedRobotsHealths(self, positions, healths, directions):
        """
        :type positions: List[int]
        :type healths: List[int]
        :type directions: str
        :rtype: List[int]
        """
        
```

### Usage

To use the solution, create an instance of the `Solution` class and call the `survivedRobotsHealths` method with the `positions`, `healths`, and `directions` arrays:

```python
# Example usage
solution = Solution()
positions = [1, 3, 5, 6]
healths = [10, 5, 6, 8]
directions = "RLRL"
result = solution.survivedRobotsHealths(positions, healths, directions)
print(result)  # Output: [9, 6]
```

### Additional Resources

[Link to detailed explanation on Medium](https://medium.com/@ashwinmani37/robot-collisions-problem-leetcode-2751-be4fc2a44de6)

### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/FMV5Pp0tdXY/mqdefault.jpg)](https://youtu.be/FMV5Pp0tdXY)

[![Video Explanation](https://img.youtube.com/vi/kLjAWG1Je-c/mqdefault.jpg)](https://youtu.be/kLjAWG1Je-c)

[![Video Explanation](https://img.youtube.com/vi/xgojcwRX4Tg/mqdefault.jpg)](https://youtu.be/xgojcwRX4Tg)

### Complexity Analysis

- **Time Complexity:** O(n log n) due to sorting the robots by their positions.
- **Space Complexity:** O(n), due to the use of a stack to manage the robots and their collisions.