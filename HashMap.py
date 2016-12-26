from LinkedList import *
class HashMap():
    def __init__(self):
        self.number_of_words=0
        self.list_of_words = ['']*1000

    def hash_function(self,word):
        hash_num=0
        i=0
        for letter in word:
            hash_num = hash_num + ord(letter.lower())*(int(i/5)+1)
            i = i + 1
        return hash_num%1000

    def add(self,node_of_word):
        if self.list_of_words[self.hash_function(node_of_word.data)] == '':
            self.list_of_words[self.hash_function(node_of_word.data)] = LinkedList()
            node = self.list_of_words[self.hash_function(node_of_word.data)].add(node_of_word.data)
            node.refrence = LinkedList()
            node.hash_num = self.hash_function(node_of_word.data)
            node.refrence.SuperAdd(node_of_word,root_tree=self,node_ref=node)
        else:
            element = self.list_of_words[self.hash_function(node_of_word.data)].search(node_of_word.data)
            if element:
                element.refrence.SuperAdd(node_of_word,root_tree=self,node_ref=element)
            else:
                node = self.list_of_words[self.hash_function(node_of_word.data)].add(node_of_word.data)
                node.refrence = LinkedList()
                node.hash_num = self.hash_function(node_of_word.data)
                node.refrence.SuperAdd(node_of_word,root_tree=self,node_ref=node)

    def get(self,word):
        if self.list_of_words[self.hash_function(word)]!='':
            node = self.list_of_words[self.hash_function(word)].search(word)
            if node:
                return node
        return None

    def remove(self,node):
        if node.prev == node.next:
            self.list_of_words[node.hash_num] = ''
        else:
            self.list_of_words[node.hash_num].remove(node.data)


    def traverse(self):
        for element in self.list_of_words:
            if element != '':
                current_linked = element.head
                while current_linked.next != None and current_linked.next != element.head:
                    current_linked = current_linked.next
                    print(current_linked.refrence.head.superNext.data+' ' + str(self.hash_function(current_linked.refrence.head.superNext.data)))

    def traverse_words_documents(self):
        result_str = ''
        for element in self.list_of_words:
            if element != '':
                current_linked = element.head
                while current_linked.next != None and current_linked.next != element.head:
                    current_linked = current_linked.next
                    self.number_of_words = self.number_of_words + 1
                    result_str = result_str + current_linked.refrence.getDocuments()
        return result_str