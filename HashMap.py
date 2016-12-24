from LinkedList import *
class HashMap():
    def __init__(self):
        self.list_of_words = ['']*15000

    def hash_function(self,word):
        hash_num=0
        i=0
        for letter in word:
            hash_num = hash_num + ord(letter)*(int(i/5)+1)
            i = i + 1
        return hash_num

    def add(self,node_of_word):
        if self.list_of_words[self.hash_function(node_of_word.data)] == '':
            print('shit')
            self.list_of_words[self.hash_function(node_of_word.data)] = LinkedList()
            node = self.list_of_words[self.hash_function(node_of_word.data)].add(node_of_word.data)
            node.LinkedList_of_node = LinkedList()
            node.LinkedList_of_node.SuperAdd(node_of_word)
        else:
            element = self.list_of_words[self.hash_function(node_of_word.data)].search(node_of_word.data)
            if element:
                element.LinkedList_of_node.SuperAdd(node_of_word)
            else:
                print('fuck')
                node = self.list_of_words[self.hash_function(node_of_word.data)].add(node_of_word.data)
                node.LinkedList_of_node = LinkedList()
                node.LinkedList_of_node.SuperAdd(node_of_word)
                self.list_of_words[self.hash_function(node_of_word.data)].search('node')

    def get(self,word):
        if self.list_of_words[self.hash_function(word)]!='':
            node = self.list_of_words[self.hash_function(word)].search(word)
            if node:
                print(node.data)
            else:
                print('not found')
        else:print('not found')

if __name__ == '__main__':
    alireza = HashMap()
    alireza.add(Node('word'))
    alireza.add(Node('rowd'))
    alireza.get('rowd')
    alireza.get('love')