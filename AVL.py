from BST import NodeBST
from Stack import Stack

class AVL():
    def __init__(self):
        self.number_of_words =0
        self.i = 0
        self.root = None

    def add(self, node_of_word):
        check_balance_nodes = Stack()
        current_node = self.root
        wordIsAdded = False
        if not current_node:
            current_node = NodeBST(node_of_word.data.lower())
            current_node.refrence.SuperAdd(node_of_word, root_tree=self, node_ref=current_node.rightChild)
            self.root = current_node
            wordIsAdded = True
        while not wordIsAdded:
            if node_of_word.data.lower() > current_node.word:
                check_balance_nodes.push(current_node)
                if current_node.rightChild == None:
                    current_node.rightChild = NodeBST(node_of_word.data.lower())
                    current_node.rightChild.refrence.SuperAdd(node_of_word, root_tree=self,node_ref=current_node.rightChild)
                    wordIsAdded = True
                else:
                    current_node = current_node.rightChild
            elif node_of_word.data.lower() < current_node.word:
                check_balance_nodes.push(current_node)
                if current_node.leftChild == None:
                    current_node.leftChild = NodeBST(node_of_word.data.lower())
                    current_node.leftChild.refrence.SuperAdd(node_of_word, root_tree=self,node_ref=current_node.leftChild)
                    wordIsAdded = True
                else:
                    current_node = current_node.leftChild
            else:
                current_node.refrence.SuperAdd(node_of_word, root_tree=self, node_ref=current_node)
                wordIsAdded = True
        while not check_balance_nodes.isEmpty():
            current_checking_node = check_balance_nodes.pop()
            height_of_left = self.ret_bf(current_checking_node.leftChild)
            height_of_right = self.ret_bf(current_checking_node.rightChild)
            if (height_of_left - height_of_right == 2):
                if node_of_word.data > current_checking_node.leftChild.word:
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
                    self.balance_factor_cal(tmpNode)
                    self.balance_factor_cal(s)
                    self.balance_factor_cal(current_checking_node)
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
                    self.balance_factor_cal(current_checking_node)
                    self.balance_factor_cal(tmpNode)
            elif (height_of_right - height_of_left == 2):
                if node_of_word.data > current_checking_node.rightChild.word:
                    # RR rotate in AVL
                    tmpNode = current_checking_node.rightChild
                    current_checking_node.rightChild = tmpNode.leftChild
                    tmpNode.leftChild = current_checking_node
                    if current_checking_node == self.root:
                        self.root = tmpNode
                    else:
                        if check_balance_nodes.peek().leftChild == current_checking_node:
                            check_balance_nodes.peek().leftChild = tmpNode
                        else:
                            check_balance_nodes.peek().rightChild = tmpNode
                    self.balance_factor_cal(current_checking_node)
                    self.balance_factor_cal(tmpNode)
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
                    self.balance_factor_cal(tmpNode)
                    self.balance_factor_cal(s)
                    self.balance_factor_cal(current_checking_node)
            else:
                self.balance_factor_cal(current_checking_node)

    def get(self, word):
        current_node = self.root
        while current_node != None:
            if word.lower() == current_node.word:
                return current_node
            if word.lower() > current_node.word:
                current_node = current_node.rightChild
            else:
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
                if node_to_delete.rightChild:
                    node_to_delete.rightChild.father = tmp_node
                node_to_delete.leftChild.father = tmp_node
                tmp_node.father = node_to_delete.father
                tmp_node.leftChild = node_to_delete.leftChild
                tmp_node.rightChild = node_to_delete.rightChild
                if node_to_delete == self.root :
                    self.root = tmp_node
                    # node_to_delete.father = None
                else:
                    if node_to_delete.father.leftChild == node_to_delete:
                        node_to_delete.father.leftChild = tmp_node
                        # node_to_delete.father = None
                    else:
                        node_to_delete.father.rightChild = tmp_node
                        # node_to_delete.father = None
            else:
                if node_to_delete == self.root:
                    self.root = node_to_delete.leftChild
                    # node_to_delete.father = None
                else:
                    node_to_delete.leftChild.father = node_to_delete.father
                    if node_to_delete.father.leftChild == node_to_delete:
                        node_to_delete.father.leftChild = node_to_delete.leftChild
                        # node_to_delete.father = None
                    else:
                        node_to_delete.father.rightChild = node_to_delete.leftChild
                        # node_to_delete.father = None
        else :
            if node_to_delete.rightChild:
                if node_to_delete == self.root:
                    self.root = node_to_delete.rightChild
                    # node_to_delete.father = None
                else:
                    node_to_delete.rightChild.father = node_to_delete.father
                    if node_to_delete.father.leftChild == node_to_delete:
                        node_to_delete.father.leftChild = node_to_delete.rightChild
                        # node_to_delete.father = None
                    else:
                        node_to_delete.father.rightChild = node_to_delete.rightChild
                        # node_to_delete.father = None
            else:
                print(node_to_delete.word)
                if node_to_delete == self.root:
                    self.root = NodeBST('m', isUsableWord=False)
                else:
                    if node_to_delete.father.leftChild == node_to_delete:
                        node_to_delete.father.leftChild = None
                        # if node_to_delete.word == 'good':
                        #     print(node_to_delete.father.word)
                    else:
                        node_to_delete.father.rightChild = None

    def traverse(self, node=None):
        if node == None:
            node = self.root
        if node.leftChild != None:
            self.traverse(node=node.leftChild)
        if node.rightChild != None:
            self.traverse(node=node.rightChild)
        self.i = self.i + 1
        print(self.i.__str__() + ' ' + node.word + node.balance_factor.__str__())

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

    def balance_factor_cal(self,node):
        result = 0
        left_bf = -1
        right_bf = -1
        if node.leftChild:
            left_bf = node.leftChild.balance_factor
        if node.rightChild:
            right_bf = node.rightChild.balance_factor
        node.balance_factor = max(left_bf,right_bf)+1

    def ret_bf(self,node):
        if not node :
            return -1
        else:
            return node.balance_factor
