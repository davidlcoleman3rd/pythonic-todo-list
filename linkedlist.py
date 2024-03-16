

class NoValueFound(Exception):
    "Raised when the desired list item to be removed cannot be found in the list."
    pass

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
      #  self.prev = None

class LinkedList:
    def __init__(self,head=None):
        self.head = head
        self.length = 0

# ******
    def append(self, new_node):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_node
            current.next.prev = current
            
        else:
            self.head = new_node

        self.length = self.length + 1

# ******
    def delete(self, selection):
        current = self.head
        selection = int(selection)
        if selection <= self.length and current != None:
            counter = 1
            while counter < selection:
                current = current.next
                counter = counter + 1
            if current is self.head:
                if counter == 1:
                    self.head = None
                else:
                    self.head = current.next
                    self.head.prev = None
            else:
                current.prev.next = current.next
                if current.next != None:
                    current.next.prev = current.prev
            current = None
            current = self.head
            
            self.length = self.length - 1
        else:
            raise NoValueFound('The requested list item was not found in the list.')

# ******
    def search(self, selection):
        current = self.head
        position = 1
        while position <= self.length:
            if selection == current.value:
                return current.value
        else:
            return None

# ******
    def iterate(self, selection):
        current = self.head
        position = 1
        while position <= selection and not (self.length < selection):
           # print("this happened")
           # print(f"selection = {selection}")
            #print(f"position = {position}")
            if position == selection:
                #print("return curr")
                return current.value
            current = current.next
            position += 1
        while current.next != None:
            current = current.next
        return current.value

# ******
    def printList(self):
        counter = 1
        
        current = self.head
        while current:
            print(f"{counter})  {current.value}")
            current = current.next
            counter = counter + 1

# ******
    def clearList(self):
        while self.length > 0:
            self.delete(self.length)

#myList = LinkedList()
#myList.append(Node(37))
#myList.append(Node(101))

#myList.printList()

#myList.delete(2)

#yList.printList()