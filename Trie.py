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
        return current_node

    def traverse(self,current_node=None,charWord=''):
        if current_node == None:
            current_node = self.root
        for current_child in current_node.child.values():
            if current_child != None:
                self.traverse(current_node=current_child,charWord=charWord+current_node.character)
        if current_node.completeWord:
            print(charWord+current_node.character)

    def height(self,node=None):
        if node == None:
            node = self.root
        if len(node.child) == 0:
            return 1
        else :
            return max(self.height(node = c) for c in node.child.values()) + 1