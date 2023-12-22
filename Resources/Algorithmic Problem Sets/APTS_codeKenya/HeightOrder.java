import java.util.*;

/*Given a reference to the root of a binary tree, return an int[ ] of all values from the binary tree 
sorted from least to greatest height of the nodes containing those values. 
 Break ties for nodes of the same height by their value from least to greatest. 
For this question, height of a node is defined as the number of nodes on the longest simple path to a leaf from that node. 
The height of a leaf node is 1, whereas the root node has the greatest height of all nodes in the tree.  */

public class HeightOrder {
    public int[] arrange(TreeNode root) {

        Map<TreeNode, Integer> map = new HashMap<>();
        getHeight(root, map);
        List<TreeNode> var = new ArrayList<>(map.keySet());

        Collections.sort(var, (node1, node2) -> {

            int diff = map.get(node1) - map.get(node2);
            if (diff != 0) {
                return diff;
            } else {
                return node1.info - node2.info;
            }
        });
        int[] result = new int[var.size()];

        for (int i = 0; i < var.size(); i++) {
            result[i] = var.get(i).info;
        }
        return result;
    }

    private int getHeight(TreeNode tree, Map<TreeNode, Integer> map) {
        if (tree == null) {
            return 0;
        }
        int left= getHeight(tree.left, map);
        int right = getHeight(tree.right, map);

        int num = Math.max(left, right) + 1;

        map.put(tree, num);
        return num;
    }
}
