# Python program to implement Stack data structure with operations push(), pop(), peek(), isEmpty() 


class stack:
    def __init__ (self):
        self.items=[]

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self , data):
        self.items.append(data)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Error: stack is empty")
            return None
    

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Error: stack is empty")
            return None
        
    def size(self):
        return len(self.items)
    

# driver code


mystack=stack()

print("pushing :")
mystack.push(10)
mystack.push(20)
mystack.push(30)

print("is the stack is empty?" , mystack.is_empty)

print("popped :",mystack.pop())

print("peek:",mystack.peek())

print("size of the stack:",mystack.size())