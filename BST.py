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
        self.number_of_words =0
        self.i = 0
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
            self.i = self.i+1
            print(self.i.__str__()+' '+node.word)
        if node.leftChild != None:
            self.traverse(node=node.leftChild)
        if node.rightChild != None:
            self.traverse(node=node.rightChild)

    def traverse_words_documents(self, node=None,sentence=''):
        if node == None:
            node = self.root
        if node.leftChild != None:
            sentence = sentence + self.traverse_words_documents(node=node.leftChild)
        if node.rightChild != None:
            sentence = sentence + self.traverse_words_documents(node=node.rightChild)
        if node :
            node_documents = node.refrence.getDocuments()
            if node_documents is not '':
                self.number_of_words = self.number_of_words+1
            return sentence + node_documents
    # def get_num_words(self):
    #     global number_of_words
    #     num = number_of_words
    #     number_of_words=0
    #     return num

    def height(self,node = None,isRoot = True):
        if isRoot:
            node = self.root
        if node == None:
            return -1
        leftH = self.height(node = node.leftChild,isRoot=False)
        rightH = self.height(node = node.rightChild,isRoot=False)
        if isRoot:
            return max(leftH,rightH)+2
        else:
            return max(leftH,rightH)+1
