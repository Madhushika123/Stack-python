

class Node:
    # Constructor Node
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    # Constructor Stack
    def __init__(self,limit):
        self.head = None
        self.size = 0

    def getsize(self):
        return self.size


    # To check is empty the linked list
    def isempty(self):
        if self.head.size == None:
            return True
        else:
            return False

    # To push data to the linked list
    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
            self.size += 1

    # Find the first data in linked list
    def top(self):
        if self.isempty():
            print(" Underflow ")
        else:
            currentnode = self.head.data
            print(self.head.data)
            return currentnode


    # pop (delete) to the data in linked list
    def pop(self):
        if self.isempty():
            return None
        else:
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            self.size -= 1
            return poppednode.next

    # To disply the linked list
    def disply(self):
        currentnode = self.head
        if self.isempty():
            print("Stack Underflow")
        else:
            while(currentnode != None):
                print(currentnode.data, end= " --> ")
                currentnode = currentnode.next
            return

