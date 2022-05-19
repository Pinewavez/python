class Node:

    def __init__(self,d,n):
        self.data = d
        self.next = n

    def __str__(self):
        return('(' +str(self.data)+ ')')

class LinkedList:

    def __init__(self):
        self.root = None
        self.size = 0

    def addFront(self,d):
        if self.root == None:
            self.root = Node(d,None)
        else:
            newNode = Node(d,self.root)
            self.root = newNode
        self.size += 1

    def addBack(self,d):
        if self.root == None:
            self.root = Node(d,None)
        else:
            thisNode = self.root
            while thisNode.next:
                thisNode = thisNode.next
            newNode = Node(d,None)
            thisNode.next = newNode
        self.size += 1

    def remove(self,d):
        thisNode = self.root
        prevNode = None
        while thisNode:
            if thisNode.data == d:
                if prevNode == None:
                    self.root = thisNode.next
                prevNode.next = thisNode.next
                self.size -= 1
            prevNode = thisNode
            thisNode = thisNode.next

    def printList(self):
        thisNode = self.root
        while thisNode:
            print(thisNode, end='=>')
            thisNode = thisNode.next
        print('None')

myList = LinkedList()
myList.addFront(32)
myList.printList()
myList.addBack(24)
myList.printList()
myList.addFront(12)
myList.addFront(3)
myList.addFront(54)
myList.addFront(17)
myList.printList()
myList.remove(12)
myList.printList()