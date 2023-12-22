public class Maps {
    public static void main(String [] args) {
        Map<Character, List<String>> myMap = new HashMap<>();
        String message = "the fox, the quick brown fox jumps";
        List<String> blankList = new ArrayList<>();
        int order = 3;
      
        for (int i=0; i<message.length(); i++) {
            char key = message.charAt(i);
            if (!myMap.containsKey(key)) {
                myMap.put(key, blankList);
            }
            myMap.get(key).add(message.substring(order, i+order));
        }
        System.out.println(myMap);
    }
 }