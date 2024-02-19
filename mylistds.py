import ctypes

class myList:
    def __init__(self):
        self.size = 1          # Array size (capacity)
        self.n = 0             # no.of items that array contains
        # Create a C type array with size = self.size
        self.A = self.make_array(self.size)

    def make_array(self,capacity):
        return (capacity*ctypes.py_object)()
    def length(self):
        return self.n 
    def resize(self, new_capacity):
        B = self.make_array(new_capacity)
        self.size = new_capacity
        # copy of old array to new array 
        for i in range(self.n):
            B[i] = self.A[i]
        # reassign A
        self.A = B

    def aappend(self,item):
        if self.n == self.size:
            # resize array
            self.resize(self.size*2)
        #append
        self.A[self.n] = item
        self.n = self.n + 1

    def display(self):
        # example [1,2,3]
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ","
        return '[' + result[:-1] + ']'

    def getitem_at(self, index):
        if index <= self.n:
            return self.A[index]
        else:
            return "IndexError, Index out of range"
        
    def pop_item(self):
        if self.n == 0:
            return "Empty List"
        print(self.A[self.n-1])
        self.n = self.n - 1

    def clear(self):
        self.size = 1
        self.n = 0

    def find_item(self, item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return "Value Error, not in List"
    
    def insert(self,pos,item):
        if self.n == self.size:
            self.resize(self.size*2)
        for i in range(self.n,pos,-1):
            self.A[i] = self.A[i-1]
        self.A[pos] = item
        self.n = self.n + 1

    def delete(self,pos):
        if 0<= pos < self.n:
            for i in range(pos,self.n-1):
                self.A[i] = self.A[i+1]
            self.n = self.n - 1

    def remove(self,item):
        pos = self.find_item(item)
        if type(pos) == int:
            #delete 
            self.delete(pos)
        else:
            return pos
        


L = myList()

L.aappend("hello")
L.aappend(True)
L.aappend(69)
L.aappend("G")
print(L.length())
print(L.display())
# print(L.getitem_at(2))
# L.pop_item()
# L.clear()
# print(L.display())
# print(L.find_item(69))
# L.insert(1,100)
# print(L.display())
# L.delete(1)
# print(L.display())
L.remove("hello")
print(L.display())

