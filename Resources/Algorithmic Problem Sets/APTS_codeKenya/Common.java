import java.util.HashMap;

public class Common {
    public int count(String a, String b) {
        int num = 0;
        String idx;
        HashMap<String, Integer> result = new HashMap<>();
        for (int i = 0; i < a.length(); i++) {
            idx = a.substring(i, i + 1);
            if (result.containsKey(idx)) {
                result.replace(idx, result.get(idx) + 1);
            } else {
                result.put(idx, 1);
            }
        }

        for (int i = 0; i < b.length(); i++) {
            idx = b.substring(i, i + 1);
            if (result.containsKey(idx)) {
                if (result.get(idx) > 0) {
                    num += 1;
                    result.replace(idx, result.get(idx) - 1);
                }
            }
        }

        return num;
    }
}
