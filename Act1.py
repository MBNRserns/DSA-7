#Stack -- FILO (First In Last Out)
class Stack:
    def __init__(self,n):
        self.stack = []
        self.n = n #max elements
    
    #Push is letting numbers into the stack
    def push(self,k):
        if len(self.stack) < self.n:
            self.stack.append(k)
        else:
            print("The stack is Full")
        
    def pop(self):
        if len(self.stack) == 0: #when its empty it should do nothing
            print("The stack is Empty")
        else:
            self.stack.pop(-1) #delete the last number and then go backwards
    
    def top(self):
        if len(self.stack) == 0:
            print("The stack is Empty")
        else:
            return self.stack[-1]
    
    def size(self):
        return len(self.stack)

    def display(self):
        print(self.stack)

s = Stack(3)
s.display()
print(s.size())
s.push(1)
s.push(8)
s.push(5)
s.display()
print(s.size())
s.push(10)
print(s.top())
s.pop()
s.display()
s.pop()
s.pop()
s.display()
s.pop()
print(s.top())