# from tkinter import *
#
# class Application(Frame):
#     def say_hi(self):
#         print ("hi there, everyone!")
#
#     def createWidgets(self):
#         self.QUIT = Button(self)
#         self.QUIT["text"] = "QUIT",
#         self.QUIT["fg"]   = "red"
#         self.QUIT["command"] =  self.quit
#
#         self.QUIT.pack({"side": "left"})
#
#         self.hi_there = Button(self)
#         self.hi_there["text"] = "Hello",
#         self.hi_there["command"] = self.say_hi
#
#         self.hi_there.pack({"side": "left"})
#
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()
#
# root = Tk()
# app = Application(master=root)
# app.mainloop()
# root.destroy()


from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
#
# class MyFrame(Frame):
#     def __init__(self):
#         Frame.__init__(self)
#         self.master.title("Example")
#         self.master.rowconfigure(5, weight=1)
#         self.master.columnconfigure(5, weight=1)
#         self.grid(sticky=W+E+N+S)
#
#         self.button = Button(self, text="Browse", command=self.load_file, width=10)
#         self.button.grid(row=1, column=0, sticky=W)
#
#     def load_file(self):
#         fname = askopenfilename(filetypes=(("Template files", "*.tplate"),
#                                            ("HTML files", "*.html;*.htm"),
#                                            ("All files", "*.*") ))
#         if fname:
#             try:
#                 print("""here it comes: self.settings["template"].set(fname)""")
#             except:                     # <- naked except is a bad idea
#                 showerror("Open Source File", "Failed to read file\n'%s'" % fname)
#             return
#
#
# if __name__ == "__main__":
#     MyFrame().mainloop()

# import sys
# def onclick():
#    pass
#
# root = Tk()
# text = Text(root)
# text.insert(INSERT, "Hello.....")
# text.insert(END, "Bye Bye.....")
# text.pack()
#
# text.tag_add("here", "1.0", "1.4")
# text.tag_add("start", "1.8", "1.13")
# text.tag_config("here", background="yellow", foreground="blue")
# text.tag_config("start", background="black", foreground="green")
# root.mainloop()

from tkinter import *
import tkinter.filedialog

def askDirectory(text_label):
    print('bitch')
    dir = tkinter.filedialog.askdirectory(initialdir='/')
    text_label.delete(0,END)
    text_label.insert(0,str(dir))
    return dir



directory_var = ""



if __name__ == '__main__':

    search_var = IntVar


    root = Tk()
    frame = Frame(root)
    frame.pack()

    directoryframe = Frame(root)
    directoryframe.pack( side = TOP )

    directory_label = Label(directoryframe , text="Please Enter the Directory: ")
    directory_label.pack(side=TOP)

    directory_text_field = Entry(directoryframe,textvariable = directory_var,width=30)
    directory_text_field.pack(side = LEFT)

    blackbutton = Button(directoryframe, text="Browse", command = lambda : askDirectory(directory_text_field))
    blackbutton.pack( side = RIGHT)

    resultframe = LabelFrame(root , text= 'Result:')
    resultframe.pack()

    text = Text(resultframe , width=50)
    scroll = Scrollbar(resultframe, command=text.yview)
    text.pack()

    text.configure(yscrollcommand=scroll.set)
    text.insert(INSERT,'u only live twice')
    text.config(state=DISABLED)

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

    command_line_frame = Frame(root)
    command_line_frame.pack()

    command_line = Entry(command_line_frame , width=40)
    command_line.pack(side=LEFT)

    buttons_frame = Frame(root)
    buttons_frame.pack()

    build_button = Button(buttons_frame, text="Build", command=lambda: askDirectory(directory_text_field))
    build_button.pack(side=LEFT)

    build_button = Button(buttons_frame, text="Reset", command=lambda: askDirectory(directory_text_field))
    build_button.pack(side=LEFT)

    build_button = Button(buttons_frame, text="Help", command=lambda: askDirectory(directory_text_field))
    build_button.pack(side=RIGHT)

    build_button = Button(buttons_frame, text="Exit", command=lambda: askDirectory(directory_text_field))
    build_button.pack(side=RIGHT)

    root.mainloop()




# top = Tk()
#
# Lb1 = Listbox(top)
# Lb1.insert(1, "Python")
# Lb1.insert(2, "Perl")
# Lb1.insert(3, "C")
# Lb1.insert(4, "PHP")
# Lb1.insert(5, "JSP")
# Lb1.insert(6, "Ruby")
# Lb1.delete(1)
# Lb1.pack()
# top.mainloop()




# root = Tk()
#
# var = StringVar()
# label = Message( root, textvariable=var, relief=RAISED )
#
# var.set("Hey!? How are you doing?")
# label.pack()
# root.mainloop()





# def sel():
#    selection = "You selected the option " + str(var.get())
#    label.config(text = selection)
#
# root = Tk()
# var = IntVar()
# R1 = Radiobutton(root, text="Option 1", variable=var, value=1,
#                   command=sel)
# R1.pack( anchor = W )
#
# R2 = Radiobutton(root, text="Option 2", variable=var, value=2,
#                   command=sel)
# R2.pack( anchor = W )
#
# R3 = Radiobutton(root, text="Option 3", variable=var, value=3,
#                   command=sel)
# R3.pack( anchor = W )
#
# label = Label(root)
# label.pack()
# root.mainloop()



# root = Tk()
#
# labelframe = LabelFrame(root, text="This is a LabelFrame")
# labelframe.pack(fill="both", expand="yes")
#
# left = Label(labelframe, text="Inside the LabelFrame")
# left.config(text = 'wow')
# left.pack()
import time
import curses
import os
# os.environ['TERM'] = 'xterm'
# win = curses.initscr()
# # Turn off line buffering
# curses.cbreak()
#
# # Initialize the terminal
# win = curses.initscr()
#
# # Make getch() non-blocking
# win.nodelay(True)
#
# while True:
#     key = win.getch()
#     if key != -1:
#         print('Pressed key', key)
#     time.sleep(0.01)

# class StdOutWrapper:
#     text = ""
#     def write(self,txt):
#         self.text += txt
#         self.text = '\n'.join(self.text.split('\n')[-30:])
#     def get_text(self,beg,end):
#         return '\n'.join(self.text.split('\n')[beg:end])
#
# if __name__ == "__main__":
#     print('adsf')
#     mystdout = StdOutWrapper()
#     sys.stdout = mystdout
#     sys.stderr = mystdout
#     screen = curses.initscr()
#     curses.noecho()
#     curses.cbreak()
#
#     # do your stuff here
#     # you can also output mystdout.get_text() in a ncurses widget in runtime
#
#     screen.keypad(0)
#     curses.nocbreak()
#     curses.echo()
#     curses.endwin()
#     sys.stdout = sys.__stdout__
#     sys.stderr = sys.__stderr__
#     sys.stdout.write(mystdout.get_text())
