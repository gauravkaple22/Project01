from tkinter import *
root=Tk()

root.geometry("655x333")

f1=Frame(root,bg="grey",borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT,fill="y")

f2=Frame(root,bg="grey",borderwidth=9,relief=SUNKEN)
f2.pack(side=TOP,fill="x")

l=Label(f1,text="Tkinter Project- Pycharm")
l.pack(pady=142)

l1=Label(f2,text="Welcome to Sublime text",font="Helvetica  16 bold",fg="red")
l1.pack()

root.mainloop()

