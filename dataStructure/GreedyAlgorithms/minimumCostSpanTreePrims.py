#=============================================================================================
#!/usr/bin/env python
#title           :Minumum cost spanning Tree.py
#description     :PRIMS Algo .Greedy Approach
#author          :Tanaji Sutar
#date            :2020-Feb-13
#python_version  :2.7/3  
#============================================================================================

#Complexity is 0(n2) as we need n for all vertices and n for searching minimum connected
#We can reduce to 0(nlogn) if we use MIN HEAP
#PRIMS algo work for only connected graphs but fails for unconnected graphs. For unconnected gram we need to use Kruskal's Algo.
#
#Algo
#Step1 :set curr to  first vertex
#Step2 :find vertex that has  minimum cost and it is connected to curr vertex
#Step3 :move to next
#Step4 :repeat step 2 to 3 till all vertex completed.

class Graph():
    def __init__(self,V,E):
        self.V=V
        self.E=E
        self.W=None


    def isConnected(self,v1,v2):
        """
        return TRUE if EDGE exist else FALSE
        """
        alledges=self.E
        #Here if v1='A',v2='B' then v1+v2 ='AB'
        return alledges.__contains__(str(v1+v2))

    def getWeight(self,v1,v2):
        try:
            w=self.W[v1+v2]
            return w
        except Exception as e:
            try:
                w=self.W[v2+v1]
                return w
            except Exception as e:
                print('Weight Not found for edge :%s' %(v1+v2))
                return None

    def getMinimumConnected(self,curr,v_notvisited):
        #print('hi',curr,v_notvisited)
        if len(v_notvisited)==0:
            return None , None
        min=None
        for i in v_notvisited:
            if min==None:
                min=i
            else:
                if self.isConnected(curr,i) and (self.getWeight(curr,i) < self.getWeight(curr,min)):
                    min=i
                else :
                    continue
        #print('min',min,self.getWeight(curr,min))
        return min,self.getWeight(curr,min)

    def primsMST(self):
        mstSeq=[]
        start=self.V[0]
        mstSeq.append(start)
        mstCost=0
        v_notvisited=list(self.V)
        #print('by',v_notvisited)
        for curr_vertex in self.V:
            if len(v_notvisited)==0:
                return
            v_notvisited.remove(curr_vertex)
            #print('Cuur',curr_vertex,v_notvisited)
            v,w=self.getMinimumConnected(curr_vertex,v_notvisited)
            #print('check')
            if v is not None:
                #v_notvisited.remove(v)
                mstSeq.append(v)
                mstCost=mstCost+w
                
        print('mstSeq',mstSeq)
        print('mstCost',mstCost)

if __name__ == "__main__":    

        
    V=['A','B','C','D']
    E=['AB','AC','CD','BD','BC']
    g1=Graph(V,E)
    weigths={'AB':4 ,'AC':5,'CD':3,'BD':6,'BC':2}
    g1.W=weigths
    g1.primsMST()

################################
# Test Case 1 : Ans :['A', 'B', 'C', 'D'] and cost=9
#
#       5
#     A___C
#     | 2/|  3
#   4 | / |
#     B___D
#       6
#################################

