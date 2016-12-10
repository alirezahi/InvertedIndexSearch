from Stack import Stack

from tkinter import *
import tkinter.filedialog

main_command_line = Entry

main_stack = Stack()
secondary_stack = Stack()
import os

directory_text_field_global = None


resultText = None

def askDirectory(text_label):
    dir = tkinter.filedialog.askdirectory(initialdir='/')
    text_label.delete(0,END)
    text_label.insert(0,str(dir))
    return dir

def tab(arg):
    print("tab pressed")
    return 'break'


def write_result(inputStr):
    resultText.config(state=tkinter.NORMAL)
    resultText.insert(INSERT, inputStr)
    resultText.config(state=tkinter.DISABLED)



def enter(arg):
    while not secondary_stack.isEmpty():
        main_stack.push(secondary_stack.pop())
    command_line_content = main_command_line.get()
    main_stack.push(command_line_content)
    main_command_line.delete(0,END)

    sytax_of_command_line(command_line_content)

    return 'break'

def Reset():
    words_tree = None
    resultText.config(state=tkinter.NORMAL)
    resultText.delete('1.0',END)
    resultText.config(state=tkinter.DISABLED)
    return 'break'

def callback(sv,e):
    if (len(sv.get())>0 and sv.get()[-1] == ''):
        if not main_stack.isEmpty():
            e.delete(0,END)
            secondary_stack.push(main_stack.pop())
            e.insert(0, secondary_stack.peek())
        elif not secondary_stack.isEmpty() :
            e.delete(0, END)
            e.insert(0, secondary_stack.peek())
        else :
            e.delete(0, END)
            e.insert(0, '')
    elif (len(sv.get())>0 and sv.get()[-1] == ''):
        if not secondary_stack.isEmpty():
            e.delete(0, END)
            main_stack.push(secondary_stack.pop())
            if secondary_stack.isEmpty():
                e.insert(0,'')
            else:
                e.insert(0, secondary_stack.peek())
        else :
            e.delete(0, END)
            e.insert(0, '')

directory_var = ""

from TST import TST
from BST import BST
from Trie import Trie

stopwordsTST = None
stopwordsBST = None
stopwordsTrie = None

def Stopwords_def():
    from LinkedList import Node

    # <-- Start Listing Stopwords in TST from the list of "Stopwords" -->
    global stopwordsTST
    stopwordsTST = TST()
    with open('StopWords.txt', 'r+') as myfile:
        DATA = myfile.read().replace('\n', ' ')
        for stopword in re.findall(r"[\w']+", DATA):
            node = Node(data=stopword)
            stopwordsTST.push(node, 0)
    # <-- End Listing Stopwords TST -->



    # <-- Start Listing Stopwords in BST from the list of "Stopwords" -->
    global stopwordsBST
    stopwordsBST = BST()
    with open('StopWords.txt', 'r+') as myfile:
        DATA = myfile.read().replace('\n', ' ')
        for stopword in re.findall(r"[\w']+", DATA):
            node = Node(data=stopword)
            stopwordsBST.add(node)
    # <-- End Listing Stopwords BST -->

    # <-- Start Listing Stopwords in Trie from the list of "Stopwords" -->
    global stopwordsTrie
    stopwordsTrie = Trie()
    with open('StopWords.txt', 'r+') as myfile:
        DATA = myfile.read().replace('\n', ' ')
        for stopword in re.findall(r"[\w']+", DATA):
            node = Node(data=stopword)
            stopwordsTrie.add(node)
    # <-- End Listing Stopwords Trie -->

