import java.util.*;

public class LeafTrails {

    public class Leaf{
        int val;
        String path;

        Leaf(int val, String path){
            this.val = val;
            this.path = path;
        }

        public int getVal(){
            return val;
        }
    }

    public String[] trails(TreeNode tree) {
        // replace with working code
        List<Leaf> binary = new ArrayList<>();
        getLeaves(tree, "", binary);
        Collections.sort(binary, Comparator.comparing(Leaf::getVal));

        String[] paths = new String [binary.size()];
        for(int i = 0; i < binary.size(); ++i) {
            paths[i] = binary.get(i).path;
        }
        return paths;
    }

    private void getLeaves(TreeNode tree, String path,  List <LeafTrails.Leaf> binary ) {
       
        if(tree == null){
            return;
        }

        if(tree.left == null && tree.right == null) {
            binary.add(new Leaf(tree.info, path));
        }
        getLeaves(tree.left, path +"0", binary);
        getLeaves(tree.right, path +"1", binary);
        
        }
        

 }

