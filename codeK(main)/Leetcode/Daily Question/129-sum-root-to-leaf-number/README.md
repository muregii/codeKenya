# Leetcode - Sum of Root to Leaf Numbers

## Problem Description

You are given the `root` of a binary tree containing digits from `0 to 9` only. 
Each root-to-leaf path in the tree represents a number. 

For example, the root-to-leaf path `1 -> 2 -> 3` represents the number `123`. 

Return the `total sum of all root-to-leaf numbers`. 

Test cases are generated so that the answer will fit in a 32-bit integer. A `leaf node` is a node with no children.


## Solution

The idea is to traverse from root to all leaves in top-down fashion maintaining a path[] array to store current root to leaf path. While traversing, store data of all nodes of current path in the array path[]. Whenever a leaf node is reached, calculate the sum of all of the nodes on the current path using the array path[] and check if it is equal to the given sum.

Here's how we can calculate the sum of root to leaf numbers:

1. We'll start from the root of the tree.
2. We'll go down the tree, keeping track of the current number formed by the path from the root.
3. When we reach a leaf node, we'll add the number formed by the path from the root to this leaf to our sum.
4. We'll repeat this process for every path from the root to a leaf.
5. At the end, we'll have the sum of all root-to-leaf numbers.



Does this make sense? Great!"


## Usage

To use the solution, simply create an instance of the `Solution` class and call the `sumNumbers` method with the input `root` representing the root of the binary tree:

```python
solution = Solution()
# Define the binary tree nodes
# root = TreeNode(val=1)
# root.left = TreeNode(val=2)
# root.right = TreeNode(val=3)
# ...
# Call the sumNumbers method
result = solution.sumNumbers(root)
print(result)
```

```python
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```


[Link to detailed explanation on Medium](https://medium.com/@choudharyarpit99/leetcode-129-sum-root-to-leaf-numbers-b8149061b376)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/root-to-leaf-path-sum-equal-to-a-given-number-in-bst/)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/applications-of-bst/?ref=lbp)




## Check Out this video

[![Video Explanation](https://img.youtube.com/vi/Gi0202QawRQ/mqdefault.jpg)](https://youtu.be/Gi0202QawRQ)


[![Video Explanation](https://img.youtube.com/vi/Jk16lZGFWxE/mqdefault.jpg)](https://youtu.be/Jk16lZGFWxE)





## Complexity Analysis

- **Time Complexity:** O(n), where n is the number of nodes in the binary tree.
- **Space Complexity:** O(h), where h is the height of the binary tree. In the worst case, the space complexity can be O(n) for a skewed tree.

---

