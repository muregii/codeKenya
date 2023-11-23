public class AVLTree {
    private class AVLNode{
        private int info;
        private AVLNode leftChild;
        private AVLNode rightChild;

        public AVLNode (int info){
            this.info = info;
        }

        @Override
        public String toString(){
            return "Value=" + this.info;
        }
    }

    private AVLNode root;

    public void insert(int info){
        root = insert(root, info);
    }

    private AVLNode insert(AVLNode root, int info){
        if(root == null) 
        return new AVLNode(info);

        if(info < root.info)
        insert(root.leftChild, info);
        else
        insert(root.rightChild, info);

    
        return root;
    }


}