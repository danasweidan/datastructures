'''
need to check is full
check enqueue is working

'''

queue=["","","","",""]
#initialising
front=0
rear=-1
size=0

#enqueue
def enqueue(studentname):
    # add to the rear of the queue
    global rear,size
    if (not(isFull())):
        rear=rear+1
        queue[rear]=studentname
        size=size+1

#dequeue
def dequeue():
     global front, size
     front=front+1
     size=size-1
     return

##### THIS NOT WORKING ########
# checking if queue is full
def isFull():
     if size==5:
          print("Error: queue is full")
          return True
     else:
          return False
# checking if queue is full
def isEmpty():
     if size==0:
          print("queue is empty")
          return True
     else:
          return False

# test data
enqueue("A")
print("q", queue)

enqueue("B")
print("q", queue)

enqueue("C")
print("q", queue)

enqueue("D")
print("q", queue)

enqueue("E")
print("q", queue)

dequeue()
print("q", queue)

dequeue()
print("q", queue)

enqueue("F")
print("q", queue)

enqueue("G")
print("q", queue)

print(queue)
#here


