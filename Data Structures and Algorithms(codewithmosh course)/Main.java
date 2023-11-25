//import java.util.Arrays;

public class Main{
  public static void main(String[] args) {
   var graph = new WeightedGraph();
   graph.addNode("A");
   graph.addNode("B");
   graph.addNode("C");
   graph.addNode("D");
   graph.addEdge("A","B",3);
   graph.addEdge("B","D",4);
   graph.addEdge("C","D",5);
   graph.addEdge("A", "C", 1);
   graph.addEdge("B","C", 2);
   var tree = graph.getMinimumSpanningTree();
   tree.print();

   //var path = graph.getShortestPath("A", "C");

   //graph.print();
   
  //  var list = graph.topologicalSort();
  //System.out.println(graph.hasCycle());
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