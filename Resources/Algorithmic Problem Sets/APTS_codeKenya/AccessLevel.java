
public class AccessLevel {
    public String canAccess(int[] rights, int minPermission) {
           // fill in code here
    String s = "";

    for(int i: rights) {
       s+= (i < minPermission) ? 'D' : 'A';
    }
    return s;   
}
    public static void main(String[] args) {
        AccessLevel obj = new AccessLevel();
        int[] rights = {0,1,2,3,4,5};
        int minPermission = 2;
        System.out.println(obj.canAccess(rights, minPermission));
    }
}
