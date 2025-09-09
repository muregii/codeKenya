
import java.util.*;

public class isValidSubsequence { //Wrapper to just remove the squiggles on VS code. There shouldn't be two pucblic classes here.

    //run program on algo expert
public class Program {
  public static boolean isValidSubsequence(
    List<Integer> array, List<Integer> sequence
  ) {
    // Write your code here.
  
    if (array.size() < sequence.size()) return false;

    for (int arrayNum : array){
        Integer sequenceNum = sequence.get(0);
      if (arrayNum == sequenceNum){
        sequence.remove(0);
      }
      if(sequence.size() == 0) return true;
  
    }
    return false;  
    
  } 
}
//End of algoexpert


}
