# <--Creating Class Stack-->

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

# <--End of Creating Class Stack-->