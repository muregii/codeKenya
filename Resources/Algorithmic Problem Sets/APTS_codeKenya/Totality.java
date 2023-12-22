
public class Totality {
    public int sum(int[] a, String stype) {
        // you add code here
        int val = 0;
        switch(stype) {
            case "even":
            for(int i = 0; i < a.length; i+=2) {
                val+=a[i];
            }
            break;

            case "odd":
            for(int i = 1; i < a.length; i+=2 ) {
                val+=a[i];
            }
            break;

            default:
            for(int i = 0; i < a.length; i++) {
                val+=a[i];
            }
        }
        return val;
    }
    //psvm 
    public static void main(String[] args) {
        Totality obj = new Totality();
        int[] a = {1,2,3,4,5};
        String stype = "";
        int result = obj.sum(a, stype);
        System.out.println(result);
    }
}