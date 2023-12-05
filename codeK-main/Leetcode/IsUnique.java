import java.util.HashMap;
import java.util.Map;

public class IsUnique{
    public boolean isUnique(String string){
        var count  = 0;
        Map<Character, Integer> map = new HashMap<>();
        var str = string.toCharArray();
        for(var ch : str){
            if(map.containsKey(ch)) return false;
        
        map.put(ch, count);

    }
    if(count > 1) return false;
    return true;
    }
}