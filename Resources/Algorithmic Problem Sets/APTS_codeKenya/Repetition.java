public class Repetition {
    public int isRepetition(String str) {
        for (int i = 1; i <= str.length() / 2; i++) {
            String prefix = str.substring(0, i);
            if (str.length() % i == 0) {
                int repeatCount = str.length() / i;
                StringBuilder repeated = new StringBuilder();
                for (int j = 0; j < repeatCount; j++) {
                    repeated.append(prefix);
                }
                if (repeated.toString().equals(str)) {
                    return repeatCount;
                }
            }
        
     
        if (str.length() % prefix.length() == 0) {
            int repeatCount = str.length() / prefix.length();
            StringBuilder repeated = new StringBuilder();
            for (int j = 0; j < repeatCount; j++) {
                repeated.append(prefix);
            }
            if (repeated.toString().equals(str)) {
                return repeatCount;
            }
        }
        return -1;
    }
    }
  }