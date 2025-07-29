
"""
root = In life, there are only two things to worry about
left_child = Whether you're healthy
right_child = Whether you're sick.

              root
         /              `\`
        healthy                 sick 
        /      `\`                 /       `\`
    nothing to worry abt      better     worse
        
...

"""
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

joke = TreeNode(
    "There are two things in life that you worry about",
    TreeNode("Whether you're healthy",
             TreeNode("If you're healthy? You ain't got nothing to worry about")
             ), 
    TreeNode("Whether You're sick", 
             TreeNode("If you're sick, then you have two things to worry about, Whether you gonna get better"),
             TreeNode("Whether you gonna get worse",
                      TreeNode("If you get better, then you got nothing to worry about"),
                      TreeNode("if you get worse, then you've got two things to worry about",
                               TreeNode("Whether you're gonna live",
                                        TreeNode("If you live, ain't got nothing to worry about")
                                        ),
                               TreeNode("Or whether you gonna die",
                                        TreeNode("if you die? You got two things",
                                                 TreeNode("Whether you got to Heaven",
                                                          TreeNode("If you go to Heaven? Then you got nothing to worry about.")
                                                          ),
                                                 TreeNode("Whether you got to Hell",
                                                          TreeNode("But if you got to Hell",
                                                                   TreeNode("You got two things",
                                                                            TreeNode("Original"),
                                                                            TreeNode("Extra crispy")
                                                                            )
                                                                   )
                                                          )
                                                 )
                                        )
                               )
                      )
             ))

#

import time
from collections import deque

def delayed_print(msg):
    time.sleep(3)
    print(msg)

#level order traversal Breadth First Search
def print_tree_dfs(root):
    if not root:
        return ""
    delayed_print(root.val) # Depth First Search : Pre-Order Traversal
    print_tree(root.left)
    print_tree(root.right)
    
def tree_height(node):
    if not node:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))

# 2) Print all nodes at a given level
def print_level(node, level):
    if not node:
        return
    if level == 1:
        delayed_print(node.val)
    else:
        # recurse down, decreasing level
        print_level(node.left,  level - 1)
        print_level(node.right, level - 1)

# 3) Recursive level‑order using the two helpers
def print_tree_bfs(root):
    h = tree_height(root)
    for lvl in range(1, h + 1):
        print_level(root, lvl)

#print_tree_dfs(joke)
print_tree_bfs(joke)
print_tree_dfs(joke)

#delayed_print(joke.val)
#delayed_print(joke.left.val)
#delayed_print(joke.right.val)
#delayed_print(joke.left.left.val)
#delayed_print(joke.right.left.val)
#delayed_print(joke.right.right.val)
#delayed_print(joke.right.right.left.val)
#delayed_print(joke.right.right.right.val)
#delayed_print(joke.right.right.right.left.val)
#delayed_print(joke.right.right.right.right.val)
#delayed_print(joke.right.right.right.left.left.val)
#delayed_print(joke.right.right.right.right.left.val)
#delayed_print(joke.right.right.right.right.left.left.val)
#delayed_print(joke.right.right.right.right.left.right.val)
#delayed_print(joke.right.right.right.right.left.left.left.val)
#delayed_print(joke.right.right.right.right.left.right.left.val)
#delayed_print(joke.right.right.right.right.left.right.left.left.val)
#delayed_print(joke.right.right.right.right.left.right.left.left.left.val)
#delayed_print(joke.right.right.right.right.left.right.left.left.right.val)
