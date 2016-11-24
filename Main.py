# import time
import re
import glob, os
#Stack Data Structure import
from Stack import Stack

#LinkedList Data Structure import
from LinkedList import LinkedList

if __name__ == "__main__":
    mahdi = Stack()
    print(mahdi.peek())
    alireza = LinkedList()
    # start_time = time.time()
    dir = input('Please Enter the direction of File: ')

    for subdir, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith('.txt'):
                with open(os.path.join(subdir, file), 'r+') as myfile:
                    DATA = myfile.read().replace('\n', ' ')
                    for word in re.findall(r"[\w']+", DATA):
                        alireza.add(word)

    print(alireza.search('Belcher').next.data)
    # print("--- %s seconds ---" % (time.time() - start_time))