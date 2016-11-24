# import time
import re
import glob, os
# Creating Class Stack

class Stack():
    def __init__(self):
        self.stackArray = []

    def push(self,item):
        self.stackArray.append(item)

    def pop(self):
        popElement = self.stackArray[len(self.stackArray)-1]
        del self.stackArray[len(self.stackArray)-1]
        return popElement

    def peek(self):
        return self.stackArray[len(self.stackArray)-1]

    def isEmpty(self):
        return self.stackArray == []

# End of Creating Class Stack


class Node():
    def __init__( self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList :
    def __init__( self ) :
        self.head = None

    def add( self, data ) :
        node = Node(data)
        if self.head == None :
            self.head = node
        else:
            node.next = self.head
            node.next.prev = node
            self.head = node

    def search(self, k):
        p = self.head
        if p is None:
            while p.next != None :
                if (p.data==k):
                    return p
                p = p.next
            if (p.data==k):
                return p
        return None

    def remove( self, p ) :
        tmp = p.prev
        p.prev.next = p.next
        p.prev = tmp

    def __str__(self):
        s = ""
        p = self.head
        if p!=None:
            while p.next != None :
                s += p.data
                p = p.next
            s += p.data
        return s

if __name__ == "__main__":
    alireza = Stack()
    # print(alireza.pop())
    alireza.push('sdaf')
    print(alireza.pop())
    # start_time = time.time()
    dir = input('Please Enter the direction of File: ')

    for subdir, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith('.txt'):
                with open(os.path.join(subdir, file), 'r+') as myfile:
                    # print('wow')
                    print(subdir + file)
                    DATA = myfile.read().replace('\n', ' ')
                    text = re.findall(r"[\w']+", DATA)
                    print(text)
                    # print(DATA)
    # print("--- %s seconds ---" % (time.time() - start_time))