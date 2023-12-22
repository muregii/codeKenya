import java.util.*;

public class discussion implements Comparator<String> {
@Override
public int compare(String s1, String s2) {
    int lengthDiff = s1.length() - s2.length();
    if(lengthDiff != 0) {
        return lengthDiff;
    }

    int minLength = Math.min(s1.length(), s2.length());
    for(int i =0; i < minLength; i++) {
        int charDiff = (-1) * (s1.charAt(i) - s2.charAt(i));
        if(charDiff != 0) {
            return charDiff;
        } 
    }
    return 0;
}
public static void main(String[] args) {
String[] words = new String[]{"how", "now", "brown","cow","hmm"};
Arrays.sort(words, new discussion());
System.out.println(Arrays.toString(words));
 }
}