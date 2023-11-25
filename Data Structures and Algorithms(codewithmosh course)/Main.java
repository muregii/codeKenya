import java.util.Arrays;

public class Main{
  public static void main(String[] args) {
   int[] numbers = {8, 7 , 6, 5, 4, 3, 2, 1};
   var sorter = new SelectionSort();
   sorter.sort(numbers);
   System.out.println(Arrays.toString(numbers));
    
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