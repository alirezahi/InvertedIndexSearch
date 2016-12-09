import time
import re
import glob, os
import sys
#Stack Data Structure import
from Stack import Stack
from TST import NodeTST,TST
from Trie import Trie,NodeTrie
from BST import BST , NodeBST

#LinkedList Data Structure import
from LinkedList import LinkedList,Node

if __name__ == "__main__":
    file_names = Trie()
    man = Trie()
    start_time = time.time()
    i=0
    motherTree = TST()


    # <-- Start Listing Stopwords in TST from the list of "Stopwords" -->

    stopwordsTST = TST()
    with open('StopWords.txt', 'r+') as myfile:
        DATA = myfile.read().replace('\n', ' ')
        for stopword in re.findall(r"[\w']+", DATA):
            node = Node(data=stopword)
            stopwordsTST.push(node, 0)
    stopwordsTST.get('is').refrence.getAll()
    # <-- End Listing Stopwords TST -->



    # <-- Start Listing Stopwords in BST from the list of "Stopwords" -->

    stopwordsBST = BST()
    with open('StopWords.txt', 'r+') as myfile:
        DATA = myfile.read().replace('\n', ' ')
        for stopword in re.findall(r"[\w']+", DATA):
            node = Node(data=stopword)
            stopwordsBST.add(node)

    # <-- End Listing Stopwords BST -->


    # <-- Start Listing Stopwords in Trie from the list of "Stopwords" -->

    stopwordsTrie = Trie()
    with open('StopWords.txt', 'r+') as myfile:
        DATA = myfile.read().replace('\n', ' ')
        for stopword in re.findall(r"[\w']+", DATA):
            node = Node(data=stopword)
            stopwordsTrie.add(node)

    # <-- End Listing Stopwords Trie -->

    dir = input('Please Enter the direction of File: ')
    sum =0
    total = 0

    # Total number of Files

    # for root, dirs, files in os.walk(dir):
    #     total += len([file for file in files if file.endswith('.txt')])
    # print(total)

    # Total number of Files

    # Trie Research
    for subdir, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith('.txt'):
                with open(os.path.join(subdir, file), 'r+', errors='ignore') as myfile:
                    fileLinkedList = LinkedList(documentName=file[:-4])
                    DATA = myfile.read().replace('\n', ' ')
                    for word in re.findall(r"[\w']+", DATA):
                        node = fileLinkedList.add(word)
                        if stopwordsTrie.get(word) == None:
                            man.add(node)
    man.traverse()

    # Trie Research
    # file_names.traverse()





    # TST Search

    for subdir, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith('.txt'):
                with open(os.path.join(subdir, file), 'r+',errors='ignore') as myfile:
                    fileLinkedList = LinkedList(documentName=file[:-4])
                    DATA = myfile.read().replace('\n', ' ')
                    for word in re.findall(r"[\w']+", DATA):
                        node = fileLinkedList.add(word)
                        if stopwordsTST.get(word) == None:
                            motherTree.push(node, i)
                            i = i + 1
    motherTree.traverse()
    # motherTree.get('people')

    # TST Search

    # BST Search

    myBst = BST()
    for subdir, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith('.txt'):
                with open(os.path.join(subdir, file), 'r+',errors='ignore') as myfile:
                    fileLinkedList = LinkedList(documentName=file[:-4])
                    DATA = myfile.read().replace('\n', ' ')
                    for word in re.findall(r"[\w']+", DATA):
                        node = fileLinkedList.add(word)
                        if stopwordsBST.get(word) == None:
                            myBst.add(node)
    myBst.traverse()

    # BST Search



    print("--- %s seconds ---" % (time.time() - start_time))