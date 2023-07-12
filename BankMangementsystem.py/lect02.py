from tkinter import *
root=Tk()

root.geometry("433x444")


def name():
    print("correct it!")


def hello():
    print("perform it!")


def msd():
    print("Achieve it!")


def grd():
    print("Do it!")


f=Frame(root,relief=SUNKEN,bg="grey",borderwidth=6)
f.pack(side=LEFT,anchor="nw")

b=Button(f,fg="red",text="print now",command=name)
b.pack(side=LEFT,padx=23)

b1=Button(f,fg="red",text="print now",command=hello)
b1.pack(side=LEFT,padx=23)

b2=Button(f,fg="red",text="print now",command=msd)
b2.pack(side=LEFT,padx=23)

b3=Button(f,fg="red",text="print now",command=grd)
b3.pack(side=LEFT,padx=23)


root.mainloop()
