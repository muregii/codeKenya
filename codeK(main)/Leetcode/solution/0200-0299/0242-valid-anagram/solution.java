class Solution {
    public boolean isAnagram(String s, String t) {
    
    int[] letters = new int[128];

    for(int i = 0; i < s.length(); i++){
        letters[s.charAt(i) - 'a']++;
        
    }
    for(int i = 0; i < t.length(); i++){
        letters[t.charAt(i) - 'a']--;
    }

    for(var ch : letters){
        if(ch != 0 ) return false;
    }

    return true;
        
    }
    
}