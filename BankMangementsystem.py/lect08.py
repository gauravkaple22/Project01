from tkinter import *

root=Tk()
root.geometry("733x366")
root.title("Pycharm")


def myfunc():
    print("is it okkkkkk")

# TODO: use this to create non-drop-down menu
# mymenu = Menu(root)
# mymenu.add_command(label="File",command=myfunc)
# mymenu.add_command(label="Exit",command=quit)
#
# root.config(menu=mymenu)


yourmenubar = Menu(root)
m1=Menu(yourmenubar,tearoff=0)
m1.add_command(label="New Window",command=myfunc)
m1.add_command(label="Save",command=myfunc)
m1.add_separator()
m1.add_command(label="Save as",command=myfunc)
m1.add_command(label="Print",command=myfunc)

root.config(menu=yourmenubar)

yourmenubar.add_cascade(label="File",menu=m1)


root.mainloop()
