#=============================================================================================
#!/usr/bin/env python
#title           :Minumum cost spanning Tree.py
#description     :Kruskal Algo .Greedy Approach
#author          :Tanaji Sutar
#date            :2020-Feb-13
#python_version  :2.7/3  
#============================================================================================

# NOT COMPLETED YET
#Algo
#Step1 :set curr to  first vertex
#Step2 :find vertex that has  minimum cost & if not forming cycle, join them
#Step3 :move to next
#Step4 :repeat step 2 to 3 till all vertex completed.


#

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

    def getMinimum(self,v_notvisited):
        if len(v_notvisited)==0:
            return None

        #edge with last and first vertex
        min=self.getWeight(v_notvisited[0],v_notvisited[-1])
        prev=v_notvisited[0]
        for  i in v_notvisited[1:]:
            if min is None:
                min =self.getWeight(prev,i)
            elif self.getWeight(prev,i) is not None:
                if self.getWeight(prev,i) <min:
                    min=self.getWeight(prev,i)

            
            return prev+i

    def kruskalMST(self):
        mstSeq=[]
        start=self.V[0]
        #mstSeq.append(start)
        mstCost=0
        v_notvisited=list(self.V)
        #print('by',v_notvisited)
        while(1):
            #print('sjss',v_notvisited)
            if len(v_notvisited)==0:
                break
            
            res=self.getMinimum(v_notvisited)
            if res is not None:
                v_notvisited.remove(res[0])
                v_notvisited.remove(res[1])
                mstSeq.append(res)
                mstCost=mstCost+self.getWeight(res[0],res[1])


        print('mstSeq',mstSeq)
        print('mstCost',mstCost)

if __name__ == "__main__":    
        
    V=['A','B','C','D']
    E=['AB','AC','CD','BD','BC']
    g1=Graph(V,E)
    weigths={'AB':4 ,'AC':5,'CD':3,'BD':6,'BC':2,'AD':3}
    g1.W=weigths
    g1.kruskalMST()

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

