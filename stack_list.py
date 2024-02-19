def push():
    e = int(input("Enter element to push: "))
    if(len(stack)==n):
        print("stack is full!")
    else:
        stack.append(e)
        print("element is added!")
def pop():
    if(len(stack)==0):
        print("stack is empty!")
    else:
        print("the popped element is: ",stack[-1])
        stack.pop()
def display():
    if(len(stack)==0):
        print("stack is empty!")
    else:
        print("the stack contains: ",*stack)

n = int(input("Enter the limit of stack: "))
stack = []
while True:
    print("\n1.push\n2.pop\n3.Display\n4.quit")
    c = int(input("\n Select operation: "))
    if c==1:
        push()
    elif c==2:
        pop()
    elif c==3:
        display()
    else:
        display()
        break

