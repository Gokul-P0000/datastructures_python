import colletions
stack = collections.deque() #can define size in ()
stack.append(10)
stack.append(20)
stack.pop()
print(stack) #display


import queue
stack = queue.LifoQueue() #can define size in ()
stack.put(10)
stack.get()
stack.put(20,timeout=1) 
#it blocks at most 'timeout' seconds and raises the Full exception if no free slot was available within that time.
stack.get(timeout=1)
#it blocks at most 'timeout' seconds and raises the Empty exception if no item was available within that time.