words_tree = None
from LinkedList import LinkedList
files_list = []
tree_type_global = None
def Build(directory_entered,tree_type):
    global tree_type_global
    tree_type_global = tree_type
    if os.path.isdir(directory_entered.get()):
        from LinkedList import LinkedList
        if tree_type.get() == 1:
            # TST Tree
            global words_tree
            words_tree = TST()
            i=0
            for subdir, dirs, files in os.walk(directory_entered.get()):
                for file in files:
                    if file.endswith('.txt'):
                        with open(os.path.join(subdir, file), 'r+', errors='ignore') as myfile:
                            fileLinkedList = LinkedList(documentName=file[:-4])
                            files_list.append(fileLinkedList)
                            DATA = myfile.read().replace('\n', ' ')
                            for word in re.findall(r"[\w']+", DATA):
                                node = fileLinkedList.add(word)
                                if stopwordsTST.get(word) == None:
                                    words_tree.push(node, i)
                                    i = i + 1
            # TST Tree
        elif tree_type.get() == 2:
            # BST Search
            words_tree = BST()
            for subdir, dirs, files in os.walk(directory_entered.get()):
                for file in files:
                    if file.endswith('.txt'):
                        with open(os.path.join(subdir, file), 'r+', errors='ignore') as myfile:
                            fileLinkedList = LinkedList(documentName=file[:-4])
                            files_list.append(fileLinkedList)
                            DATA = myfile.read().replace('\n', ' ')
                            for word in re.findall(r"[\w']+", DATA):
                                node = fileLinkedList.add(word)
                                if stopwordsBST.get(word) == None:
                                    words_tree.add(node)
            # BST Search

        elif tree_type.get() == 3:
            # Trie Search
            words_tree = Trie()
            for subdir, dirs, files in os.walk(directory_entered.get()):
                for file in files:
                    if file.endswith('.txt'):
                        with open(os.path.join(subdir, file), 'r+', errors='ignore') as myfile:
                            fileLinkedList = LinkedList(documentName=file[:-4])
                            files_list.append(fileLinkedList)
                            DATA = myfile.read().replace('\n', ' ')
                            for word in re.findall(r"[\w']+", DATA):
                                node = fileLinkedList.add(word)
                                if stopwordsTrie.get(word) == None:
                                    words_tree.add(node)
            # Trie Search

    else :
        tkinter.messagebox.showinfo("Directory", "The Directory Entered doesn't Exist")

