"""
Emil Dark 2564926 edark18@student.oulu.file
 
 Input: Name of a graph file (needs to be in same folder for ease of use)
 Python program for Kruskal's algorithm to find 
 Minimum Spanning Tree of a given connected, 
 undirected and weighted graph. Given graph used with
 Dijkstra's algorithm to find fastest route trough
 minimum spanding tree. 
 Output: Path and heaviest edge on path.
"""
from weightedgraph import *
from collections import defaultdict 
import time

#Class to represent a graph 
class Graph: 

    def __init__(self,vertices): 
        self.V= vertices #No. of vertices 
        self.graph = [] # default dictionary 
                                # to store graph 
        

    # function to add an edge to graph 
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 

    # A utility function to find set of an element i 
    # (uses path compression technique) 
    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 

    # A function that does union of two sets of x and y 
    # (uses union by rank) 
    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 

        # Attach smaller rank tree under root of 
        # high rank tree (Union by Rank) 
        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 

        # If ranks are same, then make one as root 
        # and increment its rank by one 
        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1

    # The main function to construct MST using Kruskal's 
        # algorithm 
    def KruskalMST(self): 

        result =[] #This will store the resultant MST 

        i = 0 # An index variable, used for sorted edges 
        e = 0 # An index variable, used for result[] 

            # Step 1: Sort all the edges in non-decreasing 
                # order of their 
                # weight. If we are not allowed to change the 
                # given graph, we can create a copy of graph 
        self.graph = sorted(self.graph,key=lambda item: item[2]) 

        parent = [] ; rank = [] 

        # Create V subsets with single elements 
        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
    
        # Number of edges to be taken is equal to V-1 
        while i < self.V -1 : 
            
            # Step 2: Pick the smallest edge and increment 
                    # the index for next iteration 
            u,v,w = self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v) 

            # If including this edge does't cause cycle, 
            # include it in result and increment the index 
            # of result for next edge 
            if x != y: 
                e = e + 1   
                result.append([u,v,w]) 
                self.union(parent, rank, x, y)           
            # Else discard the edge 

        # print the contents of result[] to display the built MST 
        print ("\tFollowing are the edges in the constructed MST")
        for u,v,weight in result:
            # DEBUG INFO: 
            #print ("\t%d -- %d == %d" % (u,v,weight))
            add_edge(graaffi,u,v,weight)
            
       
        dijkstra(graaffi,1)
        print("\nDIJKSTRA - FIND SHORTEST PATH")
        print("\t Path from 1 to", int(endpoint) ,"with cumulative weights:")
        print_path(graaffi,int(endpoint))
        print_heaviestEdge()
        
        """
        MST_KRUSKAL(G):
        A = empty
        For each vertex v contains G.V:
            MAKE-SET(v)
        For each edge (u, v) contains G.E ordered by increasing order by weight(u, v):
            if FIND-SET(u) ≠ FIND-SET(v):       
            A = A ∪ {(u, v)}
            UNION(u, v)
        return A
        """

# Driver code

filename = input("Type filename: ")
print()
start_time = time.time() #start timing program
f = open(filename, "r")
endpoint, edgesLeft = (f.readline()).split()
int_edgesLeft = int(edgesLeft)

print("PARAMETERS")
print("\tEndpoint: {}".format(endpoint))
print("\tEdges to add to graph: {}".format(edgesLeft))


g = Graph(int_edgesLeft-1)
graaffi = WeightedGraph(int(endpoint))
i = 0
for x in f:
    if int_edgesLeft > 0:
        node, edge, edgeWeight = (x).split()
        g.addEdge(int(node), int(edge), int(edgeWeight))
        i += 1
        int_edgesLeft -= 1
     

print("\tEdges added to the graph:", i, "\n")
print("KRUSKAL - CREATE MST")
g.KruskalMST() 
print("--- %s seconds ---" % (time.time() - start_time))

