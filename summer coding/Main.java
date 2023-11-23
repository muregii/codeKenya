//import java.util.Arrays;

public class Main{
  public static void main(String[] args) {
   var graph = new WeightedGraph();
   graph.addNode("A");
   graph.addNode("B");
   graph.addNode("C");
   graph.addEdge("A","B",1);
   graph.addEdge("B","C",4);
   graph.addEdge("A","C", 10);

   var path = graph.getShortestPath("A", "C");

   //graph.print();
   
  //  var list = graph.topologicalSort();
  System.out.println(graph.hasCycle());
   //graph.print();
    
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