def sytax_of_command_line(command):
    # <-- It checks the sytax of input command by automata -->
    command_words = command.split()
    current_state=0
    max_non_error_state = 15
    i=0
    while i<len(command_words) and current_state<max_non_error_state:
        if current_state == 0 :
            if command_words[0].lower() == 'add':
                current_state = 1
            elif command_words[0].lower() == 'del':
                current_state = 2
            elif command_words[0].lower() == 'update':
                current_state = 3
            elif command_words[0].lower() == 'list':
                current_state = 4
            elif command_words[0].lower() == 'search':
                current_state = 5
            else :
                current_state = 14
        elif current_state == 1 :
            first_quote = re.match(r'^"(.*)', command_words[1])
            second_quote = re.match(r'(.*)"$', command_words[-1])
            if first_quote and second_quote:
                if command_words[1] == '\"':
                    del command_words[1]
                else:
                    command_words[1] = command_words[1].replace('\"', '')
                if command_words[-1] == '\"':
                    del command_words[-1]
                else:
                    command_words[-1] = command_words[-1].replace('\"', '')
                name_of_file = ''
                for separate_word in command_words[1:]:
                    name_of_file = name_of_file + separate_word
                file_exist = False
                for subdir, dirs, files in os.walk(directory_text_field_global.get()):
                    for file in files:
                        if name_of_file in file:
                            file_exist = True
                if [name_of_file_added for name_of_file_added in files_list if name_of_file_added.documentName == name_of_file].__len__()>0:
                    write_result('Error : Document already Exists!!!\n---------------\n')
                elif not file_exist:
                    write_result('Error : Document not Found!!!\n---------------\n')
                else :
                    if tree_type_global.get() == 1:
                        for subdir, dirs, files in os.walk(directory_text_field_global.get()):
                            for file in files:
                                if name_of_file in file and file.endswith('.txt'):
                                    with open(os.path.join(subdir, file), 'r+', errors='ignore') as myfile:
                                        fileLinkedList = LinkedList(documentName=file[:-4])
                                        files_list.append(fileLinkedList)
                                        DATA = myfile.read().replace('\n', ' ')
                                        for word in re.findall(r"[\w']+", DATA):
                                            node = fileLinkedList.add(word)
                                            if stopwordsTST.get(word) == None:
                                                words_tree.push(node, i)
                                                i = i + 1
                    if tree_type_global.get() == 2:
                        for subdir, dirs, files in os.walk(directory_text_field_global.get()):
                            for file in files:
                                if name_of_file in file and file.endswith('.txt'):
                                    with open(os.path.join(subdir, file), 'r+', errors='ignore') as myfile:
                                        fileLinkedList = LinkedList(documentName=file[:-4])
                                        DATA = myfile.read().replace('\n', ' ')
                                        for word in re.findall(r"[\w']+", DATA):
                                            node = fileLinkedList.add(word)
                                            if stopwordsBST.get(word) == None:
                                                words_tree.add(node)
                    if tree_type_global.get() == 3:
                        for subdir, dirs, files in os.walk(directory_text_field_global.get()):
                            for file in files:
                                if name_of_file in file and file.endswith('.txt'):
                                    with open(os.path.join(subdir, file), 'r+', errors='ignore') as myfile:
                                        fileLinkedList = LinkedList(documentName=file[:-4])
                                        files_list.append(fileLinkedList)
                                        DATA = myfile.read().replace('\n', ' ')
                                        for word in re.findall(r"[\w']+", DATA):
                                            node = fileLinkedList.add(word)
                                            if stopwordsTrie.get(word) == None:
                                                words_tree.add(node)
                    write_result('File' + name_of_file + 'Added\n---------------\n')
            else:
                write_result('Error Happend\n---------------\n')
            return True
        elif current_state == 2:
            first_quote = re.match(r'^"(.*)', command_words[1])
            second_quote = re.match(r'(.*)"$', command_words[-1])
            if first_quote and second_quote:
                if command_words[1] == '\"':
                    del command_words[1]
                else :
                    command_words[1] = command_words[1].replace('\"', '')
                if command_words[-1] == '\"':
                    del command_words[-1]
                else :
                    command_words[-1] = command_words[-1].replace('\"', '')
                name_of_file = ''
                for separate_word in command_words[1:]:
                    name_of_file = name_of_file + separate_word
                file_name_found = False
                files_to_delete = [name_of_file_added for name_of_file_added in files_list if name_of_file_added.documentName == name_of_file]
                for file_going_to_delete in files_to_delete:
                    file_name_found = True
                    file_going_to_delete.removeAll()
                    files_list.remove(file_going_to_delete)
                    del file_going_to_delete
                    write_result('File ' + name_of_file + ' Deleted\n---------------\n')
                if not file_name_found:
                    write_result(resultText.insert(INSERT, 'Error : Document not Found!!!\n---------------\n'))
            else:
                write_result('Error Happend\n---------------\n')

            return True
        elif current_state == 3:
            first_quote = re.match(r'^"(.*)', command_words[1])
            second_quote = re.match(r'(.*)"$', command_words[-1])
            if first_quote and second_quote:
                if command_words[1] == '\"':
                    del command_words[1]
                else:
                    command_words[1] = command_words[1].replace('\"', '')
                if command_words[-1] == '\"':
                    del command_words[-1]
                else:
                    command_words[-1] = command_words[-1].replace('\"', '')
                name_of_file = ''
                for separate_word in command_words[1:]:
                    name_of_file = name_of_file + separate_word
                file_name_found = False
                files_to_delete = [name_of_file_added for name_of_file_added in files_list if
                                   name_of_file_added.documentName == name_of_file]
                for file_going_to_delete in files_to_delete:
                    file_name_found = True
                    file_going_to_delete.removeAll()
                    files_list.remove(file_going_to_delete)
                    del file_going_to_delete
                    if tree_type_global.get() == 1:
                        for subdir, dirs, files in os.walk(directory_text_field_global.get()):
                            for file in files:
                                if name_of_file in file and file.endswith('.txt'):
                                    with open(os.path.join(subdir, file), 'r+', errors='ignore') as myfile:
                                        fileLinkedList = LinkedList(documentName=file[:-4])
                                        files_list.append(fileLinkedList)
                                        DATA = myfile.read().replace('\n', ' ')
                                        for word in re.findall(r"[\w']+", DATA):
                                            node = fileLinkedList.add(word)
                                            if stopwordsTST.get(word) == None:
                                                words_tree.push(node, i)
                                                i = i + 1
                    if tree_type_global.get() == 2:
                        for subdir, dirs, files in os.walk(directory_text_field_global.get()):
                            for file in files:
                                if name_of_file in file and file.endswith('.txt'):
                                    with open(os.path.join(subdir, file), 'r+', errors='ignore') as myfile:
                                        fileLinkedList = LinkedList(documentName=file[:-4])
                                        DATA = myfile.read().replace('\n', ' ')
                                        for word in re.findall(r"[\w']+", DATA):
                                            node = fileLinkedList.add(word)
                                            if stopwordsBST.get(word) == None:
                                                words_tree.add(node)
                    if tree_type_global.get() == 3:
                        for subdir, dirs, files in os.walk(directory_text_field_global.get()):
                            for file in files:
                                if name_of_file in file and file.endswith('.txt'):
                                    with open(os.path.join(subdir, file), 'r+', errors='ignore') as myfile:
                                        fileLinkedList = LinkedList(documentName=file[:-4])
                                        files_list.append(fileLinkedList)
                                        DATA = myfile.read().replace('\n', ' ')
                                        for word in re.findall(r"[\w']+", DATA):
                                            node = fileLinkedList.add(word)
                                            if stopwordsTrie.get(word) == None:
                                                words_tree.add(node)
                    write_result('File' + name_of_file + 'Updated\n---------------\n')
                if not file_name_found:
                    write_result('Error : Document not Found!!!\n---------------\n')
            else:
                write_result('Error Happend\n---------------\n')

            return True
        elif current_state == 4:
            if command_words[1] == '-w':
                current_state = 9
            elif command_words[1] == '-l':
                current_state = 10
            elif command_words[1] == '-f':
                current_state = 11
        elif current_state == 5:
            if command_words[1] == '-s':
                current_state = 12
            elif command_words[1] == '-w':
                current_state = 13
        elif current_state == 6:
            return True
        elif current_state == 7:
            return True
        elif current_state == 8:
            return True
        elif current_state == 9:
            write_result(words_tree.traverse_words_documents())
            write_result('Number of all Words : '+str(words_tree.number_of_words) + '\n---------------\n')
            words_tree.number_of_words = 0
            return True
        elif current_state == 10:
            for file in files_list:
                write_result(file.documentName+' ')
            write_result('\nNumber of listed Docs = ' + files_list.__len__().__str__()+'\n---------------\n')
            return True
        elif current_state == 11:
            number_of_files = 0
            for subdir, dirs, files in os.walk(directory_text_field_global.get()):
                for file in files:
                    if file.endswith('.txt'):
                        write_result(file[:-4] + ' ')
                        number_of_files = number_of_files + 1
            write_result('\nNumber of all Docs = ' + number_of_files.__str__()+'\n---------------\n')
            return True

        elif current_state == 12:
            first_quote = re.match(r'^"(.*)', command_words[2])
            second_quote = re.match(r'(.*)"$', command_words[-1])
            if first_quote and second_quote:
                if not first_quote.group(1) == '\"':
                    command_words[2] = command_words[2].replace('\"', '')
                if not second_quote.group(1) == '\"':
                    command_words[-1] = command_words[-1].replace('\"', '')
            else:
                write_result('Error Happend\n---------------\n')
            if command_words[-1] is command_words[2]:
                if not words_tree.get(command_words[-1]):
                    write_result('\nAny word found !!!\n---------------\n')
                else:
                    write_result(words_tree.get(command_words[-1]).refrence.getAll())
            current_state = 20     # <-- This live has to change -->
            return True
        elif current_state == 13:
            first_quote = re.match(r'^"(.*)', command_words[2])
            second_quote = re.match(r'(.*)"$', command_words[-1])
            if first_quote and second_quote:
                if not first_quote.group(1) == '\"':
                    command_words[2] = command_words[2].replace('\"', '')
                if not second_quote.group(1) == '\"':
                    command_words[-1] = command_words[-1].replace('\"', '')
            else:
                write_result('Error Happend\n---------------\n')
            if command_words[-1] is command_words[2]:
                if not words_tree.get(command_words[-1]):
                    write_result('Any word found !!!\n---------------\n')
                else:
                    write_result(words_tree.get(command_words[-1]).refrence.getAll())
            current_state = 20     # <-- This live has to change -->
            return True
        else:
            write_result('Error : Unkown Command\n---------------\n')
            return True
    return True

