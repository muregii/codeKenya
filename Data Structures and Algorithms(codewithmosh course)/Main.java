public class Main {

    public static void main(String[] args) {
        IsValidBST bstChecker = new IsValidBST();

        // Kubuild our tree
        bstChecker.root = bstChecker.new TreeNode(10);
        bstChecker.root.leftChild = bstChecker.new TreeNode(5);
        bstChecker.root.rightChild = bstChecker.new TreeNode(15);
        bstChecker.root.leftChild.leftChild = bstChecker.new TreeNode(5);
        bstChecker.root.leftChild.rightChild = bstChecker.new TreeNode(7);
        bstChecker.root.rightChild.rightChild = bstChecker.new TreeNode(18);

        // Testing kama tree yetu is indeed a valid binary tree
        boolean isValid = bstChecker.isValidBST();
        System.out.println("Is the tree a valid BST? " + isValid);
    }

    public static class IsValidBST{ //Hii static hapa ni muhimu ndio main method iweze kuload information iko kwa hii class

      private class TreeNode{
          
          private TreeNode leftChild;
          private TreeNode rightChild;
          private int info;
          
          public TreeNode(int info) {
              this.info = info;
          }
  
          @Override
          public String toString(){
              return "Node=" + info;
          }
          
      }
  
      private TreeNode root;
  
      public boolean isValidBST(){
  
          return isValidBST(root, Integer.MIN_VALUE, Integer.MAX_VALUE);
  
      }
  
      private boolean isValidBST(TreeNode root, int lefts, int rights){
          
          if(root == null) return true;
          
          if(root.info < lefts || root.info > rights) return false;
  
          return isValidBST(root.leftChild, lefts, root.info -1) && isValidBST(root.rightChild, root.info, rights);
  
      }
  }

}
