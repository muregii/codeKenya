//package codeK(main).100 Day Challenge.Day 13;

public class URLify {
    public StringBuilder url(String s){
        StringBuilder bld = new StringBuilder(); //Strings are immutable in Java. As in, huezi edit the original, you have to recreate a copy somewhere. 
     
        for(int i = 0; i < s.length(); i++){
          if(s.charAt(i) != ' '){
             bld.append(s.toLowerCase().charAt(i));
          }else{
            bld.append("%20");
          }         
        }
       return bld; 
    }
    public StringBuilder url1(String s){
       
         StringBuilder bld = new StringBuilder(); //Strings are immutable in Java. As in, huezi edit the original, you have to recreate a copy somewhere. 
         int[] letters = new int[128];
        var chars = s.toLowerCase().toCharArray();
        for(int i =  0 ; i < chars.length;i++){
            if(chars[i] == 32){
                bld.append("%20");
            }else{
                 bld.append(chars[i]);
            }
           
        }
       

        return bld;
        
      
    }

    public static void main(String[] args){
        URLify test = new URLify();
        String s = "One a month foundation";
        StringBuilder answer =  test.url(s);
        System.out.println("URL of the string is: " + answer);
    }
}