if __name__ == '__main__':

    search_var = IntVar

    Stopwords_def()

    root = Tk()
    frame = Frame(root)
    frame.pack()

    directoryframe = Frame(root)
    directoryframe.pack( side = TOP )

    directory_label = Label(directoryframe , text="Please Enter the Directory: ")
    directory_label.pack(side=TOP)

    directory_text_field = Entry(directoryframe,textvariable = directory_var,width=30)
    directory_text_field.pack(side = LEFT)
    directory_text_field_global = directory_text_field

    blackbutton = Button(directoryframe, text="Browse", command = lambda : askDirectory(directory_text_field))
    blackbutton.pack( side = RIGHT)

    resultframe = LabelFrame(root , text= 'Result:')
    resultframe.pack()

    text = Text(resultframe , width=50)
    scroll = Scrollbar(resultframe, command=text.yview)
    text.pack()

    text.configure(yscrollcommand=scroll.set)
    text.config(state=tkinter.DISABLED)
    resultText = text

    search_ds = LabelFrame(root , text='Search Data Structure:')
    search_ds.pack()

    var = IntVar()

    R1 = Radiobutton(search_ds, text="TST", variable=var, value=1)
    R1.pack( side = LEFT )
    R1.invoke()

    R2 = Radiobutton(search_ds, text="BST", variable=var, value=2)
    R2.pack( side = LEFT )

    R3 = Radiobutton(search_ds, text="Trie", variable=var, value=3)
    R3.pack( side = LEFT )

    command_line_frame = LabelFrame(root,text='Command Line : ')
    command_line_frame.pack()

    sv = StringVar()
    command_line = Entry(command_line_frame , width=40,textvariable=sv)
    sv.trace("w", lambda name, index, mode, sv=sv: callback(sv,command_line))
    command_line.bind('<Tab>', tab)
    command_line.bind('<Return>', enter)
    command_line.pack(side=LEFT)
    main_command_line = command_line

    buttons_frame = Frame(root)
    buttons_frame.pack()

    build_button = Button(buttons_frame, text="Build", command=lambda: Build(directory_text_field,var))
    build_button.pack(side=LEFT)

    build_button = Button(buttons_frame, text="Reset", command=lambda: Reset())
    build_button.pack(side=LEFT)

    build_button = Button(buttons_frame, text="Exit", command=lambda: root.destroy())
    build_button.pack(side=RIGHT)

    build_button = Button(buttons_frame, text="Help", command=lambda: askDirectory(directory_text_field))
    build_button.pack(side=RIGHT)


    root.mainloop()