
public class CirclesCountry {
    public int leastBorders(int[] x, int[] y, int[] r, int x1, int y1, int x2, int y2) {
        int crosses = 0;
        // you write code here
        for(int k = 0; k<x.length; k++){
            if(isInside(x1, y1, x[k], y[k], r[k]) && ! isInside(x2, y2, x[k], y[k], r[k])){
                crosses+=1;
            }
            else if (isInside(x2, y2, x[k], y[k], r[k]) ^ isInside(x1, y1, x[k], y[k], r[k])) {
                crosses++;
            }
        }
        return crosses;
    }

    //helper method
    public boolean isInside(int x, int y, int cx, int cy, int r){
        double dist = (x - cx)*(x - cx) + (y - cy) * (y - cy);
        // (x^2 + y^2) = r^2
        double radSquared = r*r;
        return dist < radSquared;
    }

    public static void main(String[] args) {
        int[] x = {0, 0, 5};
        int[] y = {0, 0, 0};
        int[] r = {3, 4, 5};
        int x1 = -5;
        int y1 = 0;
        int x2 = 5;
        int y2 = 0;
        CirclesCountry cc = new CirclesCountry();
        int crosses = cc.leastBorders(x, y, r, x1, y1, x2, y2);
        System.out.println(crosses);
    }
    
    
 }