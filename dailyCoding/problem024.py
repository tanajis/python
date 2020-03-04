
class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.locked = False
        self.parent = None
    
    def is_locked(self):
        """
        returns whether the node is locked
        """
        return self.locked

    def is_ancestors_locked(self):
        #check if parrents are not locked
        parent =self.parent
        #print('parant',parent.data)
        flg = 'N'
        while(parent):
            if parent.is_locked():
                flg = 'Y'
                break
            parent = parent.parent
        
        if flg == 'Y':
            return True
        else:
            return False

    def is_descendants_locked(self):
        """
        check if decendants are locked
        """
        if self.left:
            #check if left node is locked
            res1 = self.left.is_locked()
            #check RECURSIVELY if descendants of left node are locked 
            res2 = self.left.is_descendants_locked()

            if res1 or res2 :
                return True
            else:
                return False
        
        if self.right:
            #check if left node is locked
            res1 = self.right.is_locked()
            #check RECURSIVELY if descendants of left node are locked 
            res2 = self.right.is_descendants_locked()

            if res1 or res2 :
                return True
            else:
                return False

    def lock(self):
        """
         which attempts to lock the node. If it cannot be locked, 
         then it should return false. Otherwise, it should lock it and return true.
         node can be locked only if all of its descendants or ancestors are not locked.
        """

        #check if not locked
        if self.locked:
            print('Already locked!!')
            return False


        #print(self.is_ancestors_locked(), self.is_descendants_locked())
        #check if any descendant or decendants is locked
        if self.is_ancestors_locked() or self.is_descendants_locked():
            #if any one is loked, return False as we cant apply lock
            #print('hi')
            return False
        else:
            self.locked = True
            #print('hi',self.data,self.locked)
            return True
        
    def unlock(self):
        """
        unlocks the node. If it cannot be unlocked, then it should return false. 
        Otherwise, it should unlock it and return true.
        """

        #check if locked .If not locked, we cant unlock
        if not self.locked:
            print('Not locked!!')
            return False

        #check if any descendant or decendants is locked
        if self.is_ancestors_locked() or self.is_descendants_locked():
            #if any one is loked, return False as we cant apply unlock
            return False
        else:
            self.locked = False
            return True

if __name__ == "__main__":
    
    root = Node('a')
    b =   Node('b')
    c =   Node('c')
    d =   Node('d')
    e =   Node('e')
    f =   Node('f')
    g =   Node('g')
    
    root.left = b
    b.parent = root

    root.right = c
    c.parent = root

    b.left = d
    d.parent = b

    b.right = e
    e.parent = b

    e.left = f
    f.parent = e

    c.left = g
    g.parent = c
    print('is b Locked?:',b.is_locked())
    #Lock b 
    print('Locking b:',b.lock())
    #check status of b .Shoud retur True
    print('is b Locked?:',b.is_locked())

    #Now try to lock root.It should not allow
    print('Locking Root:',root.lock())
    print('unlocking b:',b.unlock())
    print('check b',b.is_locked())

    print('Locking Root:',root.lock())
    print('is Root locked:',root.is_locked())

    #Now root is locked try locking f as ansester root is locked
    print('Locking c:',c.lock())
    print('Locking g:',g.lock())
    print('Locking f:',f.lock())

    #now unlock root 
    print('unlock root:',root.unlock())
    #lock c
    print('Locking c:',c.lock())
    #try locking g.It hsoulkdnt allowed as ansester c is locked

    print('Locking g:',g.lock())

    #for f No anscenter is locked so ut shoud retunr True
    print('Locking f:',f.lock())
    

"""
        a
    b       c
 d    e    g 

    f
"""

    
