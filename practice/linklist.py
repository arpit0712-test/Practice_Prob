class Node:  # Node class
    # Function to initialize Node object
    def __init__(self, data=None):
        self.data = data  # Assign  data
        self.next = None  # Assign next null


class SinglyLink:
    def __init__(self):
        self.head = None

    def insertionInList(self, newdata):
        NewNode = Node(newdata)

        NewNode.next = self.head
        self.head = NewNode

    def insertAtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return
        lastval = self.head
        while lastval.next:
            lastval = lastval.next
            lastval.next = NewNode

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next


llist = SinglyLink()
llist.head = Node(1)

e2 = Node(2)
e3 = Node(3)

llist.head.next = e2
e2.next = e3
llist.insertionInList("0")

llist.printList()
