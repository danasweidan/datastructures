#Traversing means to work your way systematically through the list
#To traverse a linked list you need to start from the first node (referenced by head) and follow each next link until you reach the last node (whose next pointer will be Null)

#Contructor for Node
class Node(): 
  def __init__(self, given_data):
    self.data= given_data
    self.next = None

  #Retrieving the data from the node
  def get_data(self):
      return self.data

  #Retriveing the data from the next node
  def get_next(self):
      return self.next
  
  def set_next(self, new_next):
      self.next = new_next

#Constructor for the list
class LinkedList():
  def __init__(self):
    self.head = None
  #Head is pointing at null since theres nothing in the queue

  def traverse(my_list):
    # Set the current node as the head
    current= my_list.head
    print(current)
    #Head pointer points at the first node

  # Repeat until there are no more linked nodes
    while current is not None:
      print(current.get_data())
      current = current.get_next()
      print(current)

  #inserting at the front of the list
  def insert_at_front(self, data):
    # Create a new node
    new_node = Node(data)

    # Check if the head node exists
    if self.head is None:
      self.head = new_node
    else:
    # Update the pointers so the new node is the head
        new_node.set_next(self.head)            
        self.head = new_node
    
###############  IAM HERE 'THIS DOESNT WORK NEED TO.....

'''
ADD IN THE INSERT INTO MIDDLE CODE FROM ISSAAC


'''
my_list=LinkedList()    
print(my_list)

print(my_list.head)

randomNode = Node("Dana")

print(randomNode.next)

Node("dana")
print(self.head.next.data)

