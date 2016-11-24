# import time
import re
import glob, os
#Stack Data Structure import
from Stack import Stack

#LinkedList Data Structure import
from LinkedList import LinkedList

if __name__ == "__main__":
    alireza = LinkedList()
    alireza.add('mom')
    alireza.add('dad')
    alireza.remove('mom')
    alireza.add('you')
    alireza.add('wow')
    alireza.remove('you')
    print(alireza)
    # start_time = time.time()
    dir = input('Please Enter the direction of File: ')

    for subdir, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith('.txt'):
                with open(os.path.join(subdir, file), 'r+') as myfile:
                    DATA = myfile.read().replace('\n', ' ')
                    text = re.findall(r"[\w']+", DATA)
                    print(text)
    # print("--- %s seconds ---" % (time.time() - start_time))