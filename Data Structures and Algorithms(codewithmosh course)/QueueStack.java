import java.util.EmptyStackException;
import java.util.Stack;

public class QueueStack{
    //Q
    //S1 enqueue
    //S2 dequeue
    private Stack<Integer> stack1 = new Stack<>();
    private Stack<Integer> stack2 = new Stack<>();
    //O(1)
    public void enqueue(int item){
        stack1.push(item);
    }
    //O(n)
    public int dequeue(){
        if(stack1.isEmpty() && stack2.isEmpty())
        throw new EmptyStackException();
        
        MoveStack1ToStack2();
        return stack2.pop();
    }

    public int peek(){
        if(stack1.isEmpty() && stack2.isEmpty())
        throw new EmptyStackException();
        
        MoveStack1ToStack2();
        return stack2.peek();
    }
    private void MoveStack1ToStack2() {
        if(stack2.empty())
        while(!stack1.isEmpty())
        stack2.push(stack1.pop());
    }

    public boolean isEmpty(){
        return (stack1.isEmpty() && stack2.isEmpty());
    }
}