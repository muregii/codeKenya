public class DNAMaxNucleotide {
      public String max(String[] strands, String nuc) {
          if (nuc.length() == 0){
              return "";
          }
  
          String result = "";
          int DNA_length = 0;
          int cur_length = 0;
          int pos = 0;
  
          for (String DNA : strands){
              if (DNA.contains(nuc)){
                  pos = DNA.indexOf(nuc);
                  while (pos != -1) {
                      DNA_length += 1;
                      pos = DNA.indexOf(nuc, pos+1);
                  }
                  if (cur_length == 0 || (DNA_length > cur_length) || (DNA.length() > result.length() && DNA_length == cur_length)){
                      result = DNA;
                      cur_length = DNA_length;
                  }
              }
              DNA_length = 0;
          }
          return result;
    }
    public static void main(String[] args) {
      DNAMaxNucleotide obj = new DNAMaxNucleotide();
      String[] strands = {"agt", "aagt", "taattt", "ccatg"};
      String nuc = "a";
      String result = obj.max(strands, nuc);
      System.out.println(result);
    }
  }