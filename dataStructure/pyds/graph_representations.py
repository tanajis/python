
#IMP Note : Copied from : geeksforgeeks.org/graph-and-its-representations/ 
# Best explaination : https://www.javatpoint.com/graph-theory-graph-representations

#Graph and its representations
#Every graph has below two components
#    1. A finite set of vertices also called as nodes.
#    2. A finite set of ordered pair of the form (u, v) called as edge


#Directed and Undirected graph . In directed graph edge ED != DE


#Applications of Graph 
# 1.social networks like linkedIn, Facebook.(person is node/vertex)
# 2.Path in cities
# 3.networks

 #      A---B
 #      |   / \
 #      |  /   \
 #      |/     /E
 #      C----D/
 #
 

# Following two are the most commonly used representations of a graph.
# Best explaination : https://www.javatpoint.com/graph-theory-graph-representations
# 1. Adjacency Matrix
# 2. Adjacency List
# 3. Incidence Matrix 
# 4. Incidence List

#First tow are commonly used
#The choice is situation specific




#1.Adjacency Matrix:
# Undirected Here if edge is there between AB then add flag 1 for AB & BA both
#Adjacency matrix for undirected graph is always symmetric
#
#Above graph has 6 edges so 12 times flag should be 1
#   #  A  B  C  D  E
#   A  0  1  1  0  0
#   B  1  0  1  0  1
#   C  1  1  0  1  0
#   D  0  0  1  0  1  
#   E  0  1  0  1  0
#   

#Note you can put difererent weights at the place of zero in case of weighthed graph


#pros : 1.easier to implemen 
#       2.Removing an edge takes only O(1) time.
#Cons  :1.Consumes more space O(V^2)
#       2.Adding a vertex is O(V^2) time


#--------------------------------------------------------------------------------------
#A simple representation of graph using Adjacency Matrix
#--------------------------------------------------------------------------------------

#Note you can put difererent weights at the place of zero in case of weighthed graph


class Graph:
    def __init__(self,numvertex):
        self.numvertex = numvertex #number of vertex
        self.adjMatrix = [[0]*numvertex for x in range(numvertex)] #Array
        self.verticeslist =[0]*numvertex # list of vertexes
        self.vertices = {}              #vertex numbur and name mapping

    def set_vertex(self,vtx,id):
        #get vertex number(vtx) and its name(id)
        if 0<=vtx<=self.numvertex:
            #Add to id and number mapping
            self.vertices[id] = vtx

            #Add to list of names of vertex
            self.verticeslist[vtx] = id

    def set_edge(self,frm,to,cost=0):
        # Get the number of given name  of vertex
        frm = self.vertices[frm]
        to = self.vertices[to]

        #set the weight in matrix

        self.adjMatrix[frm][to] = cost
        #for directed graph do not add this
        self.adjMatrix[to][frm] = cost

    def get_vertex(self):
        #return the list of all the vertices 
        return self.verticeslist

    def get_edges(self):
        #return all the edges
        edges=[]
        for i in range (self.numvertex):
            for j in range (self.numvertex):
                if (self.adjMatrix[i][j]!=0):
                    edges.append((self.verticeslist[i],self.verticeslist[j],self.adjMatrix[i][j]))
        return edges
        
    def get_matrix(self):
        return self.adjMatrix

G =Graph(5)
G.set_vertex(0,'a')
G.set_vertex(1,'b')
G.set_vertex(2,'c')
G.set_vertex(3,'d')
G.set_vertex(4,'e')   
G.set_edge('a','b',1)
G.set_edge('a','c',1)
G.set_edge('b','c',1)
G.set_edge('b','e',1)
G.set_edge('d','e',1)
print("Vertices of Graph")
print(G.get_vertex())
print("Edges of Graph")
print(G.get_edges())
print("Adjacency Matrix of Graph")
print(G.get_matrix())
#This code is contributed by Rajat Singhal
#--------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------
#2. Adjacency List implementation of Graph
#--------------------------------------------------------------------------------------

#An array of lists is used. 
#Size of the array is equal to the number of vertices.
#Each element in Array is Linked list/python list

""" 
Ex.Vertex are A,B,C,D,E and EDges are AB,BC,AC,CD,DE
graph{
    n = 5
    graph_array =
    [
        [A, [B,C]  ]
        [B, [A,C]  ]
        [C, [B,A]  ]
        [D, [C,E]  ]
        [E, [D]    ]
    ]
}
"""  
print('-----------------------------------------')
print('2. Adjacency List implementation of Graph')
print('-----------------------------------------')
  
# A class to represent the adjacency list of the node 
class linkedListNode: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
# A class to represent a graph. A graph 
# is the list of the adjacency lists. 
# Size of the array will be the no. of the 
# vertices "V" 

class Graph: 
    def __init__(self, n): 
        #number if vertices 
        self.v = n 
        #Array size n
        self.graph_array = [None] * self.v 
  
    # Function to add an edge in an undirected graph 
    def add_edge(self, src, dest): 
        # Adding the node to the source node 
        node = linkedListNode(dest) 
        node.next = self.graph_array[src] 
        self.graph_array[src] = node
  
        # Adding the source node to the destination as 
        # it is the undirected graph 
        node = linkedListNode(src) 
        node.next = self.graph_array[dest] 
        self.graph_array[dest] = node 
  
    # Function to print the graph 
    def print_graph(self): 
        for i in range(self.v): 
            print("Adjacency list of vertex {}\n head".format(i), end="") 
            temp = self.graph_array[i] 
            while temp: 
                print(" -> {}".format(temp.data), end="") 
                temp = temp.next
            print(" \n") 
  
  
# Driver program to the above graph class 
if __name__ == "__main__": 
    V = 5
    graph = Graph(V) 
    graph.add_edge(0, 1) 
    graph.add_edge(0, 4) 
    graph.add_edge(1, 2) 
    graph.add_edge(1, 3) 
    graph.add_edge(1, 4) 
    graph.add_edge(2, 3) 
    graph.add_edge(3, 4) 
  
    graph.print_graph() 
  
#Note :copied from Geeksforgeeks
