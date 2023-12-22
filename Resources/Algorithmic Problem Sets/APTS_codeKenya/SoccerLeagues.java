
public class SoccerLeagues{
    public int[] points(String[] matches){
        int[] yourScore = new int[matches.length];
        
        for(int i=0;i<matches.length;i++) {
            for(int j=0;j<matches[i].length();j++) {
                switch(matches[i].substring(j, j+1)) {
                    case "W":
                    yourScore[i] +=3;
                    break;
                    case "D":
                    yourScore[i] +=1;
                    yourScore[j] +=1;
                    break;
                    case "L":
                    yourScore[j] += 3;
                    break;
                }
            }
        }
        return yourScore;
    }
    
}

