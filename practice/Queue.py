class Queue:

    def __init__(self):
        self.list1 = []

    def insert(self, a):
        self.list1.append(a)

    def delete(self):
        self.list1.pop(0)

    def printQueue(self):
        print(self.list1)


queue = Queue()
queue.insert(1)
queue.insert(2)
queue.insert(3)
queue.insert(4)
queue.insert(5)
queue.insert(6)
queue.insert(7)

queue.printQueue()

queue.delete()
queue.printQueue()
queue.delete()
queue.printQueue()
queue.delete()
queue.printQueue()
queue.delete()
queue.printQueue()
queue.delete()
queue.printQueue()
queue.delete()
queue.printQueue()
