# Leetcode - Crawler Log Folder

## Problem Description

The Leetcode file system keeps a log each time some user performs a change folder operation. The operations are described below:

- `"../"`: Move to the parent folder of the current folder. (If you are already in the main folder, **remain in the same folder**).
- `"./"`: Remain in the same folder.
- `"x/"`: Move to the child folder named `x` (This folder is **guaranteed to always exist**).

You are given a list of strings `logs` where `logs[i]` is the operation performed by the user at the `i`th step.

The file system starts in the main folder, then the operations in `logs` are performed.

Return *the minimum number of operations needed to go back to the main folder after the change folder operations*.

**Constraints:**
- `1 <= logs.length <= 10^3`
- `2 <= logs[i].length <= 10`
- `logs[i]` contains lowercase English letters, digits, '.', and '/'.
- `logs[i]` follows the format described in the statement.
- Folder names consist of lowercase English letters and digits.

## Solution

To determine the minimum number of operations needed to go back to the main folder, simulate the file system navigation based on the given logs.

1. **Understanding the Problem:**
   - `"../"`: Move to the parent folder unless already in the main folder.
   - `"./"`: Stay in the current folder.
   - `"x/"`: Move to the child folder named `x`.

2. **Simulating the Process:**
   - Use a counter to track the current depth of the folder.
   - Increment the counter for each `"x/"` operation.
   - Decrement the counter for each `"../"` operation, ensuring it doesn't go below zero.
   - Ignore `"./"` operations as they don't change the folder depth.

3. **Algorithm Steps:**
   - Initialize a counter `depth` to 0.
   - Iterate through each log entry and update the `depth` based on the type of operation.
   - Return the current depth as the minimum number of operations to go back to the main folder.

### Example

Suppose you have `logs = ["d1/", "d2/", "../", "d21/", "./"]`:

1. `"d1/"`: Move to child folder `d1` (depth = 1).
2. `"d2/"`: Move to child folder `d2` (depth = 2).
3. `"../"`: Move to parent folder (depth = 1).
4. `"d21/"`: Move to child folder `d21` (depth = 2).
5. `"./"`: Stay in the current folder (depth = 2).

Minimum number of operations to go back to the main folder: 2.

### Python Code

```python
class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        
```

### Usage

To use the solution, create an instance of the `Solution` class and call the `minOperations` method with the list of logs:

```python
# Example usage
solution = Solution()
logs = ["d1/", "d2/", "../", "d21/", "./"]
result = solution.minOperations(logs)
print(result)  # Output: 2
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/1598)

### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/Ur3saIXP7ro/mqdefault.jpg)](https://youtu.be/Ur3saIXP7ro)

[![Video Explanation](https://img.youtube.com/vi/6pEO1jUuA-E/mqdefault.jpg)](https://youtu.be/6pEO1jUuA-E)

[![Video Explanation](https://img.youtube.com/vi/n_VTHCuidBQ/mqdefault.jpg)](https://youtu.be/n_VTHCuidBQ)

### Complexity Analysis

- **Time Complexity:** O(n), as we iterate through the list of logs once.
- **Space Complexity:** O(1), as we use a constant amount of extra space.