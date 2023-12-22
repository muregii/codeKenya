import java.util.*;

public class SortedLeaves {
    public String[] values(TreeNode tree) {
        // replace with working code ...
        List<String> leaves = new ArrayList<>();
        getLeaves(tree, leaves);
        Collections.sort(leaves);
        return leaves.toArray(new String[0]);
       
    }

    private void getLeaves(TreeNode node, List<String> leaves) {
        if(node == null){
            return;
        }

        if(node.left==null && node.right==null){
            leaves.add(String.valueOf((char)node.info));
        }

        getLeaves(node.left, leaves);
        getLeaves(node.right, leaves);
    }
}