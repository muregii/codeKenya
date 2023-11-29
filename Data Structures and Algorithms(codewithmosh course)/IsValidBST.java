//I just so happened to have solved this while doing codewithmosh.
//You can find the solution to this challenge by copying this "Permalink" --:  https://github.com/muregii/codeKenya/blob/f40dfe514c29e30482bf2fec7c80ef23260660a9/Data%20Structures%20and%20Algorithms(codewithmosh%20course)/Tree.java#L194
//Anyway ... Acha ni re-do hapa for Day 1's sake ya hii challenge yetu

//first of all: you need a public and private method. 




    public class IsValidBST{
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
            //juu tunasolve recursively, unahitaji base condition ndo recursion iterminate / avoid infinite loop
            if(root == null) return true;
            //Condition 1: ni kama root node yetu inabeba a value less than node iko to its left(Juu it should be bigger than the left child) au value kubwa kuliko node iko to it's right(Juu haifai kukua value kubwa kuliko ya right) method inafaa kureturn false.
            if(root.info < lefts || root.info > rights) return false;
    
            return isValidBST(root.leftChild, lefts, root.info -1) && isValidBST(root.rightChild, root.info, rights);
    
        }
    }
    

    
