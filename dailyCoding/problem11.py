
#--------------------------------------------------------
#Trie Data Structure
#--------------------------------------------------------
#Tries is a tree that stores strings.
#Trie is an efficient information reTrieval data structure
#Trie supports search, insert and delete operations in O(L) time where L is length of key.
#It is faster than BST
#If we store keys in binary search tree, a well balanced BST will need time proportional to M * log N, 
# where M is maximum string length and N is number of keys in tree. 
#Using Trie, we can search the key in O(M) time. However the penalty is on Trie storage requirements.
#(Also explore Red-Black Tree, AVL Tree, Splay Tree, etc)
#---------------Advantages of trie------------------------------
#1.search, insert and delete in O(L) time(faster than BST)
#2.we can easily print all words in alphabetical order which is not easily possible with 
# hashing.
#3.We can efficiently do prefix search (or auto-complete) with Trie.

#---------------Issue with trie---------------------------------------------------------
#they need a lot of memory for storing the strings.number of nodes ==number of characters 
#
# NOTE : Ternary Search Tree  can be prefered over Trie if space is issue
# DELETE is  not implemented correctly in below code
#---------------------------------------------------------------------------------------



class Trie:

    def __init__(self,data:str):
        self.data=data
        #list/Array of chilren nodes
        self.childrens=[]
        #flag to indicate if this node is end of word or not
        self.isWordEnd=False
        #How many times this character appeared in the addition process
        self.cnt=1
    

    def insert(self,word:str):
        """
        This method adds the word to given trie
        """

        #initialise at root
        curr=self

        #for every character in word
        for c in word:
            #print('adding word',c,'below',curr.data)
            #present_in_trie
            present_in_trie_flag=False

            #search if character already exist in child
            for child in curr.childrens:
                if child.data == c:
                    #print('already present at',curr.data)
                    #set found flag True
                    present_in_trie_flag = True
                    #Found it so increase counter
                    curr.cnt +=1

                    #set curr to this node where data found and break from loop
                    curr = child
                    break
            
            #print('if not found then add new node',present_in_trie_flag)
            #if not found then add new node
            if not present_in_trie_flag:
                #print('cuur',curr.data,curr.childrens)
                #print('New Node added')
                newNode=Trie(c)
                curr.childrens.append(newNode)
                curr=newNode


        #After completion of for loop,we reached at the end of given word.
        # Mark the last node as end of word

        curr.isWordEnd = True

    def getAllwords(self):
        """
        This function returns all the nodes from given node as string
        
        """


        stk=[]

        if self.data and not self.childrens :
            stk.append(self.data)
        
        elif self.childrens:
            for child in self.childrens:
                for w in child.getwords():
                    stk.append(self.data + w)

        #print(stk)
        return stk

                    

    def get_autocomplete_suggestions(self,prefx):
        
        #set to root
        curr=self
        i=0
        while(i < len(prefx)):
            """
            if curr.data == prefx[i]:
                #if found move ahead
            """
            for child in curr.childrens:
                if child.data == prefx[i]:
                    curr = child
                    print('curr',curr.data)
                    break
                
                
            
            if i == len(prefx) - 1 :
                print('Hereee ',i)
                #
                res = [str(prefx[0:-1]) + i for i in curr.getwords()]
                #res = curr.getwords()
                return res
            
            i=i+1
            #print()

            #now add prefix to each word
            












        



 


    def printTrie(self):
        if self:
            print('Node:',self.data,end=',')
            if self.childrens:
                print('childrens:' ,end=' ')
                for child in self.childrens:
                    print(child.data,end=',')
                
                print('\n')
                for child in self.childrens:
                    child.printTrie()
                    print('')
                
            #printTrie('printTrie')


    def delete(self, key:str):
        """
        This method delete the given key from Trie
        """
        print('inside delete')
        
        #start from first character
        #check in the trie
        #found and have only one or zero child then only delete else keep as it is

        #set start at root
        curr=self

        #if No children available
        if not self.childrens:
            return False
        
        #for every character in key
        for c in key:
            print('looking for', c)
            char_found = False

            #Check character c in all children of current
            for child in curr.childrens:
                print('curr',curr.data)

                if c == child.data:
                    #if matched with child's value
                    char_found = 'Y'
                    print(c,'found')
                    #set the curr to that child

                    #if child is last delete it
                    if not child.childrens:
                        print('removing1 ',child.data)
                        curr.childrens.remove(child)
                    
                    #if child has one child, then go to that and delete it firsts
                    elif len(child.childrens) == 1:
                        print('removing2 ',child.data)
                        #remove child and point curr to child of child
                        curr.childrens.remove(child)
                        curr=child.childrens[0]
                        curr.delete(key[1:])
                        
                    #if child has tow or more child, then dont delete it
                    elif len(child.childrens) >1:
                        print('removing3')
                        continue



    def search(self, key:str):
        """
        This method search the given key in Trie
        """
        #set start at root
        curr=self

        #if No children available
        if not self.childrens:
            return False
        
        #for every character in key
        for c in key:
            #print('looking for', c)
            char_found = False

            #Check character c in all children of current
            
            for child in curr.childrens:

                if c == child.data:
                    #if matched with child's value
                    char_found = 'Y'
                    #print(c,'found')
                    
                    #set the curr to that child
                    curr = child
                    break
            
            #if chat not found
            if not char_found:
                return False

        #Here loop completed will all c means key is found
        if char_found :
            return True
        else:
            return False


#Driver code
if __name__ == "__main__":
    
    #create a root node
    root= Trie('*')
    """

    root.insert('hackathon')
    root.insert('hack')
    
    print('Key preset?','hac',root.search('hac'))
    print('Key preset?','hack',root.search('hack'))
    print('Key preset?','hackathon',root.search('hackathon'))
    print('Key preset?','ha',root.search('ha'))
    print('Key preset?','hammer',root.search('hammer'))

    
    root.insert('abce')
    root.insert('abft')
    print(root.printTrie())
    root.delete('abft')
    """

    
    #assert get_autocomplete_suggestions("ca", ["cat", "car", "cer"]) == ["cat", "car"]
    #assert get_autocomplete_suggestions("ae", ["cat", "car", "cer"]) == []
    #assert get_autocomplete_suggestions("ae", []) == []

    #root.insert('abce')
    #root.insert('abft')

    #get_autocomplete_suggestions("de", ["dog", "deer", "deal"]) == ["deer", "deal"]

    s= ["dog", "deer", "deal"]
    for w in s:
        root.insert(w)
    
    print('and')
    print(root.get_autocomplete_suggestions('de'))
    #print(root.getwords())
    #print(root.printTrie())
        


