

public class AVL {
    private class AVLNode{
        private int height;
        private AVLNode leftChild;
        private AVLNode rightChild;
        private int info;

        public AVLNode(int info) {
            this.info = info;
        }

        @Override
        public String toString(){
            return "Value=" + this.info; 
        }
    }

    private AVLNode root;

    public void insert(int info) {
        root = insert(root, info);
    }

    private AVLNode insert(AVLNode root, int info){
        if(root == null)
         return new AVLNode(info);

         if(info < root.info)
            root.leftChild = insert(root.leftChild, info);
         else
            root.rightChild = insert(root.rightChild, info);
         
        root.height = Math.max(height(root.leftChild), height(root.rightChild)) + 1;


         if(isLeftHeavy(root)){
            if(balanceFactor(root.leftChild) < 0)
           root.leftChild = leftRotation(root.leftChild);  
           return rightRotation(root);
        }
             
        else if(isRightHeavy(root)){
            if(balanceFactor(root.rightChild) > 0)
            root.rightChild = rightRotation(root.rightChild);
            return leftRotation(root);
        }
        
        return root;
    }
   
    private int balanceFactor(AVLNode node){
        return (node == null) ? 0 : height(node.leftChild) - height(node.rightChild);
    }

    private boolean isLeftHeavy(AVLNode node){
        return balanceFactor(node) > 1;
    }
    private boolean isRightHeavy(AVLNode node){
         return balanceFactor(node) < -1;
    }

    private int height(AVLNode node){
        return (node == null) ? -1 : node.height;
    }
    
    private AVLNode rightRotation(AVLNode node){
        var newRoot = root.leftChild;
        root.leftChild =  newRoot.rightChild;
        newRoot.rightChild = root;

        setHeight(root);
        setHeight(newRoot);

        return newRoot;
    
     }
     private AVLNode leftRotation(AVLNode root){
        var newRoot =  root.rightChild;
        root.rightChild =  newRoot.leftChild;
        newRoot.leftChild =  root;

        setHeight(root);
        setHeight(newRoot);
        
        return newRoot;
    }

    
    
    private void setHeight(AVLNode node){
        root.height = Math.max(height(root.leftChild), height(root.rightChild) + 1);

    }
}