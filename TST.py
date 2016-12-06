from LinkedList import Node,LinkedList

class NodeTST():
    def __init__(self,character = None):
        self.character = character
        self.value = None
        self.leftChild = None
        self.rightChild = None
        self.middleChild = None
        self.completeWord = False
        self.refrence = LinkedList()

class TST():
    def __init__(self):
        self.root = NodeTST('m')

    def push(self,nodeOfWord,value):
        self.root = self.pushWord(self.root,nodeOfWord,value,0)

    def pushWord(self, node, nodeOfWord, value, charIndex):
        charOfWord = nodeOfWord.data[charIndex].lower()

        if node == None:
            node = NodeTST(charOfWord)

        if charOfWord < node.character:
            node.leftChild = self.pushWord(node.leftChild,nodeOfWord,value,charIndex)

        elif charOfWord > node.character:
            node.rightChild = self.pushWord(node.rightChild, nodeOfWord, value, charIndex)

        elif charIndex < len(nodeOfWord.data)-1:
            node.middleChild = self.pushWord(node.middleChild, nodeOfWord, value, charIndex+1)

        else:
            node.value = value
            node.refrence.SuperAdd(nodeOfWord)
            node.completeWord = True

        return node

    def get(self,word):
        node = self.getWord(self.root,word,0)

        if node == None:
            return None

        return node

    def getWord(self, node , word, charIndex):

        if node == None:
            return None

        charOfWord = word[charIndex]

        if charOfWord < node.character :
            return self.getWord(node.leftChild,word,charIndex)

        elif charOfWord > node.character :
            return self.getWord(node.rightChild,word,charIndex)

        elif charIndex < len(word)-1:
            return self.getWord(node.middleChild,word,charIndex+1)

        else :
            if node.refrence == None:
                return None
            return node.refrence.getAll()

    def traverse(self,node=None,charWord=''):
        if node == None:
            node = self.root
        if(node.leftChild != None):
            self.traverse(node.leftChild,charWord)
        if (node.rightChild != None):
            self.traverse(node.rightChild,charWord)
        if (node.middleChild != None):
            self.traverse(node.middleChild,charWord+node.character)
        if(node.completeWord):
            print (charWord+node.character)

    def height(self, node=None, isRoot=True):
        if isRoot:
            node = self.root
        if node == None:
            return -1
        leftH = self.height(node=node.leftChild, isRoot=False)
        rightH = self.height(node=node.rightChild, isRoot=False)
        middleH = self.height(node=node.middleChild, isRoot=False)
        if isRoot:
            return max(leftH,rightH,middleH)+2
        else:
            return max(leftH, rightH, middleH) + 1