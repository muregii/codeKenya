

import java.util.Arrays;
import java.util.List;
import java.util.Stack;

public class BalancedExpressions{

    private final List<Character> leftBrackets = Arrays.asList('(','<' ,'[','{');
    private final List<Character> rightBrackets = Arrays.asList(')','>',']','}');

    public boolean balanced(String input){
        Stack<Character> stck = new Stack<>();
        
        for(char chr : input.toCharArray()){
            if(isLeftBrackets(chr))
            stck.push(chr);
            
            if(isRightBrackets(chr)){
                if(stck.empty()) return false;

                var top = stck.pop();
                if(!bracketsMatch(top, chr)) return false;   
            }          
        }
        return stck.empty();
        
    }

    private boolean isLeftBrackets(char chr){
        //var leftBrackets = Arrays.asList('(', '<','[','{');
    return leftBrackets.contains(chr);
  
    }


    private boolean isRightBrackets(char chr){
    return rightBrackets.contains(chr);
    } 

    private boolean bracketsMatch(char left, char right){
    return leftBrackets.indexOf(left) == rightBrackets.indexOf(right);
    /*return 
    (right == ')' && left != '(') ||
    (right == '>' && left != '<') ||
    (right == ']' && left != '[') ||
    (right == '}' && left != '{');*/
    }
   

}