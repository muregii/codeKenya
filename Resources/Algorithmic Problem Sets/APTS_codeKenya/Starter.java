import java.util.HashSet;

public class Starter {
    public int begins(String[] words, String first) {
        // replace this code
        if (words.length == 0) {
            return 0;
        }

        HashSet<String> result = new HashSet<>();
        int num = 0;
        for (String s: words) {
            if (s.startsWith(first)){
                if (!result.contains(s)) {
                    num += 1;
                    result.add(s);
                }
            }
        }
        return num;
    }
    public static void main(String[] args) {
        Starter obj = new Starter();
        String[] words = {"easy", "lies", "the", "head", "that", "wears", "yellow"};
        String first = "t";
        int result = obj.begins(words, first);
        System.out.println(result);
    }
}