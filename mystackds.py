class Node:
    def __init__(self, value):
        self.data = value
        self.next = None 

class Stack:
    def __init__(self):
        self.top = None
        self.n = 0          #number of elements

    def isempty(self):
        return self.top == None

    def push(self, value):
        newNode = Node(value)
        newNode.next = self.top
        self.top = newNode
        self.n = self.n + 1

    def pop(self):
        if(self.isempty()):
            return "Stack is Empty"
        else:
            item = self.top.data
            self.top =  self.top.next
            self.n = self.n - 1
            return item

    def peek(self):
        if(self.isempty()):
            return "Stack is Empty"
        else:
            return self.top.data

    def traverse(self):
        temp = self.top
        while(temp != None):
            print(temp.data)
            temp = temp.next

# s = Stack()
# print(s.isempty())
# s.push(10)
# s.push(20)
# s.push(30)
# s.push(40)
# s.push(50)
# print(s.pop())
# print(s.peek())
# s.traverse()
# print(s.n)