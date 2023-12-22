
public class PathSum {

    public int hasPath(int target, TreeNode tree){
        // replace with working code
        if(tree == null) {
            return 0;
        }
        else if(tree.left == null && tree.right == null && tree.info == target) {
            return 1;
        }
        else{
            int remTarget = target - tree.info;
            return hasPath(remTarget, tree.left) | hasPath(remTarget, tree.right);

        }

    } 
  
}