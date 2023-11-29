//I just so happened to have solved this while doing codewithmosh.
//You can find the solution to this challenge by copying this "Permalink" --:  https://github.com/muregii/codeKenya/blob/f40dfe514c29e30482bf2fec7c80ef23260660a9/Data%20Structures%20and%20Algorithms(codewithmosh%20course)/Tree.java#L194

    public class IsValidBST{

        private class TreeNode{
            
            private TreeNode leftChild;
            private TreeNode rightChild;
            private int info;
            
            private TreeNode(int info) {
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
            
            return isValidBST(root.leftChild, lefts, root.info) && isValidBST(root.rightChild, root.info, rights);
    
        }
    }
    
    

    
