#Emil Dark 2564926 edark18@student.oulu.file
# Python code to perform Dijkstra's algorithm
# in a non-directed graph
import math
from collections import deque

INF = float('inf')
# global variable
heaviestEdge = 0
previes = 0
 
# We assume that nodes numbered from 1 to n

# class for edges in adjacency list
class WeightedEdgeNode:
    def __init__(self,nde,wght=0):
        self.node = nde
        self.weight = wght

# graph class for breadth-forst search 
class WeightedGraph:
    
    def __init__(self,nVerts):
        self.nVertices = nVerts
        self.adj_list = {}
        self.vertices = []
        
        for x in range(1,nVerts+1):
            self.adj_list[x] = []
            self.vertices.append(x)
            
        self.dist = {}
        for x in range(1,nVerts+1):
            self.dist[x] = INF
            
        self.pred = {}
        for x in range(1,nVerts+1):
            self.pred[x] = None

        
# adds edge (x,y)       
def add_edge(g,x,y,wght):   
    g.adj_list[x].append(WeightedEdgeNode(y,wght))
    g.adj_list[y].append(WeightedEdgeNode(x,wght))  

    
'''
   Dijkstra's algorithm:
   DIJKSTRA(G,w,s)
   for each vertex v in V
      d[v] = INF
      p[v] = NIL
   d[s] = 0
   S = EMPTY
   Q = V[G]
   while Q != EMPTY
         u =  EXTRACT-MIN(Q)
         S = S UNION {u}
         for each vertex v in Adj[u] do
            if d[v] > d[u] + w(u,v) then
               d[v] = d[u] + w(u,v)
               p[v] = u
'''

def dijkstra(g,s):
    
    for i in g.vertices:
        g.dist[i] = INF
        g.pred[i] = 0
        
    g.dist[s] = 0
    
    queue = [i for i in g.vertices]
    
    while len(queue) > 0:
        minval = INF
        u = 0
        for vert in queue:
            if g.dist[vert] < minval:
                minval = g.dist[vert]
                u = vert

        if u == 0:
            #Check if list has gone trough
            break
        
        queue.remove(u)
            
        
        for edge in g.adj_list[u]:
            v = edge.node
            
            if g.dist[v] > g.dist[u] + edge.weight:
                    g.dist[v] = g.dist[u] + edge.weight
                    g.pred[v] = u    
                    
        # DEBUG INFO:
        # print(u, " processed, dist =  ",g.dist[u])
        
def print_path(g,u):
    global previes
    global heaviestEdge
    
    if g.pred[u] != 0:
        print_path(g,g.pred[u])
        
    distance = g.dist[u]
    diff = distance - previes
    print("\t",u,':',distance, " +", diff)
    
    previes = distance
    if heaviestEdge < diff:   
        heaviestEdge = diff    
            
def print_heaviestEdge():
    if heaviestEdge == INF:
        print("\t\nPath was not found to ENDPOINT\n")
    else:
        print("\t Heaviest edge is: ", heaviestEdge, "\n")
    
    
    
