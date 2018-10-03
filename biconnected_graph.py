from collections import defaultdict 
   
#This class represents an undirected graph using adjacency list representation 
class Graph: 
   
    def __init__(self,vertices): 
        self.V= vertices #No. of vertices 
        self.graph = defaultdict(list) # default dictionary to store graph 
        self.Time = 0
   
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
        self.graph[v].append(u) 
   
    '''A recursive function that returns true if there is an articulation 
    point in given graph, otherwise returns false. 
    This function is almost same as isAPUtil() 
    u --> The vertex to be visited next 
    visited[] --> keeps tract of visited vertices 
    disc[] --> Stores discovery times of visited vertices 
    parent[] --> Stores parent vertices in DFS tree'''
    def isBCUtil(self,u, visited, parent, low, disc): 
  
        #Count of children in current node  
        children =0
  
        # Mark the current node as visited and print it 
        visited[u]= True
  
        # Initialize discovery time and low value 
        disc[u] = self.Time 
        low[u] = self.Time 
        self.Time += 1
  
        #Recur for all the vertices adjacent to this vertex 
        for v in self.graph[u]: 
            # If v is not visited yet, then make it a child of u 
            # in DFS tree and recur for it 
            if visited[v] == False : 
                parent[v] = u 
                children += 1
                if self.isBCUtil(v, visited, parent, low, disc): 
                    return True
  
                # Check if the subtree rooted with v has a connection to 
                # one of the ancestors of u 
                low[u] = min(low[u], low[v]) 
  
                # u is an articulation point in following cases 
                # (1) u is root of DFS tree and has two or more chilren. 
                if parent[u] == -1 and children > 1: 
                    return True
  
                #(2) If u is not root and low value of one of its child is more 
                # than discovery value of u. 
                if parent[u] != -1 and low[v] >= disc[u]: 
                    return True    
                      
            elif v != parent[u]: # Update low value of u for parent function calls. 
                low[u] = min(low[u], disc[v]) 
  
        return False
  
  
    # The main function that returns true if graph is Biconnected, 
    # otherwise false. It uses recursive function isBCUtil() 
    def isBC(self): 
   
        # Mark all the vertices as not visited and Initialize parent and visited,  
        # and ap(articulation point) arrays 
        visited = [False] * (self.V) 
        disc = [float("Inf")] * (self.V) 
        low = [float("Inf")] * (self.V) 
        parent = [-1] * (self.V) 
      
  
        # Call the recursive helper function to find if there is an  
        # articulation points in given graph. We do DFS traversal starting 
        # from vertex 0 
        if self.isBCUtil(0, visited, parent, low, disc): 
            return False
  
        '''Now check whether the given graph is connected or not. 
        An undirected graph is connected if all vertices are 
        reachable from any starting point (we have taken 0 as 
        starting point)'''
        if any(i == False for i in visited): 
            return False
          
        return True
   
# Create a graph given in the above diagram 
g1 =  Graph(2) 
g1.addEdge(0, 1) 
print "Yes" if g1.isBC() else "No"
  
g2 = Graph(5) 
g2.addEdge(1, 0) 
g2.addEdge(0, 2) 
g2.addEdge(2, 1) 
g2.addEdge(0, 3) 
g2.addEdge(3, 4) 
g2.addEdge(2, 4) 
print "Yes" if g2.isBC() else "No"
  
g3 = Graph(3) 
g3.addEdge(0, 1) 
g3.addEdge(1, 2) 
print "Yes" if g3.isBC() else "No"
  
   
g4 = Graph (5) 
g4.addEdge(1, 0) 
g4.addEdge(0, 2) 
g4.addEdge(2, 1) 
g4.addEdge(0, 3) 
g4.addEdge(3, 4) 
print "Yes" if g4.isBC() else "No"
  
g5 = Graph(3) 
g5.addEdge(0, 1) 
g5.addEdge(1, 2) 
g5.addEdge(2, 0) 
print "Yes" if g5.isBC() else "No"