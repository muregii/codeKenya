# Leetcode - N-ary Tree Postorder Traversal

## Problem Description

Given the `root` of an n-ary tree, return _the postorder traversal of its nodes' values._

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

**Constraints:**

- The number of nodes in the tree is in the range `[0, 10^4]`.
- `0 <= Node.val <= 10^4`.
- The height of the n-ary tree is less than or equal to `1000`.

**Follow-up:** The recursive solution is trivial, but could you implement an iterative approach?

## Solution

### Understanding the Problem:

The task is to traverse an **n-ary tree** using **postorder traversal**. This means:

1. First, we recursively visit all children nodes.
2. After visiting all children, we then process the root node.

### Breaking It Down:

- **Recursive Approach:** This can be solved easily using recursion. We recursively process each child node, then add the current node’s value to the result list. However, this follow-up asks for an **iterative** solution.
- **Iterative Approach:** To solve this iteratively, we can simulate recursion using a **stack**. Instead of letting the system handle recursion for us, we manually track which nodes we’ve processed and their children.

### Algorithm Steps:

#### Recursive Solution:

1. **Base Case:** If the root is `None`, return an empty list.
2. **Recursive Function:**
   - Traverse all the children first.
   - Then, append the value of the current node.
3. **Return the Result:** The final list will contain the postorder traversal.

#### Iterative Solution:

1. **Initialize a Stack:** Use a stack to simulate recursion. Add the root to the stack.
2. **Process Nodes:** While the stack is not empty:
   - Pop a node from the stack.
   - Append the node's value to the result list.
   - Push all its children to the stack.
3. **Reverse the Result:** Since we process the root before its children (which is the opposite of postorder), reverse the result list at the end.
4. **Return the Result.**

### Python Code

```python
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

```

### Example

```python
# Input: root = [1, None, 3, 2, 4, None, 5, 6] (N-ary tree level order representation)
# Tree structure:
#        1
#      / | \
#     3  2  4
#    / \
#   5   6

# Output: [5, 6, 3, 2, 4, 1]

solution = Solution()
root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
result = solution.postorder(root)
print(result)  # Output: [5, 6, 3, 2, 4, 1]
```

### Usage

To use this solution, create an instance of the `Solution` class and call the `postorder` method with the root of the N-ary tree.

```python
solution = Solution()
root = Node(1, [Node(3, [Node(5), Node(6)]), Node(3), Node(4)])
result = solution.postorder(root)
print(result)  # Output: [5, 6, 3, 2, 4, 1]
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/590)

[Link to a detailed explanation on GeeksforGeeks](https://www.geeksforgeeks.org/construct-a-complete-n-ary-tree-from-given-postorder-traversal/)

[Link to a detailed explanation on GeeksforGeeks](https://www.geeksforgeeks.org/iterative-postorder-traversal-of-n-ary-tree/)

[Link to a detailed explanation on Medium](https://medium.com/@snehakweera77/590-n-ary-tree-postorder-traversal-972b3ce70cdf)

### Check Out These Video(s):

[![Video Explanation](https://img.youtube.com/vi/vnhlZ4bhEzo/mqdefault.jpg)](https://youtu.be/vnhlZ4bhEzo)

[![Video Explanation](https://img.youtube.com/vi/DAIN1ZzvFeA/mqdefault.jpg)](https://youtu.be/DAIN1ZzvFeA)

[![Video Explanation](https://img.youtube.com/vi/GMUI91_pDmM/mqdefault.jpg)](https://youtu.be/GMUI91_pDmM)

### Complexity Analysis

- **Time Complexity:** O(n), where `n` is the number of nodes in the tree. We visit each node exactly once during the traversal.
- **Space Complexity:** O(n), in the worst case due to the stack used to simulate recursion (if the tree is deep) or the result list, which stores the values of all nodes.
