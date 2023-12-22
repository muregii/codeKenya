
public class HeightLabel {
    
    public TreeNode rewire(TreeNode t) {
        // replace with working code ...
        if(t==null) {
            return null;
        }

        
        int height = getHeight(t);
        TreeNode node = new TreeNode(height);
        node.left = rewire(t.left);
        node.right = rewire(t.right);

        return node;    
    }

    private int getHeight(TreeNode t) {
        if(t==null){
            return 0;
        }


        int leftHeight = getHeight(t.left);
        int rightHeight = getHeight(t.right);
        
        return Math.max(leftHeight, rightHeight) + 1;
    }
    
}

