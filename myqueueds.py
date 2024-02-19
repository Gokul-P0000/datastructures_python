class Node:
    def __init__(self, value):
        self.data = value
        self.next = None 

class Queue:
    def __init__(self):
        self.front = None 
        self.rear = None 

    def isempty(self):
        return self.front == None
    
    def front_item(self):
        if self.isempty():
            return "queue Empty"
        else:
            return self.front.data
        
    def rear_item(self):
        if self.isempty():
            return "queue Empty"
        else:
            return self.rear.data
    
    def size(self):
        c = 0
        if self.isempty():
            return "queue Empty"
        else:
            temp = self.front 
            while temp != None:
                c+=1
                temp = temp.next 
            return c

    def enqueue(self, value):
        newNode = Node(value)
        if self.isempty():
            self.front = newNode 
            self.rear = newNode 
        else:
            self.rear.next = newNode 
            self.rear = newNode 
    
    def dequeue(self):
        if self.isempty():
            print("queue Empty")
        else:
            self.front  = self.front.next 

    def traverse(self):
        if self.isempty():
            print("queue Empty")
        else:
            temp = self.front 
            while temp != None:
                print(temp.data, end=" ")
                temp = temp.next 
            print("\n")

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.traverse()
q.dequeue()
q.traverse()
print(q.front_item())
print(q.rear_item())
print(q.size())
