
import java.util.*;

public class StringUtilities {

    
    //Counting the number of vowels
    public static int vowels(String s){
         int count = 0;
         Set<Character> vow = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u'));
         
         for(var i = 0 ; i < s.length(); i++){
             char character = s.toLowerCase().charAt(i);
             if(vow.contains(character))
             count++;
            }
            return count;
        }

        public static int countVowels(String str){
            if(str == null)
            return 0;
            
            int count = 0;
            String vowels = "aeiou";
            for(var ch : str.toLowerCase().toCharArray())
            if(vowels.contains(Character.toString(ch)))
            count++;

            return count;
        }
        
        //Reversing a String #1
        public static String reverse(String s){
            if(s == null) return "";
            StringBuilder rev = new StringBuilder(); //Useful for creating a sort of mutable string
            for(int i = s.length()-1; i >= 0; i--){
                rev.append(s.charAt(i));
            }
            return rev.toString();
        }

        //Reversing a String
        public static String reverseQuadraticGrowth(String str){
            String reversed = "";
            for(var i = str.length(); i >= 0; i--) //O(n)
                reversed += str.charAt(i); //Concatenating grwos linearly O(n) --> O(n^2)
                
            return reversed;
            

        }


        //Solution #1
        public static String reverseSentence(String sentence){
            String[] words = sentence.split(" ");
            StringBuilder rev = new StringBuilder();
            
            for(var i = words.length-1; i>= 0; i--){
                rev.append(words[i] + " ");

            }
            return rev.toString().trim();
        }

        //Solution #2
        public static String reverseSentenceArray(String sentence){
            if(sentence == null) return "_";
            String[] words = sentence.trim().split(" ");
            Collections.reverse(Arrays.asList(words));
            return String.join(" ", words);

            
            
    }
    //Are Rotations ABCD DABC CDAB BCDA ABCD
    public static boolean areRotations(String str1, String str2) {
        if(str1 == null || str2 == null) return false;
        return (str1.length() == str2.length() && (str1 + str2).contains(str2));
        
    }

    //Remove Duplicates
    public static String removeDuplicates(String str) {
        if(str == null) return " ";  // check for a null input
        StringBuilder output = new StringBuilder(); //Mahali tutastore output
        Set<Character> seen = new HashSet<>();
        for(var ch : str.toCharArray()){
            if(!seen.contains(ch)){
                seen.add(ch);
                output.append(ch);
            }
        }
        return output.toString();

    }

    public static char getMaxOccurringChar(String str){
        Map<Character, Integer> frequency = new HashMap<>();
        for(var ch : str.toCharArray()){
            if(frequency.containsKey(ch))
            frequency.replace(ch, frequency.get(ch) + 1);
            else
            frequency.put(ch, 1);
        }

    char maxChar = ' ';
    int maxCount = 0;
    for (Map.Entry<Character, Integer> entry : frequency.entrySet()) {
        if (entry.getValue() > maxCount) {
            maxCount = entry.getValue();
            maxChar = entry.getKey();
        }
    }

    return maxChar;
     
        /* OR

        //ASCII
        final int ASCII_SIZE = 256;
        int[] frequencies = new int [ASCII_SIZE];
        for(var ch: str.toCharArray())
        frequencies[ch]++;

        int max = 0;
        char result = ' ';
        for(var i = 0; i < frequencies.length; i++){
            if(frequencies[i] > max){
            max = frequencies[i];
            result = (char)i;
        }
    }
    return result;
    }*/
    }

    public static String capitalize(String sentence){
        if(sentence == null || sentence.trim().isEmpty()) return " ";

        String[] words = sentence.trim()
                        .replaceAll(" +", " ")
                        .split(" ");
        for(var i = 0; i < words.length; i++){
           words[i] = words[i].substring(0, 1).toUpperCase() + words[i].substring(1). toLowerCase();

        }
        return String.join(" ", words);

    }

    //ANAGRAM'S OF EACH OTHER 
    //O(n log n)
    //for e.g   ABCd - CBDA are anagrams
    public static boolean areAnagrams(String first, String second){
        if(first == null || second == null || first.length() != second.length()) return false;

        var array1 = first.toLowerCase().toCharArray();
        Arrays.sort(array1);

        var array2 = second.toLowerCase().toCharArray();
        Arrays.sort(array2);

        return Arrays.equals(array1, array2);
    }

    //ANAGRAMS APPROACH #2
    //O(n)
    public static boolean areAnagrams2(String first, String second){

        if(first == null || second == null) return false;

        final int ENGLISH_ALPHABET = 26;
        int[] freq = new int[ENGLISH_ALPHABET];

        first = first.toLowerCase();
        for(var i = 0; i < first.length(); i++){
            freq[first.charAt(i) - 'a']++;

        }

         second = second.toLowerCase();
        for(var i = 0; i < second.length(); i++){
            if(freq[second.charAt(i) - 'a'] == 0) return false;
            freq[second.charAt(i) - 'a']--;

    }
    return true;
}

//PALINDROME 
//ABBA is palindromic
public static boolean isPalindrome(String word){

    if(word == null) return false;

    var left = 0;
    var right = word.length()-1;

    while(left < right-1)
        if(word.charAt(left++) != word.charAt(right--))
        return false;
    
    return true;

    /*var input = new StringBuilder(word);
    input.reverse();
    return input.toString().equals(word);
    */
}

    public static int factorial(int n){
    
    var factorial = 1;
    for(var i = n; i > 1; i--){
      factorial *= i;
    }
    return factorial;
  }

  public static int factorialRecursively(int n){
    if(n == 0) return 1;
    return n * factorialRecursively(n-1);
  }
}
    