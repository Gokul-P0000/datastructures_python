def enqueue():
    e = int(input("Enter element to add: "))
    if(len(queue)==n):
        print("queue is full!")
    else:
        queue.append(e)
        print("element is added!")
def dequeue():
    if(len(queue)==0):
        print("queue is empty!")
    else:
        print("the deleted element is: ",queue[0])
        queue.pop(0)
def display():
    if(len(queue)==0):
        print("queue is empty!")
    else:
        print("the queue contains: ",*queue)

n = int(input("Enter the limit of queue: "))
queue = []
while True:
    print("\n1.Add\n2.Delete\n3.Display\n4.quit")
    c = int(input("\n Select operation: "))
    if c==1:
        enqueue()
    elif c==2:
        dequeue()
    elif c==3:
        display()
    else:
        display()
        break
