from LinkedList import LinkedList,Node



class NodeTrie():
    def __init__(self,character = None):
        self.character = character
        self.child = dict()
        self.refrence = LinkedList()
        self.completeWord = False

    def addChild(self, character):
        self.child[character] = NodeTrie(character)

class Trie():
    def __init__(self):
        self.number_of_words = 0
        self.i = 0
        self.root = NodeTrie('')

    def add(self, node_of_word):
        current_node = self.root
        for letter in node_of_word.data :
            if letter.lower() not in current_node.child:
                current_node.addChild(letter.lower())
            current_node = current_node.child[letter.lower()]
        current_node.refrence.SuperAdd(node_of_word)
        current_node.completeWord = True

    def get(self,word):
        current_node = self.root
        for letter in word:
            if letter.lower() not in current_node.child:
                return None
            current_node = current_node.child[letter.lower()]
        if current_node.completeWord:
            return current_node
        else :
            return None

    def traverse(self,current_node=None,charWord='',sentence= ''):
        if current_node == None:
            current_node = self.root
        for current_child in current_node.child.values():
            if current_child != None:
                sentence = self.traverse(current_node=current_child,charWord=charWord+current_node.character,sentence=sentence)
        if current_node.completeWord:
            self.i=self.i+1
            return sentence + (self.i.__str__()+' '+charWord+current_node.character + '\n')
        else:
            return sentence

    def traverse_words_documents(self, current_node=None, charWord='', sentence=''):
        if current_node == None:
            current_node = self.root
        for current_child in current_node.child.values():
            if current_child != None:
                sentence = self.traverse_words_documents(current_node=current_child, charWord=charWord + current_node.character,
                                         sentence=sentence)
        if current_node.completeWord:
            node_documents = current_node.refrence.getDocuments()
            if node_documents is not '':
                self.number_of_words = self.number_of_words + 1
            return sentence + (current_node.refrence.getDocuments())
        else:
            return sentence

    def height(self,node=None):
        if node == None:
            node = self.root
        if len(node.child) == 0:
            return 1
        else :
            return max(self.height(node = c) for c in node.child.values()) + 1