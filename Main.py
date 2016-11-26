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
    mom = TST()
    mom.push('mohammad',100)
    mom.push('amin',200)
    mom.push('mohsen',200)
    mom.push('danial',200)
    mom.push('am',200)
    mom.push('moh',200)
    mom.traverse(mom.root)
    alireza = LinkedList()
    dir = input('Please Enter the direction of File: ')
    for subdir, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith('.txt'):
                with open(os.path.join(subdir, file), 'r+',errors='ignore') as myfile:
                    DATA = myfile.read().replace('\n', ' ')
                    for word in re.findall(r"[\w']+", DATA):
                        mom.push(word,i)
                        i = i + 1
    print(mom.get('people'))
    # print(alireza.search('Belcher').next.data)
    print("--- %s seconds ---" % (time.time() - start_time))