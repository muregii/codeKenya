

public class MinimumChangesToMakeAlternatingBinaryString {
    
    public int minOperations(String s){
      return  Math.min(count(s, '0'), count(s, '1'));
    }
    
     private int count(String s, char ch){
        var count = 0;
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
