# <--Creating Class LinkedList-->
class Node():
    def __init__( self, data=None,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        self.superNext = None
        self.superPrev = None

class LinkedList():

    def __init__( self ) :
        self.head = Node()
        self.head.prev = None
        self.head.next = None

    def add( self, data ) :
        node = Node(data)
        if self.head.next == None:
            self.head.next = node
            self.head.prev = node
            node.prev = self.head
        else:
            self.head.prev.next = node
            node.prev = self.head.prev
            self.head.prev = node
            self.head.prev.next = self.head
        return node
    def SuperAdd(self,node):
        if self.head.superNext == None:
            self.head.superNext = node
            node.superPrev = self.head
            self.head.superPrev = node
        else:
            self.head.superPrev.superNext = node
            node.prev = self.head.superPrev
            self.head.superPrev = node
            self.head.superPrev.superNext = self.head
        return node

    def search(self, k):
        p = self.head
        while p.next != None:
            p = p.next
            if p.data == k:
                return p
        return None

    def remove( self, inputData ) :
        p = self.search(inputData)
        if p != None:
            p.prev.next = p.next
            p.next.prev = p.prev

    def SuperRemove(self , inputNode):
        if inputNode != None:
            inputNode.superPrev.superNext = inputNode.superNext
            inputNode.superNext.superPrev = inputNode.superPrev
            inputNode.superNext == None
            inputNode.superPrev == None

    def getAll(self):
        p = self.head
        if p.superNext != None:
            while p.superNext != None:
                p = p.superNext
                print(p.data + z.__str__())

    def __str__(self):
        s = ""
        p = self.head
        if p!=None:
            while p.next != None :
                s += p.data
                p = p.next
            s += p.data
        return s

# <--End of Creating Class LinkedList-->