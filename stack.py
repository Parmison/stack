class Stack():
    def __init__(self, n):
        self.stack = []
        self.n = n
    def size(self):
        return len(self.stack)
    def push(self, put):
        if self.size() < self.n:
            self.stack.append(put)
        else:
            print("the stack is full")
    def pop(self):
        if self.size() == 0:
            print("the stack is empty")
        else:
            self.stack.pop(-1)
    def top(self):
        if self.size() == 0:
            print("the stack is empty")
        else:
            return self.stack[-1]
    def display(self):
        print(self.stack)
var = Stack(3)
var.display()
print(var.size())

var.push(13)
var.display()
print(var.size())

var.push(28)
var.display()
print(var.size())

var.push(3)
var.display()
print(var.size())

var.push(8)
var.display()
print(var.size())

var.pop()
var.display()
print(var.size())

print(var.top())
print(var.size())

var.pop()
var.display()
print(var.size())

var.pop()
var.display()
print(var.size())

var.pop()
var.display()
print(var.size())