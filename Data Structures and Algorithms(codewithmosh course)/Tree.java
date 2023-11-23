import java.util.ArrayList;

public class Tree{
    
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
    
    public void insert(int info){
        if (root == null) {
            root = new TreeNode(info);
            return;
        } 

        var current = root;

        while(true){
            if(info < current.info){
                if(current.leftChild == null){
                    current.leftChild = new TreeNode(info);
                    break;
                }
                current = current.leftChild;
            }
            else{
                if(current.rightChild == null){
                current.rightChild = new TreeNode(info);
                break;

            }
            current = current.rightChild;
            
            }
        }
    }

    public boolean find(int info){
        var current = root;
        while(current != null){
            if(info < current.info)
            current =  current.leftChild;
            else if ( info > current.info)
            current = current.rightChild;
            else
            return true;
        }
       return false;
    }

    public void traversePreOrder(){
        traversePreOrder(root);
    }

    public void traverseInOrder(){
        traverseInOrder(root);
    }

    public void traversePostOrder(){
        traversePostOrder(root);
    }
   
    public int height(){
        return height(root);
    }

    public int min(){
        //minimum value of a binary search tree ( left most leaf) O(log n)
        if (root == null){
            throw new IllegalStateException();}
        
        var current = root;
        var last = current;
        while(current != null){
            last = current;
            current = current.leftChild;
        }
        return last.info;
    }

    private void traversePreOrder(TreeNode root){
        if(root == null) return;

        System.out.println(root.info);
        traversePreOrder(root.leftChild);
        traversePreOrder(root.rightChild);
    }

    private void traverseInOrder(TreeNode root){
        if(root == null) return;

        traverseInOrder(root.leftChild);
        System.out.println(root.info);
        traverseInOrder(root.rightChild);
    }

    private void traversePostOrder(TreeNode root){
        if(root == null) return;

        traversePostOrder(root.leftChild);
        traversePostOrder(root.rightChild);
        System.out.println(root);
    }

    private int height(TreeNode root) {
        if(root == null) return -1;
        if(root.leftChild == null && root.rightChild == null)
         return 0;
        
        return 1 + Math.max(height(root.leftChild), height(root.rightChild));
    }
// Minimum value of a Binary Tree (Not a binary Search tree) O(n)
   /*private int min(TreeNode root){
    if(root == null) {
        return Integer.MAX_VALUE;
    }

    int left = min(root.leftChild);
    int right = min(root.rightChild);

    return Math.min(Math.min(left, right), root.info);
   }*/

    public void remove(int value) {
        root = removeNode(root, value);
    }

    private TreeNode removeNode(TreeNode current, int value) {
        // Base case: If the current node is null, return null (not found)
        if (current == null) {
            return null;
        }

        // Recursively search for the node to remove in the left or right subtree
        if (value < current.info) {
            current.leftChild = removeNode(current.leftChild, value);
        } else if (value > current.info) {
            current.rightChild = removeNode(current.rightChild, value);
        } else {
            // Node to remove is found

            // Case 1: Node with no child or only one child
            if (current.leftChild == null) {
                return current.rightChild;
            } else if (current.rightChild == null) {
                return current.leftChild;
            }

            // Case 2: Node with two children
            // Find the inorder successor (the minimum value in the right subtree)
            current.info = findMinValue(current.rightChild);

            // Remove the inorder successor from the right subtree
            current.rightChild = removeNode(current.rightChild, current.info);
        }
        return current;
    }

    private int findMinValue(TreeNode node) {
        int minValue = node.info;
        while (node.leftChild != null) {
            minValue = node.leftChild.info;
            node = node.leftChild;
        }
        return minValue;
    }
    //Equality checking
    public boolean equals(Tree other){    
       return equals(root, other.root);
    }

    private boolean equals(TreeNode first, TreeNode second){
        if(first == null && second == null) return true;

        if(first != null && second != null)
            return first.info == second.info && equals(first.leftChild, second.leftChild) && equals(first.rightChild, second.rightChild);   
        return false;    
    }
    //Validating a Binary Search Tree
    public boolean isValidBST(){

        return isValidBST(root, Integer.MIN_VALUE, Integer.MAX_VALUE);
    }
    
    private boolean isValidBST(TreeNode root, int min, int max){
        if(root == null) return true;

        if(root.info < min || root.info > max) return false;

       return isValidBST(root.leftChild, min, root.info -1) && isValidBST(root.rightChild, root.info +1, max);
    }
    //root swap
    public void swapRoot(){


        var temp = root.leftChild;
        root.leftChild = root.rightChild;
        root.rightChild = temp;
    }
    //Node at K distance
    public ArrayList<Integer> getNodesAtDistance(int distance){
        var list = new ArrayList<Integer>();
        
        getNodesAtDistance(root, distance, list);
        return list;
    }

    private void getNodesAtDistance(TreeNode root, int distance, ArrayList<Integer> list){
        if(root == null) return;

        if(distance == 0){
            list.add(root.info);
           return;
        }

        getNodesAtDistance(root.leftChild, distance -1, list);
        getNodesAtDistance(root.rightChild, distance -1, list);
            

    }
    //level order traversal
    public void traverseLevelOrder(){
        if(root == null) throw new IllegalStateException();
        
    for(int i = 0; i <= height(); i++){
       var list =  getNodesAtDistance(i);
       for(var value : list)
       System.out.println(value);
    }
}

    //AVL Trees. (Balanced and Unbalanced trees. Self rebalancing trees)
    

    }

