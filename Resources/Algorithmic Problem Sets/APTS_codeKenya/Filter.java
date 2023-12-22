

/*In java, given the root of a binary tree called root, 
say that a subtree is bad if the depth of the node rooting the subtree is greater than the number of paths
 to leaf nodes from the node rooting the subtree. Return a new binary 
 tree that is identical to the input except that all bad subtrees have been removed.
  Recall that depth of a root node is 0, and its children have a depth of 1, as so on. 
We count a leaf node as having one path to leaf nodes. We count the number of paths to leaf nodes in the original tree, not the filtered tree. Use the skeleton public class Filter{
public TreeNode filtered (TreeNode root){
 }

}. */

public class Filter {
    public TreeNode filtered(TreeNode root) {
        return removeBadSubtrees(root, 0);
    }

    private int countLeafPaths(TreeNode node) {
        if (node == null) return 0;
        if (node.left == null && node.right == null) return 1;

        return countLeafPaths(node.left) + countLeafPaths(node.right);
    }

    private TreeNode removeBadSubtrees(TreeNode node, int depth) {
        if (node == null) return null;

        if (depth > countLeafPaths(node)) return null;

        node.left = removeBadSubtrees(node.left, depth + 1);
        node.right = removeBadSubtrees(node.right, depth + 1);

        return node;
    }
}