import java.util.HashSet;

public class FriendScore{
    public int highestScore(String[] friends) {
        int count = 0;

        for (int i=0; i < friends.length; i++) {
            HashSet<Integer> val = new HashSet<>();
            for (int j=0;j<friends[i].length();j++) {
            if (friends[i].substring(j,j+1).equals("Y")) {
                val.add(j);
                Loop(val, j, friends);
            }
        }
        if (val.contains(i)) {
            val.remove(i);
        }

        count = Math.max(count, val.size());
    }

        return count;
    }

     
    public void Loop(HashSet<Integer> val, int idx, String[] friends) {
        for (int i = 0; i < friends[idx].length(); i++) {
            if (friends[idx].substring(i, i + 1).equals("Y"))
                val.add(i);
        }
    }
    
}  