import java.util.*;

public class HashTaggery {

    public static String maxTag(String[] tags, String[] messages) {
        Set<String> hashtags = new HashSet<>();
        for (String tag : tags) {
            if (tag.startsWith("#")) {
                hashtags.add(tag.toLowerCase());
            }
        }
        
        int count = 0;
        for (String message : messages) {
            String[] words = message.split("\\s+");
            for (String word : words) {
                if (hashtags.contains(word.toLowerCase())) {
                    count++;
                    break;
                }
            }
        }
        
        if (count >= 0.75 * messages.length) {
            return "tagged";
        } else {
            return "missed";
        }
    }
    
    
    
}
