

public class Main{
  public static void main(String[] args) {
   int[] numbers = { };
   var search = new Search();
   var index = search.ternarySearch(numbers, 4);
   System.out.println(index);
    
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