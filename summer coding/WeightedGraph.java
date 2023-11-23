import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Set;
import java.util.Stack;

public class WeightedGraph{
    private class Node {
        private String label;
        private List<Edge> edges =  new ArrayList<>();

        public Node(String label) {
            this.label = label;
        }


        @Override
        public String toString(){
            return label;
        }
        public void addEdge(Node to, int weight){
            edges.add(new Edge(this, to, weight));

        }
        public List<Edge> getEdges(){
            return edges;
        }

    }


    private class Edge{
        private Node from;
        private Node to;
        private int weight;

        public Edge(WeightedGraph.Node from, WeightedGraph.Node to, int weight) {
            this.from = from;
            this.to = to;
            this.weight = weight;
        }

        @Override
        public String toString(){
            return from + "->" + to;
        }
    }

    private Map<String, Node> nodes = new HashMap<>();
    //private Map<Node, List<Edge>> adjacencyList = new HashMap<>();

    public void addNode(String label){
        //var node = new Node(label);
        nodes.putIfAbsent(label, new Node(label));
        //adjacencyList.putIfAbsent(node, new ArrayList<>());
    }

    public void addEdge(String from, String to, int weight){
        var fromNode = nodes.get(from);
       if(fromNode == null)
        throw new IllegalArgumentException("The Origin node of the edge you entered is null");

        var toNode = nodes.get(to);
        if(toNode == null)
        throw new IllegalArgumentException("Destination node is currently null");

        fromNode.addEdge(toNode, weight);
        toNode.addEdge(fromNode, weight);

       // adjacencyList.get(fromNode).add(new Edge(fromNode, toNode, weight));
       // adjacencyList.get(toNode).add(new Edge(toNode, fromNode, weight));

    }
    public void print(){
        for(var node : nodes.values()) {
            var edges = node.getEdges();

            if(!edges.isEmpty())
            System.out.println(node +  " is connected to " + edges);
        }
    }

    private class NodeEntry{
        private Node node;
        private int priority;

        public NodeEntry(WeightedGraph.Node node, int priority) {
            this.node = node;
            this.priority = priority;
        }



    }
    
    //Solution to Shortest Distance
    public int getShortestDistance(String from, String to){
        var fromNode = nodes.get(from);

        Map<Node, Integer> distances = new HashMap<>();

        for(var node : nodes.values())
            distances.put(node, Integer.MAX_VALUE);
        distances.replace(fromNode, 0);

        Set<Node> visited = new HashSet<>();

        PriorityQueue<NodeEntry> queue = new PriorityQueue<>(Comparator.comparingInt(x -> x.priority));

        queue.add(new NodeEntry(fromNode, 0));

        while(!queue.isEmpty()){
            var current = queue.remove().node;
            visited.add(current);

            for(var edge : current.getEdges()){
                if(visited.contains(edge.to))
                    continue;
                    var newDistance = distances.get(current) + edge.weight;


                    if(newDistance < distances.get(edge.to)){
                        distances.replace(edge.to, newDistance);
                        queue.add(new NodeEntry(edge.to, newDistance)); 
                    }
                }

            }

        return distances.get(nodes.get(to));
    }

    //Solution to Shortest Path
    public Path getShortestPath(String from, String to){
        var fromNode = nodes.get(from);
        if(fromNode == null) throw new IllegalArgumentException();
        var toNode = nodes.get(to);
        if(toNode == null) throw new IllegalArgumentException();

        Map<Node, Integer> distances = new HashMap<>();
        
        for(var node : nodes.values())
        distances.put(node, Integer.MAX_VALUE);
        distances.replace(fromNode, 0);
        
        Map<Node, Node> previousNodes = new HashMap<>();

        Set<Node> visited = new HashSet<>();

        PriorityQueue<NodeEntry> queue = new PriorityQueue<>(Comparator.comparingInt(x -> x.priority));

        queue.add(new NodeEntry(fromNode, 0));

        while(!queue.isEmpty()){
            var current = queue.remove().node;
            visited.add(current);

            for(var edge : current.getEdges()){
                if(visited.contains(edge.to))
                    continue;
                    var newDistance = distances.get(current) + edge.weight;
                    if(newDistance < distances.get(edge.to)){
                        distances.replace(edge.to, newDistance);
                        previousNodes.put(edge.to, current);
                        queue.add(new NodeEntry(edge.to, newDistance)); 
                    }
                }

            }

            return buildPath(previousNodes, toNode);
        }
        
        private Path buildPath(Map<Node, Node> previousNodes, Node toNode) {
            Stack<Node> stack = new Stack<>();
            Node current = toNode;
            
            // Follow the chain of previous nodes and build the stack
            while(current != null) {
                stack.push(current);
                current = previousNodes.get(current); // Update current to the previous node
            }
            
            var path = new Path();
            while(!stack.isEmpty()) {
                // Safe to access label because we never push null onto the stack
                path.add(stack.pop().label);
            }
            
            return path;
    }

    //cycle detection
    public boolean hasCycle(){
        Set<Node> visited = new HashSet<>();

        for(var node: nodes.values()){
            if(!visited.contains(node) && hasCycle(node, null, visited))
            return true;        
        }
        return false;
    }

    private boolean hasCycle(Node node, Node parent, Set<Node> visited) {
        visited.add(node);

        for(var edge : node.getEdges()) {
            if(edge.to == parent)
            continue;

            if(visited.contains(edge.to) || hasCycle(edge.to, node, visited) ) 
            return true; 
            
        }
            return false;
    }
          
}