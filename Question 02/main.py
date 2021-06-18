from stack import Stack

mystack = Stack()
print(mystack.isempty())
mystack.top()
mystack.push(100)
mystack.push(200)
mystack.push(300)
mystack.push(400)
mystack.push(500)
mystack.disply()

print("\n======================================================================")

mystack.pop()
mystack.top()
mystack.disply()

print(mystack.size())


