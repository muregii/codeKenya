
public class MinimumChangesToMakeAlternatingBinaryString {
    public int minOperations(String s) {
        //1100
        //0000
      //This code passes 31/89 test cases
        var count = 0;
        var right = s.length()-1;
        var chars = s.toCharArray();

        for(int i = 1; i <= right; i+=2){
            
            if(chars[i] == chars[i-1]){
                count++;
            }
           
             
        }
        
        return count;
    }
}
