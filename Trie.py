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
        self.root = NodeTrie()

    def add(self, node_of_word):
        current_node = self.root
        for letter in node_of_word.data :
            if letter.lower() not in current_node.child:
                current_node.addChild(letter.lower())
            current_node = current_node.child[letter.lower()]
            print(current_node.character)
        current_node.refrence.SuperAdd(node_of_word)
        current_node.completeWord = True

    def get(self,word):
        current_node = self.root
        for letter in word:
            if letter.lower() not in current_node.child:
                return None
            current_node = current_node.child[letter.lower()]
        return current_node


