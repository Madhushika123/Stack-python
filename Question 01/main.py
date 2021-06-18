from stack import Stack

mystack = Stack()
print(mystack.isEmptyStack())
print(mystack.push(150))
print(mystack.push(250))
print(mystack.push(350))
print(mystack.push(450))
print(mystack.isFullStack())
print("Pop element is           : ", mystack.pop())
print("Top element of stack     : ",mystack.top())
print("Stack size is            : ",mystack.size())
print(mystack.pop())

