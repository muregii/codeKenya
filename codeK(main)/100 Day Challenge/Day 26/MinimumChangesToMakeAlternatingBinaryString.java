//Hii ndio  tunaita dynamic programming sasa. One of the forms.

public class MinimumChangesToMakeAlternatingBinaryString {
    
    public int minOperations(String s){
        return  Math.min(countOps(s, '0'), countOps(s, '1'));
      }
  
       private int countOps(String s, char ch){
          var count = 0;
          var stringArray = s.toCharArray();
          for(int i = 0; i < stringArray.length; i++){
              if(stringArray[i] != ch){
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
