class Node():
    
    #contructor method
    
    def __init__(self, data):
        self.data=data
        self.next=None

    def get_data(self):   #retrieveing the nodes data
        return self.data
    
    def get_next(self):   #retrieveing the pointer
        return self.next
    
    def set_next(self, new_text):
        self.next=new_text

    def output_node(self):
        next_data = None
        if (self.next != None):
            next_data = self.next.data
        print(f"Data: {self.data}, next: {next_data}") 


class Stack():

   
    #contructor method
    def __init__(self):
        self.top=None

    def is_empty(self):    #check if list is empty
        if self.top==None:
            return True
        else:
            return False
        
    def push(self,data):
        new_node=Node(data)
        if not self.is_empty():  #check if list is empty
            new_node.set_next(self.top)  #point to next element in list
        
        self.top=new_node  #set top to point to the new node
            

    def pop(self):
       
        popped_data=None
        
        if self.is_empty():
            print("Stack is empty - nothing tp pop")
        else:
            popped_data= self.top.get_data()  #Get data and change pointer to next item
            self.top=self.top.get_next()
        return popped_data
    
    def output_stack(self):
        if self.top !=None:
            print("---- State of the stack (first item is the top) ----")
            current_node=self.top
            curent_node.output_node()
            while current_node.get_next() != None:
                curent_node=current_node.get_next()
                current_node.output_node()
            print()
    
    
def main():
    #Create a stack and push and pop items
        
    my_stack= Stack()
       
    my_stack.push("Dana") #test data
    # my_stack.output_stack()
    print(my_stack.top.data)
    
    my_stack.push("Anna") #test data
    # my_stack.output_stack()
    print(my_stack.top.data)
    # my_stack.push("Anna")
    # my_stack.output_stack()

    # my_stack.push("Rey")
    # my_stack.output_stack()
    
    # popped_item=my_stack.pop()
    # print(f"Popped {popped_item}")
    # my_stack.output_stack()

    # my_stack.push("Sabrina")
    # my_stack().output_stack()


 

    # def test_my_stack():  #testing the stack
    #  my_stack = Stack()
    #  my_stack.push("carrots")
    #  my_stack.push("turnips")

    #  peeked_element = my_stack.peek()
    #  print(peeked_element)

    #  popped_element = my_stack.pop()
    #  print(popped_element)


if __name__=='__main__':
    main()        



