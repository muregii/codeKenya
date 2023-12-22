import java.util.*;

//{1, 300 } ==> 301 . Return [0, 1]
public class twoSum{

    public int[] solution(int[] nums, int target){ 
        Map<Integer, Integer> numToIndex = new HashMap<>();
        for(int i = 0; i < nums.length; ++i) {
        if(numToIndex.containsKey(target - nums[i]))
        return new int[] {numToIndex.get(target - nums[i]), i};
      
        numToIndex.put(nums[i], i);
         
    }
    throw new IllegalArgumentException();
}

public static void main(String[] args) {
    twoSum obj = new twoSum();
    int[] nums = {2, 7, 11, 15};
    int target = 9;
    System.out.println(Arrays.toString(obj.solution(nums, target)));
    
  }
}