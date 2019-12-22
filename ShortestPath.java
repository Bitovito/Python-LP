// A Java program for caminoDijkstra's single source shortest path algorithm. 
// The program is for adjacency matrix representation of the graph 
import java.util.*;

class ShortestPath { 
	// A utility function to find the vertex with minimum distance value, 
	// from the set of vertices not yet included in shortest path tree 
	int V;
    ShortestPath(int V){
        this.V = V;
    } 
	int minDistance(int dist[], Boolean sptSet[]){
		int min = Integer.MAX_VALUE, min_index = -1; 

		for (int v = 0; v < V; v++){ 
			if (sptSet[v] == false && dist[v] <= min){ 
				min = dist[v]; 
				min_index = v; 
			} 
		}
		return min_index; 
	} 

	// Function that implements caminoDijkstra's single source shortest path 
	// algorithm for a graph represented using adjacency matrix 
	// representation 
	List<Integer> caminoDijkstra(int graph[][], int src, int fin){ 
        List<Integer> vPath = new ArrayList<Integer>();
        vPath.add(fin);
        int prevVertex[] = new int[V];
		int dist[] = new int[V];
		Boolean sptSet[] = new Boolean[V];
		for (int i = 0; i < V; i++){ 
			dist[i] = Integer.MAX_VALUE; 
			sptSet[i] = false; 
		} 
		dist[src] = 0; 
		for (int count = 0; count < V - 1; count++){
			int u = minDistance(dist, sptSet); 
			sptSet[u] = true; 
			for (int n = 0; n < V; n++){
				if (!sptSet[n] && graph[u][n] != 0 && dist[u] != Integer.MAX_VALUE && dist[u] + graph[u][n] < dist[n]){ 
                    dist[n] = dist[u] + graph[u][n];
                    prevVertex[n] = u;
				}
			}
		} 
        Integer curr = fin;
        while(curr!=0){
            vPath.add(prevVertex[curr]);
            curr = prevVertex[curr];
        }
        return vPath;
	} 
	
	int[] costDijkstra(int graph[][], int src){ 
		int dist[] = new int[V];
		Boolean sptSet[] = new Boolean[V]; 
		for (int i = 0; i < V; i++){ 
			dist[i] = Integer.MAX_VALUE; 
			sptSet[i] = false; 
		} 
		dist[src] = 0; 
		for (int count = 0; count < V - 1; count++){
			int u = minDistance(dist, sptSet); 
			sptSet[u] = true; 
			for (int n = 0; n < V; n++){
				if (!sptSet[n] && graph[u][n] != 0 && dist[u] != Integer.MAX_VALUE && dist[u] + graph[u][n] < dist[n]){ 
					dist[n] = dist[u] + graph[u][n];
				}
			}

		}
		return dist;
	}
}
