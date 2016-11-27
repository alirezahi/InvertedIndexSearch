from LinkedList import LinkedList

class NodeBST():

    def __init__(self,word=None,isUsableWord=True):
        self.word = word
        self.leftChild = None
        self.rightChild = None
        self.isUsableWord = isUsableWord
        self.refrence = LinkedList()

class BST():

    def __init__(self):
        self.root = NodeBST('m',isUsableWord=False)

    def add(self,node_of_word):
        current_node = self.root
        wordIsAdded = False
        while not wordIsAdded:
            if node_of_word.data.lower() > current_node.word:
                if current_node.leftChild == None:
                    current_node.leftChild = NodeBST(node_of_word.data.lower())
                    current_node.leftChild.refrence.SuperAdd(node_of_word)
                    wordIsAdded = True
                else :
                    current_node = current_node.leftChild
            elif node_of_word.data.lower() < current_node.word:
                if current_node.rightChild == None:
                    current_node.rightChild = NodeBST(node_of_word.data.lower())
                    current_node.rightChild.refrence.SuperAdd(node_of_word)
                    wordIsAdded = True
                else:
                    current_node = current_node.rightChild
            else :
                current_node.refrence.SuperAdd(node_of_word)
                current_node.isUsableWord = True
                wordIsAdded = True

    def get(self, word):
        current_node = self.root
        while current_node!=None:
            if word.lower() == current_node.word and current_node.isUsableWord:
                return current_node
            if word.lower() > current_node.word:
                current_node = current_node.leftChild
            else :
                current_node = current_node.rightChild
        return None


    def traverse(self,node = None):
        if node == None:
            node = self.root
        else:
            print(node.word)
        if node.leftChild != None:
            self.traverse(node=node.leftChild)
        if node.rightChild != None:
            self.traverse(node=node.rightChild)
