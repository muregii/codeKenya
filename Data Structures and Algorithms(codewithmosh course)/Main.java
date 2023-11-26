import java.util.Arrays;

public class Main{
  public static void main(String[] args) {
   int[] numbers = {4, 5, 6, 8, 9, 4};
   var sorter = new CountingSort();
   sorter.sort(numbers, 9);
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