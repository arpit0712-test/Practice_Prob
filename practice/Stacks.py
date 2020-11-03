class Stack:
    def __init__(self):
        self.list1 = []

    def insert(self, a):
        self.list1.append(a)

    def delete(self):
        self.list1.pop()

    def printStack(self):
        print(self.list1)


stak = Stack()
stak.insert(2)
stak.insert(3)
stak.insert(4)
stak.insert(5)
stak.insert(6)
stak.insert(7)
stak.insert(8)
stak.insert(9)

stak.printStack()

stak.delete()
stak.printStack()