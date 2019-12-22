import java.util.List;

public interface Grafo{
    int edgeWeigth(int n1, int n2);
    List<Integer> shortestPath(int n1, int n2);
    void addEdge(int n1, int n2, int peso);
    void addNode(int n1);
}