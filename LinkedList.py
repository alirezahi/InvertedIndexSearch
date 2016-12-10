
# <--Creating Class LinkedList-->
class Node():
    def __init__( self, data=None,next=None,prev=None,documentName = None):
        self.data = data
        self.next = next
        self.prev = prev
        self.superNext = None
        self.superPrev = None
        self.documentName = documentName
        self.isHead = False

class LinkedList():

    def __init__( self ,documentName = None) :
        self.head = Node(documentName)
        self.head.isHead = True
        self.head.prev = None
        self.head.next = None
        self.documentName = documentName

    def add( self, data ) :
        node = Node(data , documentName=self.documentName)
        if self.head.next == None:
            self.head.next = node
            self.head.prev = node
            node.prev = self.head
        else:
            node.prev = self.head.prev
            self.head.prev.next = node
            self.head.prev = node
            node.next = self.head
        return node
    def SuperAdd(self,node):
        if self.head.superNext == None:
            self.head.superNext = node
            node.superPrev = self.head
            node.superNext = self.head
            self.head.superPrev = node
        else:
            self.head.superPrev.superNext = node
            node.superPrev = self.head.superPrev
            self.head.superPrev = node
            node.superNext = self.head
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
        i=0
        p = self.head
        nameOfLastDocument = ''
        result_str = ''
        while p.superNext != self.head and p.superNext != None:
            result_str = result_str + '\n'
            p = p.superNext
            if nameOfLastDocument != p.documentName:
                nameOfLastDocument = p.documentName
                result_str = result_str + p.documentName+'\n'
            result_str = result_str + '( ...'
            if p.prev != None and not p.prev.isHead and p.prev.prev != None and not p.prev.prev.isHead :
                result_str = result_str + ' ' + p.prev.prev.data
            if p.prev != None and not p.prev.isHead :
                result_str = result_str + ' ' + p.prev.data
            result_str = result_str + ' ' + p.data
            if p.next != None and not p.next.isHead:
                result_str = result_str + ' ' + p.next.data
            if p.next != None and not p.next.isHead and p.next.next != None and not p.next.next.isHead:
                result_str = result_str + ' ' + p.next.next.data
            result_str = result_str + ' ... )'
        return result_str

    def getDocuments(self):
        i = 0
        p = self.head
        nameOfLastDocument = ''
        result_str = ''
        next_line = False
        if p.superNext != self.head and p.superNext != None:
            next_line = True
            result_str = result_str + '| ' + p.superNext.data + ' --> '
        while p.superNext != self.head and p.superNext != None:
            p = p.superNext
            if nameOfLastDocument != p.documentName:
                nameOfLastDocument = p.documentName
                result_str = result_str + p.documentName + ' '
        if next_line:
            result_str = result_str + '\n'
        return result_str

    def removeAll(self):
        current_node = self.head
        while current_node.next != self.head:
            current_node = current_node.next
            if current_node.superNext != None:
                self.SuperRemove(current_node)

# <--End of Creating Class LinkedList-->