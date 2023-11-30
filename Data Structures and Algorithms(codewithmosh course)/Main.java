public class Main {

    public static void main(String[] args) {
        //IsValidBST bstChecker = new IsValidBST();
        IsValidBST test = new IsValidBST();

        test.root = test.new TreeNode(10);
        test.root.leftChild = test.new TreeNode(5);
        test.root.rightChild = test.new TreeNode(15);
        test.root.leftChild.leftChild = test.new TreeNode(5);
        test.root.leftChild.rightChild = test.new TreeNode(7);
        test.root.rightChild.rightChild = test.new TreeNode(15);

        var answer = test.isValidBST();
        System.out.println("Is the tree a valid BST? " + answer);

    }

    public static class IsValidBST{

        private class TreeNode{
            private TreeNode leftChild;
            private TreeNode rightChild;

            private int info;

            public TreeNode(int info) {
                this.info = info;
            }

            @Override
            public String toString(){
                return "Node =" + info;
            }

        }

        private TreeNode root;

        public boolean isValidBST(){
            return isValidBST(root, Integer.MIN_VALUE, Integer.MAX_VALUE );
        }

        private boolean isValidBST(TreeNode root, int lefts, int rights){
            if(root == null) return true;

            if(root.info < lefts || root.info > rights) return false;

            return isValidBST(root.leftChild, lefts, root.info-1) && isValidBST(root.rightChild, root.info, rights);
        }
    }
  

}
