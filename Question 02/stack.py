class Node:
    # Constructor Node
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    # Constructor Stack
    def __init__(self):
        self.head = None

    def isempty(self):
        if self.head == None:
            return True
        else:
            return False

    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    def disply(self):
        iternode = self.head
        if self.isempty():
            print("Stack Umderflow")
        else:
            while(iternode != None):
                print(iternode.data,  end=' ==> ')
                iternode = iternode.next
            return
