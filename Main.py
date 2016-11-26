# import time
import re
import glob, os
#Stack Data Structure import
from Stack import Stack
from TST import NodeTST,TST

#LinkedList Data Structure import
from LinkedList import LinkedList

if __name__ == "__main__":
    # start_time = time.time()
    i=0
    mom = TST()
    alireza = LinkedList()
    dir = input('Please Enter the direction of File: ')
    for subdir, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith('.txt'):
                with open(os.path.join(subdir, file), 'r+') as myfile:
                    DATA = myfile.read().replace('\n', ' ')
                    for word in re.findall(r"[\w']+", DATA):
                        mom.push(word,i)
                        i = i + 1
    print(mom.get('allowed'))
    # print(alireza.search('Belcher').next.data)
    # print("--- %s seconds ---" % (time.time() - start_time))