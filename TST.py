class NodeTST():
    def __init__(self,character = None):
        self.character = character
        self.value = None
        self.leftChild = None
        self.rightChild = None
        self.middleChild = None
        self.completeWord = False

class TST():
    def __init__(self):
        self.root = NodeTST('m')

    def push(self,word,value):
        self.root = self.pushWord(self.root,word,value,0)

    def pushWord(self, node, word, value, charIndex):
        charOfWord = word[charIndex]

        if node == None:
            node = NodeTST(charOfWord)

        if charOfWord < node.character:
            node.leftChild = self.pushWord(node.leftChild,word,value,charIndex)

        elif charOfWord > node.character:
            node.rightChild = self.pushWord(node.rightChild, word, value, charIndex)

        elif charIndex < len(word)-1:
            node.middleChild = self.pushWord(node.middleChild, word, value, charIndex+1)

        else:
            node.value = value
            node.completeWord = True

        return node

    def get(self,word):
        node = self.getWord(self.root,word,0)

        if node == None:
            return None

        return node.value

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
            return node

    def traverse(self,node,charWord=''):
        if(node.leftChild != None):
            self.traverse(node.leftChild,charWord)
        if (node.rightChild != None):
            self.traverse(node.rightChild,charWord)
        if (node.middleChild != None):
            self.traverse(node.middleChild,charWord+node.character)
        if(node.completeWord):
            print (charWord+node.character)