


  public class Main {

    public static void main(String[] args) {
        
        IsValidBST treeTester = new IsValidBST();

        // Manually constructing a binary tree
        treeTester.root = treeTester.new TreeNode(10);

        treeTester.root.leftChild = treeTester.new TreeNode(5);
        treeTester.root.rightChild = treeTester.new TreeNode(15);
        treeTester.root.leftChild.leftChild = treeTester.new TreeNode(3);
        treeTester.root.leftChild.rightChild = treeTester.new TreeNode(7);
        treeTester.root.rightChild.rightChild = treeTester.new TreeNode(18);

        // Testing if the tree is a valid BST
        boolean result = treeTester.isValidBST();
        System.out.println("Is the tree a valid BST? " + result);
    }

    
}
