    class Solution {
    public int minOperations(String s){
        
      return  Math.min(countOps(s, '0'), countOps(s, '1'));
    }

     private int countOps(String s, char ch){
        int count = 0;
        var currentChar = s.toCharArray();
        for(int i = 0; i < s.length(); i++){
            if(currentChar[i] != ch){
                count++;
            }

            if(ch == '0'){
                ch = '1';
            }else{
                ch = '0';
            }

            
        }
        return count;

    }

}