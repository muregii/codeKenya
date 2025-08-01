
"""
root = In life, there are only two things to worry about
left_child = Whether you're healthy
right_child = Whether you're sick.
depth first search
breadth first search
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
    time.sleep(1)
    print(msg)

#def print_tree(root):
#    if not root:
#        return ""
#    delayed_print(root.val)
#    print_tree(root.left)
#    print_tree(root.right)


def print_tree_dfs(root):
    def dfs(root):
        if not root:
            return ""
         # Depth First Search : Pre-Order Traversal
        print_tree_dfs(root.left)
         #in order traversal
        print_tree_dfs(root.right)
        delayed_print(root.val) #post order traversal

    return dfs(root)



def print_tree_bfs1(root):
    def print_level(node, level):
        if not node:
            return
        if level == 1:
            delayed_print(node.val)
        else:
        # recurse down, decreasing level
            print_level(node.left,  level - 1)
            print_level(node.right, level - 1)
    def tree_height(root):
        if not root:
            return 0
        return 1 + max(tree_height(root.left), tree_height(root.right))

    h = tree_height(root)
    for lvl in range (1, h + 1):
        print_level(root, lvl)

from collections import deque

def print_tree_bfs2(root):
    if not root:
        return 
    
    q = deque([root])

    while q:
        for _ in range(len(q)):
            node = q.popleft()
            delayed_print(node.val)
        
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    

    

#print_tree_dfs(joke)
print(print_tree_bfs2(joke))
#print_tree_dfs(joke)
#print(print_tree_bfs1(joke))

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
