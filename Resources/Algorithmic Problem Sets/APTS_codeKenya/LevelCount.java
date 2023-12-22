
public class LevelCount {
    public int count(TreeNode t, int level) {
        // replace with working code ...
        if(t == null) {
            return 0;
        }
        else if(level == 0) {
            return 1;
        }
        else{
            return count(t.left, level-1) + count(t.right, level-1);
         }

    }
}