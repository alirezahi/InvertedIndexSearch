# <--Creating Class Stack-->

class Stack():
    def __init__(self):
        self.stackArray = []

    def push(self,item):
        self.stackArray.append(item)

    def pop(self):
        if not self.isEmpty():
            popElement = self.stackArray[len(self.stackArray)-1]
            del self.stackArray[len(self.stackArray)-1]
            return popElement
        return None

    def peek(self):
        if not self.isEmpty():
            return self.stackArray[len(self.stackArray) - 1]
        return None

    def isEmpty(self):
        return self.stackArray == []

# <--End of Creating Class Stack-->