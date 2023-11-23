import java.util.Stack;

public class StringReverser {
    public String reverse(String input){
        if(input == null)
        throw new IllegalArgumentException();
        Stack<Character> stack = new Stack <>();
        /*for(int i = 0; i < input.length(); i++)
        stack.push(input.charAt(i));*/

        for(char chr: input.toCharArray())
        stack.push(chr);

        StringBuffer reversed = new StringBuffer();
        while(!stack.isEmpty()){
        reversed.append(stack.pop());
        }return reversed.toString();
    }
 
}