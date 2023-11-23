import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.Stack;
import java.util.Queue;


public class Graphs{

    private class Node {
        private String label;


        public Node(String label) {
            this.label = label;
        }

        @Override
        public String toString(){
            return label;
        }

    }

    private Map<String, Node> nodes = new HashMap<>();
    private Map<Node, List<Node>> adjacencyList = new HashMap<>();
       

        public void addNode(String label){
            var node =  new Node(label);
            nodes.putIfAbsent(label, node);
             adjacencyList.putIfAbsent(node, new ArrayList<>());
        
        }


        public void addEdge(String from, String to){
            var fromNode = nodes.get(from);
            if(fromNode == null)
                throw new IllegalArgumentException();

            var toNode = nodes.get(to);
            if(toNode == null)
                throw new IllegalArgumentException();

            adjacencyList.get(fromNode).add(toNode);

        }

        public void print(){
            for(var source : adjacencyList.keySet()) {
                var targets = adjacencyList.get(source);

                if(!targets.isEmpty())
                System.out.println(source +  " is connected to " + targets);
            }
        }


        public void removeNode(String label){
            var node = nodes.get(label);
            if(node == null)
            return;
            
            for(var n : adjacencyList.keySet()) 
                adjacencyList.get(n).remove(node);
            adjacencyList.remove(node);
            nodes.remove(node);            
        }

        public void removeEdge(String from, String to){
            var fromNode = nodes.get(from);
            var toNode = nodes.get(to);

            if(fromNode == null || toNode == null)
            return;

            adjacencyList.get(fromNode).remove(toNode);
        }


        //DFS using recursion
        public void traverseDepthFirstRecursively(String root){
            var node = nodes.get(root);
            if(node == null) return;

            traverseDepthFirstRecursively(node, new HashSet<>());

        }

        //Stack Data Structure -- Set Data Structure for this Implementation
        private void traverseDepthFirstRecursively(Node root, Set<Node> visited){
            System.out.println(root);
            visited.add(root);

            for(var node : adjacencyList.get(root)) //for each loop. Visit all neighbours of the root node. Return a list object from adjacency list
            if(!visited.contains(node))
            traverseDepthFirstRecursively(node, visited);

        }

        //DFS using Iteration
        //push(root)
        //while(!stack.isEmpty())
        //current.pop()
        //visited(current)
        public void traverseDepthFirst(String root){
            var node = nodes.get(root);
            if(node == null) return;

            Set<Node> visited = new HashSet<>();
            Stack<Node> stck = new Stack<>();
            stck.push(node);

            while(!stck.isEmpty()){
                var current = stck.pop();

                if(visited.contains(current))
                continue;

            System.out.println(current);
            visited.add(current);

            for(var neighbour : adjacencyList.get(current))
            if(!visited.contains(neighbour))
            stck.push(neighbour);
            
            }

        }

        //BFS Trsaversal using a Queue
        public void traverseBreadthFirst(String root){
                var node = nodes.get(root);
                if(node == null) return;

                Set<Node> visited = new HashSet<>();
                Queue<Node> queue = new ArrayDeque<>();
                queue.add(node);

                while(!queue.isEmpty()){
                    var current = queue.remove();

                    if(visited.contains(current))
                    continue;

                System.out.println(current);
                visited.add(current);

                for(var neighbour : adjacencyList.get(current))
                if(!visited.contains(neighbour))
                queue.add(neighbour);
                }


        }

        public List<String> topologicalSort(){
            Stack<Node> stack = new Stack<>();
            Set<Node> visited = new HashSet<>();

            for(var node : nodes.values())
            topologicalSort(node, visited, stack);

            List<String> sorted = new ArrayList<>();
            while(!stack.isEmpty())
            sorted.add(stack.pop().label);

            return sorted;

            }

        
        private void topologicalSort(Node node, Set<Node> visited, Stack<Node> stack){
            if(visited.contains(node)) return;

            visited.add(node);

            for(var neighbour : adjacencyList.get(node))
            topologicalSort(neighbour, visited, stack);

        stack.push(node);

        }

        public boolean hasCycle(){ //Adding the method
            //We need three sets
            Set<Node> all = new HashSet<>();
            all.addAll(nodes.values());//Adding all nodes
            Set<Node> visiting = new HashSet<>();
            Set<Node> visited = new HashSet<>();

            //Picking a node from the first set to kickstart traversal
            while(!all.isEmpty()) {  //while the first node, all still has things/nodes
                var current = all.iterator().next(); /* Every collection in Java has an iterator, we use iterator to iterate over an object,
                This iterator object has a method called next(), which will return the next Object that is available for being read.
                We are using this to pick an object from the first set. You could use all])[0] (Sets don't have a methos for getting an item by index, 
                so this code converts that set to an array and then pick the first item. We pass Node to return an Array of nodes to match the type 
                passed on our private method)*/ 


                if(hasCycle(current, all, visiting, visited)) return true;//Calling our private recursive method.
            }
            return false;

        }
        //implementing a DFS using our private helper/recursive method
        private boolean hasCycle(Node node,Set<Node> all, Set<Node> visiting, Set<Node> visited ){ //this method takes a node and the three sets as parameters
            //moving the node from the first set to the second set
            all.remove(node);
            visiting.add(node);

            for(var neighbour : adjacencyList.get(node)){ //visiting all the neighbours of the node
                if(visited.contains(neighbour)) //if you've visited this neighbour, we're going to continue
                continue;

                if(visiting.contains(neighbour)) // if the node is contained in visiting, we return true, YES there's a cycle.
                return true;

              //Otherwise we'll recursively call this method and visit this neighbour
                if(hasCycle(neighbour, all, visiting, visited)) return true;
            }
            visiting.remove(node); // finally remove the node from the visiting Set 
            visited.add(node);// And add the node to the visited set.
            return false; // if the conditions are not true, there is NO cycle, so return false.
        }


        




       
}