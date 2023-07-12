from tkinter import *


def update():
    print("updating the gui")
    root.geometry(f"{input_width.get()}x{input_height.get()}")


root=Tk()
root.geometry("230x100")


input_width=StringVar()
input_height=StringVar()

label=Label(root,text="Enter Width:-")
label.grid(row=0,column=3)

label1=Label(root,text="Enter Height:-")
label1.grid(row=1,column=3)

Entry(root,textvariable=input_width).grid(row=0,column=5)
Entry(root,textvariable=input_height).grid(row=1,column=5)

Button(root,text="Apply",command=update).grid(row=2,column=5)

root.mainloop()
