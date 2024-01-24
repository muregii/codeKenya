

public class MajorityElement {

    public int majorityElement(int[] nums) {
        Integer candidate = null;
        var count = 0;

        for(var num : nums){
            if(count == 0){
             candidate = num;
                
            }   
            count += (candidate == num) ? 1 : -1;
            
        }
        
        return candidate;
    }
}
