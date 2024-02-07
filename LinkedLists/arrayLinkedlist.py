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

#checks if list is empty
def isEmpty():
 if (linkedList[head]==None):
        print("List is empty")
 else :
     print("List is full")

#traversing through the list
def traverseList():
     global current
     if (linkedList[head]==None):
        print("List is empty")
     else:
        current = head
        while current!= None:
         print(linkedList[current][data])
         current=linkedList[current][pointer]

#adding item to the list
class Node(): 
  def create_node (self, nameData):
    self.data= nameData
    self.next = None
    
  
  def add(nameData):
       global current, pointer, data
     #check the list is empty
       traverseList() #traverse through the list to find the empty space, (none/null)
       new_node = Node(nameData)
       if current.pointer==None: #finding an empty space
        current.data=new_node
        linkedList[pointer]=current.next
        linkedList[pointer.next]=None
        linkedList(new_node[current][None])
 


nameData="dana"
Node()
create_node(Dana)
add(nameData)


print(linkedList)




