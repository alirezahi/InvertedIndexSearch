import time
import re
import glob, os
#Stack Data Structure import
from Stack import Stack
from TST import NodeTST,TST

#LinkedList Data Structure import
from LinkedList import LinkedList

if __name__ == "__main__":
    start_time = time.time()
    i=0

    # <-- Start Listing Stopwords from the list of "Stopwords" -->
    stopwords = TST()
    # with open('StopWords.txt', 'r+') as myfile:
    #     DATA = myfile.read().replace('\n', ' ')
    #     for word in re.findall(r"[\w']+", DATA):
    #         stopwords.push(word, 0)

    # End Listing Stopwords
    fileLinkedList = LinkedList()
    fileLinkedList1 = LinkedList()

    mom = TST()
    j = 0
    with open('StopWords.txt', 'r+') as myfile:
        DATA = myfile.read().replace('\n', ' ')
        for word in re.findall(r"[\w']+", DATA):
            node = fileLinkedList.add(word)
            mom.push(node,j)
            j = j + 1
    mom.traverse()
    mom.get('what')
    # print(fileLinkedList.search('is'))
    # fileLinkedList.remove('is')
    # print(fileLinkedList.search('is'))
    mom.get('is')
    alireza = LinkedList()
    dir = input('Please Enter the direction of File: ')
    for subdir, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith('.txt'):
                with open(os.path.join(subdir, file), 'r+',errors='ignore') as myfile:
                    DATA = myfile.read().replace('\n', ' ')
                    for word in re.findall(r"[\w']+", DATA):
                        # mom.push(word,i)
                        i = i + 1
    print(mom.get('people'))
    # print(alireza.search('Belcher').next.data)
    print("--- %s seconds ---" % (time.time() - start_time))