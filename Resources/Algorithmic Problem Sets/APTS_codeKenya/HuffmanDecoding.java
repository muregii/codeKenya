

public class HuffmanDecoding {

    public String decode(String archive, String[] dictionary) {
        // fill in code here...
        StringBuilder result = new StringBuilder();
        int i = 0;
        int j = 1;       
        while(j<=archive.length()){
            String curr = archive.substring(i, j);
            int index = getIndex(dictionary, curr);

            if(index>=0){
                result.append((char) ('A' + index));
                i = j;
                j = i + 1;
                
            } else {
                j++;
            }
           

        }

        
        return result.toString();
    }
    //helper method
    private int getIndex(String [] dictionary, String s) {


        for(int i = 0; i<dictionary.length; ++i) {
            if(dictionary[i].equals(s)){
                return i;
            }
        }

        return -1;

    }
    
    public static void main(String[] args) {
        HuffmanDecoding obj = new HuffmanDecoding();
        String archive = "101010";
        String[] dictionary = {"10", "11", "00", "01"};
        String decodedMessage = obj.decode(archive, dictionary);
        System.out.println(decodedMessage);

    }

 }