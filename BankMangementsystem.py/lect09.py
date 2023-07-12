from tkinter import *
import tkinter.messagebox as tmsg

root=Tk()
root.geometry("733x366")
root.title("Pycharm")


def myfunc():
    print("is it okkkkkk")


def help():
    print("I will help you!")
    a = tmsg.showinfo("Message Box","I can Help you!")


def rate():
    print("Rate Us")
    val=tmsg.askquestion("Was Your Experience Good?","Was Your Experience Good?")
    print(val)
    if val=="yes":
        msg="great,Rate us on  Appstore."
    else:
        msg="Tell us what went wrong ,we will call you soon!"
    tmsg.showinfo("Experience",msg)


yourmenubar = Menu(root)

m1=Menu(yourmenubar,tearoff=0)
m1.add_command(label="New Window",command=myfunc)
m1.add_command(label="Save",command=myfunc)
m1.add_separator()
m1.add_command(label="Save as",command=myfunc)
m1.add_command(label="Print",command=myfunc)
root.config(menu=yourmenubar)
yourmenubar.add_cascade(label="File",menu=m1)


m2=Menu(yourmenubar,tearoff=0)
m2.add_command(label="Cut",command=myfunc)
m2.add_command(label="Copy",command=myfunc)
m2.add_separator()
m2.add_command(label="Paste",command=myfunc)
m2.add_command(label="Find",command=myfunc)
root.config(menu=yourmenubar)
yourmenubar.add_cascade(label="Edit",menu=m2)


m3=Menu(yourmenubar,tearoff=0)
m3.add_command(label="Help",command=help)
m3.add_command(label="Rate Us",command=rate)
yourmenubar.add_cascade(label="Edit",menu=m3)
root.config(menu=yourmenubar)


root.mainloop()
