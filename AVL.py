from LinkedList import LinkedList
from BST import NodeBST
from Stack import Stack

class AVL():
    def __init__(self):
        self.number_of_words =0
        self.i = 0
        self.root = None

    def add(self,node_of_word):
        check_balance_nodes = Stack()
        current_node = self.root
        wordIsAdded = False
        if not current_node:
            current_node = NodeBST(node_of_word.data.lower())
            current_node.refrence.SuperAdd(node_of_word)
            self.root = current_node
            wordIsAdded = True
        while not wordIsAdded:
            if node_of_word.data.lower() > current_node.word:
                check_balance_nodes.push(current_node)
                if current_node.rightChild == None:
                    current_node.rightChild = NodeBST(node_of_word.data.lower())
                    current_node.rightChild.refrence.SuperAdd(node_of_word)
                    wordIsAdded = True
                else :
                    current_node = current_node.rightChild
            elif node_of_word.data.lower() < current_node.word:
                check_balance_nodes.push(current_node)
                if current_node.leftChild == None:
                    current_node.leftChild = NodeBST(node_of_word.data.lower())
                    current_node.leftChild.refrence.SuperAdd(node_of_word)
                    wordIsAdded = True
                else:
                    current_node = current_node.leftChild
            else :
                current_node.refrence.SuperAdd(node_of_word)
                wordIsAdded = True
        while not check_balance_nodes.isEmpty():
            current_checking_node = check_balance_nodes.pop()
            height_of_left = self.height(current_checking_node.leftChild,isRoot=False)
            height_of_right = self.height(current_checking_node.rightChild,isRoot=False)
            if(height_of_left - height_of_right == 2):
                if node_of_word.data>current_checking_node.leftChild.word:
                    # LR rotate in AVL
                    s = current_checking_node.leftChild.rightChild
                    tmpNode = current_checking_node.leftChild
                    current_checking_node.leftChild = s.rightChild
                    tmpNode.rightChild = s.leftChild
                    s.rightChild = current_checking_node
                    s.leftChild = tmpNode
                    if current_checking_node == self.root:
                        self.root = s
                    else:
                        if check_balance_nodes.peek().leftChild == current_checking_node:
                            check_balance_nodes.peek().leftChild = s
                        else:
                            check_balance_nodes.peek().rightChild = s
                else:
                    # LL rotate in AVL
                    tmpNode = current_checking_node.leftChild
                    current_checking_node.leftChild = tmpNode.rightChild
                    tmpNode.rightChild = current_checking_node
                    if current_checking_node == self.root:
                        self.root = tmpNode
                    else:
                        if check_balance_nodes.peek().leftChild == current_checking_node:
                            check_balance_nodes.peek().leftChild = tmpNode
                        else:
                            check_balance_nodes.peek().rightChild = tmpNode
            elif(height_of_right - height_of_left == 2):
                if node_of_word.data>current_checking_node.rightChild.word:
                    # RR rotate in AVL
                    tmpNode = current_checking_node.rightChild
                    current_checking_node.rightChild = tmpNode.leftChild
                    tmpNode.leftChild = current_checking_node
                    if current_checking_node == self.root:
                        self.root = tmpNode
                    else:
                        if check_balance_nodes.peek().leftChild == current_checking_node:
                            check_balance_nodes.peek().leftChild = tmpNode
                        else :
                            check_balance_nodes.peek().rightChild = tmpNode
                else:
                    # RL rotate in AVL
                    s = current_checking_node.rightChild.leftChild
                    tmpNode = current_checking_node.rightChild
                    current_checking_node.rightChild = s.leftChild
                    tmpNode.leftChild = s.rightChild
                    s.leftChild = current_checking_node
                    s.rightChild = tmpNode
                    if current_checking_node == self.root:
                        self.root = s
                    else:
                        if check_balance_nodes.peek().leftChild == current_checking_node:
                            check_balance_nodes.peek().leftChild = s
                        else:
                            check_balance_nodes.peek().rightChild = s
    def get(self, word):
        current_node = self.root
        while current_node!=None:
            if word.lower() == current_node.word:
                return current_node
            if word.lower() > current_node.word:
                current_node = current_node.rightChild
            else :
                current_node = current_node.leftChild
        return None


    def traverse(self,node = None):
        if node == None:
            node = self.root
        if node.leftChild != None:
            self.traverse(node=node.leftChild)
        if node.rightChild != None:
            self.traverse(node=node.rightChild)
        self.i = self.i + 1
        print(self.i.__str__() + ' ' + node.word)

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
