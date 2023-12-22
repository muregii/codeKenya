
public class LeafCollector {
    
    public String[] getLeaves(TreeNode tree){
        
        List<String> leaves = new  ArrayList<>();
        removeLeaves(tree, leaves);
        return leaves.toArray(new String[0]);
    }

    private void removeLeaves(TreeNode tree, List<String>leaves) {
        StringBuilder str = new StringBuilder<>();

        if(tree == null) { return;}
        if(tree.left == null && tree.right == null) {//to get to the leaf node.
            str.add("" + tree.info);
            leaves.add(String.join("", str));  
        }

        removeLeaves(tree.left, leaves);
        removeLeaves(tree.right, leaves);
        

    }
}