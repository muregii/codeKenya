
public class PairDown {
    public int [] fold (int[] list) {
        int x = (int) Math.floor((list.length+1)/2);
        int[] sum = new int[x];

        for(int i=0;i<list.length;i+=2) {
            if(i==list.length-1){
                sum[(int) (i/2)] = list[i];
            }
            else{
                sum[(int) (i/2)] = list[i] + list[i+1]; 
            }
        }
        


        return sum;
    }
}