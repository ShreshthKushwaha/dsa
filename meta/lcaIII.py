class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.parent=None


def findLca(p,q):
    
    if p==q:
        return p
    a = p
    b = q
    m=0
    diff = 0
    while a.parent and b.parent:
        a = a.parent
        b = b.parent
    #finding level difference
    #initiating flag if A is lagging behind in terms of reaching lca
 
    isA = False
    while a.parent:
        isA=True
        a = a.parent
        m+=1
    while b.parent:
        b = b.parent
        m+=1
    print (m,isA)    
    if m==0:
        ##now both are at same level, so if we move each we get lca
        while p!=q:
            p = p.parent
            q=q.parent
        return p
    else:
        if isA==True:
            while m>0:
                m-=1
                p=p.parent
        else:
            while m>0:
                m-=1
                q=q.parent
        ##now both are at same level, so if we move each we get lca        
        while p!=q:
            p = p.parent
            q=q.parent
        return p         

root = Node(1)

achild = Node(2)
bchild = Node(3)
root.left=achild
root.right = bchild
achild.parent = root
bchild.parent=root
cchild=Node(5)
bchild.right = cchild
cchild.parent = bchild

print ("LCA is ", findLca(cchild,achild).val)

                
            
                
                
                
        
        
        