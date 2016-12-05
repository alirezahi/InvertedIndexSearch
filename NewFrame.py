from tkinter import *

def callback(sv):
    if (len(sv.get())>0 and sv.get()[-1] == ''):
        print('fuck')
        e.delete(0,END)
        e.insert(0,'a')
    print (sv.get())

root = Tk()
sv = StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
e = Entry(root, textvariable=sv)
e.pack()
root.mainloop()