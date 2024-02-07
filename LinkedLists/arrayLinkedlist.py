head=0
pointer=1
data=0

linkedList= [ 
    [ "Bob", 1], 
    [ "Sarah", 2],
    [ "Sharon" , 3], 
    [ "Roberto", None ],
    [ None, None] 
   ]
#print(linkedList[head])

#checking if the list is empty
'''
def isEmpty():
    if head == None:
        print("List is empty")

#adding to the end of the list
'''
'''

def addEnd(data):
    global current, pointer, linkedList
    while current!=None:
        pointer=pointer+1
        current=pointer
    linkedList.append[[data][current]]
    print(current)
addEnd("dana")
print(linkedList)

'''

#checks if list is empty
def isEmpty():
 if (linkedList[head]==None):
        print("List is empty")
 else:
      current = head
      while current!= None:
          print(linkedList[current][data])
          current=linkedList[current][pointer]


def add():
    global current, pointer, name
    isEmpty()
    current=linkedList[current][pointer]
    pointer=current.pointer + 1
    linkedList.append(name[current][pointer])

add()
name="dana"
print(linkedList)


#adding an item to the end of the list      



