import java.util.Map;
import java.util.Set;
import java.util.HashMap;
import java.util.HashSet;

public class CharFinder{
    public char nonRepeatingCharacter(String str){
        // a  green  apple
        Map<Character, Integer> map = new HashMap<>();

        var characters = str.toCharArray();
        for(var chr : str.toCharArray()){
            var count = map.containsKey(chr) ? map.get(chr) : 0;
            map.put(chr, count + 1);
        }
        for(var chr : characters)
        if(map.get(chr) == 1)
        return chr;
        
        return Character.MIN_VALUE;

    }

    public char repeatingCharacter(String str) {
       /*  Map<Character, Integer> map = new HashMap<>();
        var characters = str.toCharArray();

        for(var chr : characters){
            var count = map.containsKey(chr) ? map.get(chr) : 0;
            map.put(chr, count + 1);

        }
        for(var chr : characters)
        if(map.get(chr) > 1)
        return chr;
        
        return Character.MIN_VALUE;*/
        Set<Character> set = new HashSet<>();

        for(var chr: str.toCharArray()){
            if(set.contains(chr))
            return chr;

            set.add(chr);
        }
        return Character.MIN_VALUE;

    }
}