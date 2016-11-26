import time
import re
import glob, os
#Stack Data Structure import
from Stack import Stack
from TST import NodeTST,TST

#LinkedList Data Structure import
from LinkedList import LinkedList,Node

if __name__ == "__main__":
    start_time = time.time()
    i=0
    motherTree = TST()
    # <-- Start Listing Stopwords from the list of "Stopwords" -->
    stopwords = TST()
    with open('StopWords.txt', 'r+') as myfile:
        DATA = myfile.read().replace('\n', ' ')
        for stopword in re.findall(r"[\w']+", DATA):
            node = Node(data=stopword)
            stopwords.push(node, 0)

    # End Listing Stopwords

    dir = input('Please Enter the direction of File: ')
    sum =0
    total = 0



    # Total number of Files

    for root, dirs, files in os.walk(dir):
        total += len([file for file in files if file.endswith('.txt')])
    print(total)

    # Total number of Files




    for subdir, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith('.txt'):
                with open(os.path.join(subdir, file), 'r+',errors='ignore') as myfile:
                    fileLinkedList = LinkedList(documentName=file[:-4])
                    DATA = myfile.read().replace('\n', ' ')
                    for word in re.findall(r"[\w']+", DATA):
                        node = fileLinkedList.add(word)
                        motherTree.push(node, i)
                        i = i + 1

    motherTree.get('people')
    # motherTree.traverse()
    print("--- %s seconds ---" % (time.time() - start_time))