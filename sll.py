class Node:
    def __init__(self,data):
         self.data = data
         self.ref = None 

class SLinkList:
    def __init__(self):
        self.head = None

    def AtBeg(self,data):
        newNode = Node(data)
        newNode.ref = self.head
        self.head = newNode

    def AtEnd(self,data):
        newNode = Node(data)
        if(self.head is None):
            self.head = newNode
        else:
            endnode = self.head
            while(endnode.ref is not None):
                endnode = endnode.ref
            endnode.ref = newNode

    def After_Node(self,data,x):
        newNode = Node(data)
        midnode = self.head
        while(midnode.data!=x):
            midnode = midnode.ref
        newNode.ref = midnode.ref
        midnode.ref = newNode
    
    def Before_Node(self,data,x):
        newNode = Node(data)
        if(self.head.data == x):
            newNode.ref = self.head
            self.head = newNode
        else:
            midnode = self.head
            while(midnode.ref.data == x ):
                midnode = midnode.ref
            newNode.ref = midnode.ref
            midnode.ref = newNode

    def DelAtBeg(self):
        if(self.head is None):
            print("link list is empty!")
        else:
            self.head = self.head.ref
    
    def DelAtEnd(self):
        if(self.head is None):
            print("link list is empty!")
        else:
            endnode = self.head
            while(endnode.ref.ref is not None):
                endnode = endnode.ref
            endnode.ref = None

    def Del_Node(self,x):
        if(self.head is None):
            print("link list is empty!")
        else:
            midnode = self.head
            while(midnode.ref.data!=x):
                midnode = midnode.ref
            midnode.ref = midnode.ref.ref
    
    def display(self):
        if(self.head is None):
            print("linklist is empty!")
        else:
            iternode = self.head
            while(iternode is not None):
                print(iternode.data,end="")
                if(iternode.ref is not None):
                    print("->",end="")
                iternode = iternode.ref

sll = SLinkList()
sll.AtBeg(10)
sll.AtEnd(72)
sll.AtBeg(20)
sll.After_Node(1,10)
# sll.Before_Node(2,10)
sll.DelAtBeg()
sll.DelAtEnd()
sll.AtEnd(2)
sll.AtEnd(3)
sll.Del_Node(2)
sll.display()