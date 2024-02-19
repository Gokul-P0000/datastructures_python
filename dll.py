class Node:
    def __init__(self,data):
        self.data = data
        self.pref = None
        self.nref = None

class DLinkList:
    def __init__(self):
        self.head = None 

    def insert_empty(self,data):
        if self.head is None:
            newNode = Node(data)
            self.head = newNode 
        else:
            print("Link list is not Empty")
    
    def AtBeg(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode 
        else:
            newNode.nref = self.head
            self.head.pref = newNode
            self.head = newNode

    def Fdisplay(self):
        if self.head is None:
            print("list is empty!")
        iternode = self.head
        while(iternode is not None):
            print(iternode.data,end="")
            iternode = iternode.nref
            if(iternode is not None):
                print("->",end="")

    def Bdisplay(self):
        if self.head is None:
            print("list is empty!")
        iternode = self.head
        while(iternode.nref is not None):
            iternode = iternode.nref
        while(iternode is not None):
            print(iternode.data,end="")
            iternode = iternode.pref
            if(iternode is not None):
                print("->",end="")


dll = DLinkList()
dll.AtBeg(10)
dll.AtBeg(20)
dll.AtBeg(30)
dll.Fdisplay()
print()
dll.Bdisplay()