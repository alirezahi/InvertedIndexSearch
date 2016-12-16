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
        self.number_of_words = 0
        self.i = 0
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
            node.refrence.SuperAdd(nodeOfWord,root_tree=self,node_ref=node)
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

        if charOfWord.lower() < node.character :
            return self.getWord(node.leftChild,word,charIndex)

        elif charOfWord.lower() > node.character :
            return self.getWord(node.rightChild,word,charIndex)

        elif charIndex < len(word)-1:
            return self.getWord(node.middleChild,word,charIndex+1)

        else :
            if node.completeWord:
                return node
            else :
                return None

    def traverse(self,node=None,charWord='',sentence = ''):
        if node == None:
            node = self.root
        if(node.leftChild != None):
            sentence = self.traverse(node.leftChild,charWord,sentence)
        if (node.rightChild != None):
            sentence = self.traverse(node.rightChild,charWord,sentence)
        if (node.middleChild != None):
            sentence = self.traverse(node.middleChild,charWord+node.character,sentence)
        if(node.completeWord):
            self.i=self.i+1
            return sentence + (self.i.__str__()+' '+charWord+node.character+'\n')
        else : return sentence

    def traverse_words_documents(self, node=None, charWord='', sentence=''):
        if node == None:
            node = self.root
        if (node.leftChild != None):
            sentence = self.traverse_words_documents(node.leftChild, charWord, sentence)
        if (node.rightChild != None):
            sentence = self.traverse_words_documents(node.rightChild, charWord, sentence)
        if (node.middleChild != None):
            sentence = self.traverse_words_documents(node.middleChild, charWord + node.character, sentence)
        if (node.completeWord):
            node_documents = node.refrence.getDocuments()
            if node_documents is not '':
                self.number_of_words = self.number_of_words + 1
            return sentence + node_documents
        else:
            return sentence

    def height(self, node=None, isRoot=True):
        if isRoot:
            node = self.root
        if node == None:
            return -1
        leftH = self.height(node=node.leftChild, isRoot=False)
        rightH = self.height(node=node.rightChild, isRoot=False)
        middleH = self.height(node=node.middleChild, isRoot=False)
        return max(leftH, rightH, middleH) + 1