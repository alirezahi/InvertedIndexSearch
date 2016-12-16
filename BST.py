from LinkedList import LinkedList

class NodeBST():

    def __init__(self,word=None,isUsableWord=True):
        self.word = word
        self.leftChild = None
        self.rightChild = None
        self.isUsableWord = isUsableWord
        self.refrence = LinkedList(node_ref=self)

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
                if current_node.rightChild == None:
                    current_node.rightChild = NodeBST(node_of_word.data.lower())
                    current_node.rightChild.refrence.SuperAdd(node_of_word,root_tree=self,node_ref=current_node.rightChild)
                    current_node.rightChild.father = current_node
                    wordIsAdded = True
                else :
                    current_node = current_node.rightChild
            elif node_of_word.data.lower() < current_node.word:
                if current_node.leftChild == None:
                    current_node.leftChild = NodeBST(node_of_word.data.lower())
                    current_node.leftChild.refrence.SuperAdd(node_of_word,root_tree=self,node_ref=current_node.leftChild)
                    current_node.leftChild.father = current_node
                    wordIsAdded = True
                else:
                    current_node = current_node.leftChild
            else :
                current_node.refrence.SuperAdd(node_of_word,root_tree=self,node_ref=current_node)
                current_node.isUsableWord = True
                wordIsAdded = True

    def get(self, word):
        current_node = self.root
        while current_node:
            if word.lower() == current_node.word and current_node.isUsableWord:
                return current_node
            if word.lower() > current_node.word:
                current_node = current_node.rightChild
            else :
                current_node = current_node.leftChild
        return None

    def find_biggest_left_child(self,node):
        while node.rightChild:
            node = node.rightChild
        return node

    def find_lowest_right_child(self, node):
        while node.leftChild:
            node = node.leftChild
        return node

    def remove(self,node_to_delete):
        if node_to_delete.leftChild:
            if node_to_delete.rightChild:
                tmp_node = self.find_lowest_right_child(node_to_delete.rightChild)
                self.remove(tmp_node)
                tmp_node.father = node_to_delete.father
                tmp_node.leftChild = node_to_delete.leftChild
                tmp_node.rightChild = node_to_delete.rightChild
                if node_to_delete.father.leftChild == node_to_delete:
                    node_to_delete.father.leftChild = tmp_node
                else:
                    node_to_delete.father.rightChild = tmp_node
            else:
                if node_to_delete == self.root:
                    self.root = node_to_delete.leftChild
                    node_to_delete.father = None
                else:
                    node_to_delete.leftChild.father = node_to_delete.father
                    if node_to_delete.father.leftChild == node_to_delete:
                        node_to_delete.father.leftChild = node_to_delete.leftChild
                    else:
                        node_to_delete.father.rightChild = node_to_delete.leftChild
        else :
            if node_to_delete.rightChild:
                if node_to_delete == self.root:
                    self.root = node_to_delete.rightChild
                    node_to_delete.father = None
                else:
                    node_to_delete.rightChild.father = node_to_delete.father
                    if node_to_delete.father.leftChild == node_to_delete:
                        node_to_delete.father.leftChild = node_to_delete.rightChild
                    else:
                        node_to_delete.father.rightChild = node_to_delete.rightChild
            else:
                if node_to_delete.father.leftChild == node_to_delete:
                    node_to_delete.father.leftChild = None
                else:
                    node_to_delete.father.rightChild = None

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

    def height(self,node = None,isRoot = True):
        if isRoot:
            node = self.root
        if node == None:
            return -1
        leftH = self.height(node = node.leftChild,isRoot=False)
        rightH = self.height(node = node.rightChild,isRoot=False)
        return max(leftH,rightH)+1