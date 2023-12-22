import java.util.*;

public class AllPaths {
    public String[] paths(TreeNode t) {
        //paths main methos

       
       
    }
    
     //helper method ? Recursively traverses
    private void getPath(TreeNode tree, "", ) {
        if(tree == null) {
            return;
        }

        if(tree.left != null && tree.right != null) {
            tree.info +="->";
        }

        getPath(tree.left, "");
        getPath(tree.right, "");

    }
}
